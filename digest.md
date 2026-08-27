# 📅 Claude Code 週刊アップデート — Week 34 · August 17–21, 2026

> /design スキルで編集可能な UI アートボードを下書きし、Concise（簡潔）出力スタイルを設定。スマートフォンからマシン上の Claude Code セッションを開始できるようになりました。

## 🚀 主要機能 (3 件)

### /design `research preview`
/design スキルにより、Claude Design のアートボードワークフローが CLI と Claude Code Desktop に導入されました。アーティファクト基盤で構築されており、簡単な説明を入力するだけで Claude が編集可能なアートボードのキャンバスを公開します。好みのアートボードを選んで調整し、そのまま Claude に実装させることができます。Pro・Max・Team・Enterprise プランで利用可能。v2.1.233 以降が必要です。
🔗 https://code.claude.com/en/artifacts#availability

### Concise output style `v2.1.237`
Concise（簡潔）は新しい組み込み出力スタイルです。Claude は前置きや状況説明を省いて結果を先に提示しますが、作業自体はデフォルトスタイルと同じ精度で行います。説明や詳細を求めると、フルで回答します。エラーレポート・セキュリティ警告・破壊的操作の確認には、引き続き完全な内容が表示されます。
🔗 https://code.claude.com/en/output-styles#built-in-output-styles

### スマートフォンからマシン上のセッションを開始 `mobile`
`claude remote-control` を実行中のマシンが、Claude アプリの「Code」タブ最上部にデバイスカードとして表示されるようになりました。Remote Control はリサーチプレビューから正式リリースされました。
🔗 https://code.claude.com/en/remote-control#start-a-remote-control-session

## ✨ その他のアップデート

- claude.ai の使用量制限がリセットされると、Claude Code がセッションを自動的に再開するようになりました。`/config` の「使用量制限時に自動継続」行からオフにできます。
- オプションの `spellcheck` 設定を有効にすると、インストール済みの `aspell`・`hunspell`・`ispell` を使ってプロンプト入力中にスペルミスに下線が表示されます。
- `glab auth login` で認証済みの `glab` CLI がある場合、オープン中の GitLab マージリクエストのブランチではフッターに `MR !N` バッジが表示され、ドラフト・オープン・マージ可能の状態に応じて色が変わります。
- スマートフォンや claude.ai/code からエフォートレベルを変更すると、マシン上のセッションに即時反映されます。Desktop や VS Code がホストする Remote Control セッションも、接続デバイスに現在の権限モードを表示するようになりました。
- Claude が作業中でも `/permissions` を開いたり `/add-dir <パス>` を実行したりできるようになりました。権限ルールの変更は現在のターンの残り部分に適用されます。
- バックグラウンドタスクが `/goal` を待機させている場合、Claude は無期限に待つのではなく 30 分後にチェックインし、セッションがアイドル状態になると間隔を延ばしながらチェックインを継続します。`CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` でオプトアウト可能です。
- 自分のプロンプトがトランスクリプトでマークダウンレンダリングされるようになりました。コードブロックのハイライト・インラインコード・リストがレスポンスと同様に表示されます。
- 新しい環境変数 `ANTHROPIC_DEFAULT_MODEL` で新規セッションの開始モデルを設定できます。`/model` で選択したモデルは引き続き優先され、再起動後も維持されます。
- `SendMessage` の `notify_when_idle` 入力を使って、同じマシン上の別の Claude Code セッションがアイドル状態になったときに通知を受け取れるようになりました。
- `keybindingFlavor` を `"readline"` に設定すると、プロンプト入力での `Ctrl+W` が `/` などの句読点ではなく前の空白まで削除するようになります（Bash と同じ動作）。
- Windows ネイティブ環境でも、macOS・Linux と同様に `SendMessage` でセッション間メッセージ送信、`ListAgents` でセッション検索ができるようになりました。
- セルフホスト型ランナーが `--defer-shutdown-max-min` を受け付けるようになり、SIGTERM 後も指定した分数の間アタッチ中のセッションにサービスを継続できます。
- セルフホスト型ランナーが `--proxy-authorization-command` または `--proxy-authorization-file` を受け付けるようになり、認証を必要とするエグレスプロキシ向けに新鮮な `Proxy-Authorization` ヘッダーを供給できます。

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w34
