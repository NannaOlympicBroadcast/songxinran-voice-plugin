#!/usr/bin/env python3
"""宋昕冉 AI 音色转换：本地 GPU 优先，无 GPU 回退 ModelScope 创空间。
粉丝自制、非官方、非商用；输出为 AI 合成声音。
"""
import argparse, os, shutil, subprocess, sys, glob

SPK = "songxinran"
DEFAULT_STUDIO = "yanyan0406/snh48songxinran-sovits-demo"


def has_gpu():
    if shutil.which("nvidia-smi"):
        try:
            return subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True, timeout=15).stdout.strip() != ""
        except Exception:
            pass
    return False


def run_local(a):
    root = os.environ.get("SXR_SOVITS_DIR")
    if not root or not os.path.isdir(root):
        raise SystemExit("本地模式需要设置 SXR_SOVITS_DIR 指向 so-vits-svc 4.1 目录（含 inference_main.py、logs/44k/G_*.pth）")
    py = os.environ.get("SXR_PYTHON", sys.executable)
    ckpt = os.environ.get("SXR_CKPT", os.path.join("logs", "44k", "G_9600.pth"))
    cfg = os.environ.get("SXR_CONFIG", os.path.join("logs", "44k", "config.json"))
    raw = os.path.join(root, "raw"); res = os.path.join(root, "results")
    os.makedirs(raw, exist_ok=True); os.makedirs(res, exist_ok=True)
    name = "sxr_in.wav"
    shutil.copyfile(a.input, os.path.join(raw, name))
    for f in glob.glob(os.path.join(res, name + "*")):
        os.remove(f)
    cmd = [py, "inference_main.py", "-m", ckpt, "-c", cfg, "-n", name, "-t", str(a.key),
           "-s", SPK, "-f0p", "rmvpe", "-d", "cuda", "-wf", "wav", "-ns", str(a.noise)]
    if not a.no_enhance:
        cmd.append("-eh")
    print("[local] " + " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=root)
    if r.returncode != 0:
        raise SystemExit(f"本地推理失败（exit {r.returncode}），请查看上方日志")
    outs = sorted(glob.glob(os.path.join(res, name + "*")), key=os.path.getmtime)
    if not outs:
        raise SystemExit("未在 results/ 找到输出文件")
    shutil.copyfile(outs[-1], a.out)


def run_cloud(a):
    try:
        from gradio_client import Client, handle_file
    except ImportError:
        raise SystemExit("云端回退需要 gradio_client：pip install gradio_client")
    url = os.environ.get("SXR_STUDIO_URL")
    if not url:
        sid = os.environ.get("SXR_STUDIO_ID", DEFAULT_STUDIO)
        url = "https://" + sid.replace("/", "-").replace("_", "-").lower() + ".ms.show"
    print(f"[cloud] {url}（免费 CPU，较慢，单段 ≤60s）", flush=True)
    c = Client(url)
    res = c.predict(handle_file(a.input), a.key, True, api_name="/convert")
    path = res[0] if isinstance(res, (list, tuple)) else res
    shutil.copyfile(path, a.out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True); p.add_argument("--out", required=True)
    p.add_argument("--key", type=int, default=0); p.add_argument("--noise", type=float, default=0.2)
    p.add_argument("--no-enhance", action="store_true")
    p.add_argument("--backend", choices=["auto", "local", "cloud"], default="auto")
    a = p.parse_args()
    if not os.path.isfile(a.input):
        raise SystemExit(f"输入文件不存在：{a.input}")
    b = a.backend
    if b == "auto":
        b = "local" if (has_gpu() and os.environ.get("SXR_SOVITS_DIR")) else "cloud"
        print(f"[auto] 选择后端：{b}", flush=True)
    (run_local if b == "local" else run_cloud)(a)
    print(f"完成：{a.out}  —— AI 生成，非本人演唱，粉丝自制、非商用。")


if __name__ == "__main__":
    main()
