# 发布到 AIPMAndy GitHub：一步一验收

本项目遵循**独立公开仓库**原则，仓库名为 `AIPMAndy/wechat-account-launch-handbook`，不是其它公众号 Skill 仓库的子目录。

## 一次性前提

你必须有 AIPMAndy 账号的 GitHub 管理权限，并在自己的电脑安装 Git、GitHub CLI（`gh`），执行 `gh auth login` 完成账号授权。不要在聊天里发送 Token、验证码或 GitHub 密码。

## 直接发布

解压本项目完整 ZIP 后，在终端进入项目根目录，运行：

```bash
bash scripts/publish.sh
```

脚本会先核对当前登录用户为 `AIPMAndy`，校验来源、重建可部署网站和 PDF，通过结构/文字/JS 校验后创建或使用**指定的独立仓库**并提交文件，不会推送到未知 remote。

## 开启 GitHub Pages

打开 <https://github.com/AIPMAndy/wechat-account-launch-handbook/settings/pages> ，在 Build and deployment 的 Source 选 **GitHub Actions**。然后进入 Actions 查看 `Build, audit and deploy handbook to GitHub Pages` 成功与否；如没有自动触发，可手动运行该工作流。只有 **Actions 成功后** 才能把 <https://aipmandy.github.io/wechat-account-launch-handbook/> 当作线上地址。

## 交付验收

- 仓库公开可见，`main` 包含 24 章、模板、Website、PDF、源脚本、许可证。
- Actions 构建和 PDF 校验成功。
- 网站首页和至少 3 个章节可访问，查章节搜索和 30 天打卡。
- PDF 可公开下载、中文可复制、目录链接可用。
- 微信 `AIPMAndy`、个人官网 `metaver.vip`、公司官网 `a6no1.cn` 正确。

**注意**：如果 GitHub 权限或 Pages 开关尚不可用，绝不能把「本地打包」标为「已上线」。
