---
name: songxinran-voice
description: 用「宋昕冉 AI 音色」做人声转换/翻唱（so-vits-svc 4.1）。本机有 NVIDIA GPU 时默认本地推理，没有 GPU 时自动回退 ModelScope 创空间。用户说"用宋昕冉的声音""宋昕冉翻唱/AI 翻唱/语音转换"时使用。
---

# 宋昕冉 AI 音色转换

## 合规前提（每次都要遵守）
- 这是**粉丝自制、非官方、非商用**的 AI 音色模型，模型未获本人授权。
- 输出一律在文件名/说明里标注「AI 生成 / AI 翻唱」，不得冒充本人、诈骗、骚扰或商用。
- 只处理用户有权使用的**纯人声**（先用 demucs 等分离伴奏），建议单段不超过 60 秒（云端回退有此限制）。
- 若用户要求冒充本人发布，拒绝并说明。

## 用法
先让用户确认输入是干声（vocals）。然后运行：

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/svc.py" --input <干声.wav> --out <输出.wav> [--key 0] [--backend auto|local|cloud]
```

- `--backend auto`（默认）：检测到 NVIDIA GPU（`nvidia-smi` 或 `torch.cuda.is_available()`）且配置了本地 so-vits 目录 → 本地；否则 → ModelScope 创空间。
- 推荐参数（实测降低沙哑）：本地模式默认 `-eh`（NSF-HiFiGAN 增强）、`--key 3`（原唱为女声时可试 0~3）、`-ns 0.2`；后处理可用 ffmpeg `highpass=f=80,afftdn=nr=10:nf=-45,alimiter`。
- 环境变量见 README：`SXR_SOVITS_DIR`、`SXR_PYTHON`、`SXR_CKPT`、`SXR_STUDIO_URL`。
- 失败时**直接报告错误原因**（无 GPU 且创空间不可用/网络受限等），不要用占位或伪造结果。

## 完成后
告诉用户输出文件路径，并重申"AI 生成、非本人演唱"。
