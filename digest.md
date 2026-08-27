# 📅 Claude Code 週刊アップデート — Week 34 · August 17–21, 2026

> /design スキルで編集可能な UI アートボードを下書きし、Concise 出力スタイルを設定、スマートフォンからマシンの Claude Code セッションを開始できるようになりました。

## 🚀 主要機能 (3 件)

### /design `research preview`
/design スキルが、アーティファクトを基盤として Claude Design のアートボードワークフローを CLI および Claude Code Desktop に導入します。簡単な説明を入力するだけで、Claude が編集可能なアートボードのキャンバスを公開します。気に入ったものを選んで調整し、Claude に実装を依頼できます。Pro・Max・Team・Enterprise プランで利用可能。v2.1.233 以降が必要です。
🔗 https://code.claude.com/en/artifacts#availability

### Concise output style `v2.1.237`
Concise は新しい組み込み出力スタイルです。Claude は結果を先に示し、前置きや説明の羅列を省きながらも、Default スタイルと同じ丁寧さで作業を行います。詳しい説明を求めれば完全な回答が得られます。エラーレポート、セキュリティ警告、破壊的な操作の確認はこれまで通り完全な内容を保持します。
🔗 https://code.claude.com/en/output-styles#built-in-output-styles

### Start a session on your machine from your phone `mobile`
`claude remote-control` を実行しているマシンが、Claude アプリの「Code」タブの上部にデバイスカードとして表示されるようになりました。Remote Control も research preview から正式リリースされました。
🔗 https://code.claude.com/en/remote-control#start-a-remote-control-session

## ✨ その他のアップデート

- claude.ai の使用量制限がリセットされると、Claude Code が自動的にセッションを再開するようになりました。`/config` の「使用量制限到達時に自動継続」からオフにできます
- オプションの `spellcheck` 設定を有効にすると、インストール済みの `aspell`・`hunspell`・`ispell` を使って、入力中のプロンプトでスペルミスに下線が引かれるようになりました
- `glab auth login` で `glab` CLI 認証済みの場合、GitLab マージリクエストが開いているブランチのフッターに `MR !N` バッジが表示され、ドラフト・オープン・マージ可能の状態が色で示されます
- スマートフォンや claude.ai/code から努力レベルを変更すると、マシン上のセッションに即座に反映されます。Desktop や VS Code がホストする Remote Control セッションも、接続デバイスに現在の権限モードを表示するようになりました
- Claude が作業中に `/permissions` を開いたり `/add-dir <パス>` を実行したりできるようになりました。権限ルールの変更は現在のターンの残りに即時適用されます
- `/goal` をバックグラウンドタスクが待機させている場合、Claude は無期限に待つのではなく、30 分後にチェックインし、セッションがアイドル状態の間は間隔を延ばしながらチェックを続けます。`CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` でオプトアウト可能
- 自分のプロンプトがトランスクリプトでマークダウンとして表示されるようになりました。コードブロックのシンタックスハイライト、インラインコード、リストなど、Claude の返答と同様に表示されます
- 新しい `ANTHROPIC_DEFAULT_MODEL` 環境変数で、新しいセッションが開始するモデルを設定できます。`/model` で選んだモデルは引き続き優先され、再起動後も保持されます
- `SendMessage` の `notify_when_idle` 入力を使うと、同じマシン上の別の Claude Code セッションがアイドル状態になった時に通知を受け取れます
- `keybindingFlavor` を `"readline"` に設定すると、プロンプトでの `Ctrl+W` が `/` などの句読点で止まらず、Bash と同様に前の空白まで削除するようになります
- ネイティブ Windows でも、Claude Code セッション同士が `SendMessage` でメッセージを送り合ったり、`ListAgents` でお互いを見つけたりできるようになりました（macOS・Linux と同様）
- セルフホストランナーが `--defer-shutdown-max-min` を受け入れるようになり、SIGTERM 後も指定した分数の間、アタッチ中のセッションへのサービスを継続できます
- セルフホストランナーが `--proxy-authorization-command` または `--proxy-authorization-file` を受け入れるようになり、認証が必要な egress プロキシに新しい `Proxy-Authorization` ヘッダーを提供できます

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w34
