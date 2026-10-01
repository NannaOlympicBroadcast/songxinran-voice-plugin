# songxinran-voice（Claude Cowork / Claude Code 插件）

用**宋昕冉 AI 音色**（so-vits-svc 4.1，vec768l12 + rmvpe，G_9600）转换人声。

> ⚠️ 粉丝自制、非官方、非商用；模型未获本人授权；输出是 AI 合成声音，分享时必须标注「AI 生成」，不得冒充本人、欺诈、骚扰或商用。

## 关于宋昕冉

宋昕冉（SongXinRan，昵称「冉冉」，缩写 SXR）是 SNH48 GROUP 的成员，隶属 SNH48，现属 Team HII（原 Team X），SNH48 四期生；1997 年 7 月 8 日出生，籍贯山东济南，巨蟹座，身高 166 cm，血型 O；特长为唱歌、拉丁舞、二胡，爱好运动、旅游、看电影；2015 年 1 月 31 日加入，所属公司为上海丝芭文化传媒集团有限公司；口袋 48 / 微博：SNH48-宋昕冉。[来源：SNH48 官网名册 + data.gnz.hk 成员数据，经 pocket48-cli `member info 宋昕冉` 于 2026-10-01 读取；名册数据可能随时间变化，请以官方为准]

> 本插件与宋昕冉本人、SNH48 GROUP 及其运营公司**没有任何关联**，未获其授权或背书；这是粉丝出于喜爱制作的 AI 音色模型。

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
