# 📅 Claude Code 週刊アップデート — Week 17 · April 20–24, 2026

> /ultrareview がリサーチプレビューとして公開、ターミナルに戻った際の自動セッション要約、プラグインでビルド・配布できるカスタムカラーテーマ、そして Claude Code on the web のリデザイン。

## 🚀 主要機能 (4 件)

### /ultrareview `research preview`
現在パブリックリサーチプレビュー中。Ultrareview はクラウド上でバグ探索エージェントの群れをブランチや PR に対して実行し、結果が CLI または Desktop に自動的に届きます。認証やデータマイグレーションなどの重要な変更のマージ前に実行することを推奨します。
🔗 https://code.claude.com/docs/en/ultrareview

### Session recap `CLI`
セッションから離れている間に発生したことを、戻ってきたときに1行の要約で確認できます。複数の Claude セッションを同時に実行しながらフローを維持するのに役立ちます。
🔗 https://code.claude.com/docs/en/interactive-mode#session-recap

### Custom themes `v2.1.118`
`/theme` から名前付きカラーテーマを作成・切り替えたり、`~/.claude/themes/` の JSON ファイルを直接編集したりできます。各テーマはベースプリセットを選択し、必要なトークンのみをオーバーライドします。プラグインもテーマを同梱できます。
🔗 https://code.claude.com/docs/en/terminal-config#create-a-custom-theme

### Claude Code on the web `web`
リデザインされたデスクトップアプリに合わせた claude.ai/code の新しいルック: セッションサイドバー、ドラッグ＆ドロップレイアウト、更新されたルーティンビュー。応答の高速化と信頼性向上のため主要部分が再構築されています。
🔗 https://code.claude.com/docs/en/claude-code-on-the-web

## ✨ その他のアップデート

- **Vim ビジュアルモード**: プロンプト入力で `v` を押すと文字選択、`V` を押すと行選択が使えるようになり、オペレーターとビジュアルフィードバックをサポート
- フックが `type: "mcp_tool"` を使って MCP ツールを直接呼び出せるようになり、プロセスを起動せずに接続済みサーバーへアクセス可能
- `/cost` と `/stats` が `/usage` に統合。旧コマンド名は関連タブを開く入力ショートカットとして引き続き機能
- `/config` での変更 (テーマ、エディタモード、verbose など) が `~/.claude/settings.json` に保存され、他の設定と同じプロジェクト/ローカル/ポリシーの優先順位に従うように
- 外部ビルドで `CLAUDE_CODE_FORK_SUBAGENT=1` を設定することでフォークされたサブエージェントが有効化: フォークは最初から始める代わりに会話コンテキスト全体を継承
- Pro および Max サブスクライバーの Opus 4.6 と Sonnet 4.6 のデフォルト努力レベルが `medium` から `high` に変更
- macOS および Linux のネイティブビルドで `Glob` と `Grep` ツールが組み込みの `bfs` と `ugrep` に置き換えられ、Bash から高速検索が可能に
- `--from-pr` が github.com に加えて GitLab マージリクエスト、Bitbucket プルリクエスト、GitHub Enterprise PR の URL を受け付けるように
- Auto モード: `autoMode.allow`、`soft_deny`、または `environment` に `"$defaults"` を含めると、組み込みリストを置き換える代わりにカスタムルールを追加可能
- 新しい `claude plugin tag` コマンドでバージョン検証付きのプラグインリリース git タグを作成可能
- Opus 4.7 セッションがモデルのネイティブ 1M コンテキストウィンドウに対して計算されるようになり、`/context` パーセンテージの誤表示と早期自動コンパクションが修正
- 大規模セッションの `/resume` が最大 67% 高速化し、古い大規模セッションを再読み込みする前に要約を提案するように

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w17
