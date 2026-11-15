# 微信公众号从 0 到 1 起号与商业化 · 保姆级开源攻略

这是一份开源攻略：24 章正文、30 天 SOP、可编辑模板，以及由同一组 Markdown 生成的 PDF。面向零基础公众号作者、AI 垂直号、个人 IP 与企业内容团队。

**核心目标：** 帮一个完全没有运营经验的人，从注册、定位、验证用户需求，走到发布可核实的原创内容、复盘、获得匹配的商业询盘，并在发生合作时完成合规交付与回款。**不承诺 30 天必爆、100 粉收入、月入十万、算法捷径。**

本地快速开始（Python 3.11+）：

```bash
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/verify.py
python -m http.server 8000 -d docs
# 打开 http://127.0.0.1:8000/
```

## 阅读入口

- **GitHub Pages**：https://aipmandy.github.io/wechat-account-launch-handbook/  
  2026-11-15 对该地址执行 curl，HTTP 状态码为 200。同一天 GitHub 仓库对象的 `has_pages` 为 true。`.github/workflows/pages.yml` 在推送到 `main` 时运行 `scripts/build.py` 与 `scripts/verify.py`，并在 `GET /repos/{owner}/{repo}/pages` 返回 200 时把 `docs/` 部署到 GitHub Pages。本次没有打开仓库 Settings 页面，因此不描述 Source 下拉框当前选中的项。
- **本地网站**：打开 `docs/index.html`，或按上面的命令重建后访问 http://127.0.0.1:8000/
- **精美 PDF**：`docs/wechat-account-launch-handbook.pdf`（由同一组 Markdown 内容生成）
- **所有正文**：[`content/chapters/`](content/chapters/)
- **30 天表格**：[`templates/30-day-sop.csv`](templates/30-day-sop.csv)
- **商单与合同对接模板**：[`templates/brand-brief.md`](templates/brand-brief.md)、[`templates/media-kit.md`](templates/media-kit.md)、[`templates/commercial-pipeline.csv`](templates/commercial-pipeline.csv)

## 从哪里开始

1. 读 [`00-start-here.md`](content/chapters/00-start-here.md)，先选择流量主、品牌商单或专业服务的**主要模型**。
2. 依次完成账号注册、定位、对标、问题库、选题、实测、排版、发布和冷启动。
3. 用 30 天计划检验每一步是否有证据，遇到低阅读先看[`22-failure-diagnostics.md`](content/chapters/22-failure-diagnostics.md)。
4. 想接品牌合作，重点阅读 13–19 章，拿走媒体包/Brief/报价/验收/回款模板。
5. 每篇文稿都必须有人类主导的实测、判断和最终审核；**不提供自动批量代写/代发教程**。

## 常见问题

### 会保证爆款或收入吗？

不会。本攻略不承诺 30 天必爆、100 粉收入、月入十万或算法捷径。文中的个案数据不是收益保证。

### 能用来批量代写或代发吗？

不能。每篇文稿都必须有人类主导的实测、判断和最终审核。本仓库不提供自动批量代写或代发教程。

### 线上 Pages 和本地预览有什么差别？

线上地址在 2026-11-15 返回 HTTP 200，仓库 `has_pages` 为 true。本地站点来自 `docs/`：用 `python scripts/build.py` 从 Markdown 重建，用 `python scripts/verify.py` 做结构检查。`.github/workflows/pages.yml` 只在 Pages 接口返回 200 时部署 `docs/`。只改本地文件不会自动更新已经部署的页面。

## 两篇指定研究资料，分工明确

- [蜗牛 King《公众号新号从 0 到 1 起号保姆级全阶教程》](https://x.com/isnail/status/2060928267046060445)：吸收「账号资料统一、定位、对标、内容结构、运营复盘」；对「复制标签截流、早 7 点固定流量池、绝不分享朋友圈、洗稿或截图规避版权」等缺乏依据/不合规建议不采纳。
- [西堂《AI 公众号稳定月入变现 10 万+，从选题到接商单的万字实操教程》](https://x.com/xitang_ai/status/2121207382630117537)：吸收「人群→问题→实际结果→品牌匹配、真实实测、商务媒体包、报价与授权、交付/回款、团队 SOP」；作者收入与阅读均为其公开自述，非独立审计，**不代表零基础结果**。

详细来源等级和核验时间见 [`23-evidence-and-sources.md`](content/chapters/23-evidence-and-sources.md)。2026 规则重点看 [`20-2026-rules.md`](content/chapters/20-2026-rules.md)。

## 与其他开源工具的边界

| 仓库 | 做什么 | 本项目是否重做 |
|---|---|---|
| [wechat-explosive-article-skill](https://github.com/AIPMAndy/wechat-explosive-article-skill) | 文章创作与对抗审核 | 不重做；链接集成 |
| [MDskill-Web](https://github.com/AIPMAndy/MDskill-Web) | Markdown 排版与导出 | 不重做；提供操作教程 |
| **本项目** | 起号、需求验证、内容生产工作流、商单、履约、数据与 30 天执行 | **新独立范畴** |

## 网站可用工具

- 路线选择器：为流量主 / 品牌商单 / 个人 IP 推荐优先阅读章节
- 选题评分器：痛点、需求、证据、差异化、商业匹配；无证据直接暂停
- 商单贡献利润模拟：明确**是假设情景**、不是收入预测
- 30 天打卡：浏览器本地记录，不上传服务器，可手动导出 JSON
- 文章搜索：按标题和全文索引定位章节
- 微信号复制：只有用户点击并成功复制后才提示

## 从 Markdown 一键生成网站和 PDF

要求：Python 3.11+。命令与文首「本地快速开始」相同：`python -m pip install -r requirements.txt`、`python scripts/build.py`、`python scripts/verify.py`。需要本机预览时再运行 `python -m http.server 8000 -d docs`。

GitHub Pages 工作流是 `.github/workflows/pages.yml`。它在 `GET /repos/{owner}/{repo}/pages` 返回 200 时，用 Actions 把 `docs/` 部署出去。本地文件或压缩包本身不是线上部署结果。生成的 PDF 与 24 章 Markdown 同源。本次没有打开 Settings 页面，不记录 Source 下拉框的当前选项。

## 授权与诚信

- 工具、构建脚本、网站源码：MIT License（[`LICENSE`](LICENSE)）。
- 本项目**原创教程文字与模板**：CC BY 4.0（[`CONTENT_LICENSE.md`](CONTENT_LICENSE.md)），请署名并注明修改。
- 第三方 X 原帖、品牌标志、平台截图及外部网页内容**不包含在开源授权里**，版权归原作者或相应权利方。本仓库只用必要的短句转述、链接与方法分析，不重发完整文章。
- 不提供刷量、洗稿、自动代写代发，品牌合作与流量主资格以平台最新规定为准。

## 关于作者与服务

- **AI酋长Andy**（流量 AI 联合创始人、星觉 AI 创始人）· 星觉科技 · 北京 · 更新：**2026-11-15**
- 微信：**`AIPMAndy`**（备注「公众号」）
- 个人官网：[metaver.vip](https://metaver.vip/) / [服务介绍](https://metaver.vip/services)
- 公司官网：[星觉科技 a6no1.cn](https://www.a6no1.cn/)
- GitHub：[AIPMAndy](https://github.com/AIPMAndy) · 公众号搜索：**AI 酋长 Andy**

**这份教程免费、无需私信或关注才能阅读；需要咨询、陪跑或企业合作可自愿联系。**
