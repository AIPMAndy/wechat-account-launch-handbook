# 参与贡献｜Contributing

欢迎帮助完善《微信公众号从 0 到 1 起号与商业化 · 保姆级开源攻略》。本项目优先接受可复现、可核验、能够让零基础读者独立完成任务的改进。

## 如何提出反馈

1. 在 GitHub Issues 中说明具体章节或模板、问题现象与复现步骤。
2. 如涉及微信公众号规则，请附微信官方来源、发布日期以及适用条件；第三方经验应明确标注为“作者自述/待验证”。
3. 如涉及站点错误，请说明浏览器、设备宽度、URL、预期结果与实际结果，避免提交个人隐私、商业客户数据或 API 密钥。

## 提交 Pull Request

1. Fork 本仓库，创建一个独立分支；小步提交，一次解决一个主要问题。
2. 内容正文优先修改 `content/chapters/`，模板修改 `templates/`；网站和 PDF 均由脚本构建，避免只改生成结果。
3. 本地运行：
   ```bash
   python -m pip install -r requirements.txt
   python scripts/build.py
   python scripts/verify.py
   ```
4. 在 PR 中写清变更范围、使用的依据、构建结果与截图（界面变更时）。
5. 不提交未经授权的客户素材，不复制第三方完整文章，不使用虚构收入数据、成功率、平台规则或流量承诺。

## 发布质量门槛

- [ ] 新手可以照步骤操作，不需要猜测前提
- [ ] 外部链接能打开；政策/门槛类陈述标注官方出处和核验日期
- [ ] AI 生成的示例标注为教学模拟，不伪装成亲历案例
- [ ] 移动端阅读正常，所有工具输出解释适用范围和局限
- [ ] `python scripts/verify.py` 通过
- [ ] GitHub Pages 真正完成 `Deploy to GitHub Pages` 步骤，而非仅构建成功

## 授权

网站及构建代码遵循仓库 MIT License；原创教程与模板依照 [CONTENT_LICENSE.md](CONTENT_LICENSE.md) 的 CC BY 4.0；第三方内容仍归权利人所有。

作者：AI 酋长 Andy · GitHub [AIPMAndy](https://github.com/AIPMAndy) · [个人官网](https://metaver.vip/) · [星觉科技](https://www.a6no1.cn/) · 微信 `AIPMAndy`。
