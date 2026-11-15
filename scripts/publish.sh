#!/usr/bin/env bash
# Explicit opt-in release utility. Does not run automatically.
# Run from an extracted project folder after installing/authenticating GitHub CLI.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
REPO="AIPMAndy/wechat-account-launch-handbook"
command -v gh >/dev/null || { echo '需要安装 GitHub CLI（gh）并执行 gh auth login。'; exit 1; }
command -v git >/dev/null || { echo '需要安装 git。'; exit 1; }
LOGIN="$(gh api user --jq '.login')"
if [[ "$LOGIN" != 'AIPMAndy' ]]; then
  echo "当前 GitHub 账号为 ${LOGIN}，不是 AIPMAndy。已中止，避免推送到错误账号。" >&2
  exit 1
fi
if [[ ! -d .git ]]; then git init -b main; fi
# Fail instead of overwriting an unrelated remote.
if git remote get-url origin >/dev/null 2>&1; then
  REMOTE="$(git remote get-url origin)"
  if [[ "$REMOTE" != *"AIPMAndy/wechat-account-launch-handbook"* ]]; then
    echo "origin 指向 ${REMOTE}，不是目标仓库。已中止。" >&2
    exit 1
  fi
fi
# Important: the exact-source reproducibility gate is local and does not publish automatically.
python scripts/build.py
python scripts/verify.py
if ! gh repo view "$REPO" >/dev/null 2>&1; then
  echo "创建公开且独立的 GitHub 仓库：$REPO"
  gh repo create "$REPO" --public --description '公众号从0到1起号与商单商业化：24章实操、30天SOP、开源网站与PDF' --source . --remote origin
elif ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "https://github.com/${REPO}.git"
fi
git add README.md CHANGELOG.md CONTENT_LICENSE.md LICENSE requirements.txt content docs examples prompts research scripts templates .github
if ! git diff --cached --quiet; then
  git commit -m 'feat: publish WeChat account launch and sponsorship handbook'
fi
git push -u origin main
echo "已推送到 https://github.com/${REPO}"
echo '请在 GitHub 仓库 Settings → Pages → Source 中选择 GitHub Actions，确认 Pages 运行成功。'
