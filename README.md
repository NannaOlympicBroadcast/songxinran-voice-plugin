# songxinran-voice（Claude Cowork / Claude Code 插件）

用**宋昕冉 AI 音色**（so-vits-svc 4.1，vec768l12 + rmvpe，G_9600）转换人声。

> ⚠️ 粉丝自制、非官方、非商用；模型未获本人授权；输出是 AI 合成声音，分享时必须标注「AI 生成」，不得冒充本人、欺诈、骚扰或商用。

## 后端
| 条件 | 后端 |
|---|---|
| 检测到 NVIDIA GPU 且设置了 `SXR_SOVITS_DIR` | **本地 so-vits-svc**（默认） |
| 否则 | **ModelScope 创空间** `yanyan0406/snh48songxinran-sovits-demo`（免费 CPU，较慢） |

## 配置（环境变量，仓库内不含任何令牌）
- `SXR_SOVITS_DIR`：本地 so-vits-svc 目录（含 `inference_main.py`、`logs/44k/G_9600.pth`、`pretrain/`）
- `SXR_PYTHON`：运行 so-vits 的 python（默认当前解释器）
- `SXR_CKPT` / `SXR_CONFIG`：默认 `logs/44k/G_9600.pth`、`logs/44k/config.json`
- `SXR_STUDIO_URL`：创空间直连地址（默认由 `SXR_STUDIO_ID` 推导，请以创空间页面实际地址为准）
- 权重：<https://www.modelscope.cn/models/yanyan0406/snh48songxinran-sovits>

## 使用
```
python scripts/svc.py --input vocals.wav --out out_AI.wav --key 0 --backend auto
```
失败时脚本直接报错，不做 mock/占位。

## 许可
代码 MIT；模型与音色另见模型仓库说明（非商用）。
