# 📅 Claude Code 週刊アップデート — Week 32 · August 3–7, 2026

> Claude Code セッション同士がメッセージを送り合えるようになり、セルフホスト環境が組織のインフラ上でクラウドセッションを実行でき、auto mode がデフォルトの権限モードになります。

## 🚀 主要機能 (3 件)

### Cross-session messaging `v2.1.224`
Claude Code のセッション同士がメッセージを送り合えるようになりました。Claude は `ListAgents` ツールで他のセッションを検出し、`SendMessage` で送信します。あなたが依頼した場合だけでなく、あるセッションでの変更が別のセッションの作業に影響する場合などにも自動的に送信します。メッセージは Claude が他のセッション向けに書いたテキストであり、会話履歴やファイルは共有されません。macOS と Linux で利用可能。v2.1.224 以降が必要です。
🔗 https://code.claude.com/docs/en/cross-session-messaging#message-another-session

### Self-hosted environments `v2.1.224`
セルフホスト環境では、Claude Code クラウドセッションを組織独自のインフラ上で実行できます。Team および Enterprise プランでパブリックベータとして提供中。`claude self-hosted-runner` をマシンやコンテナで実行することでランナーとして登録できます。ユーザーが claude.ai、モバイル/デスクトップアプリ、または `claude --cloud` からセッションを開始する際にあなたの環境を選択すると、そのセッションは組織のネットワーク内部で動作し、内部サービスにアクセスできます。まず管理者設定で **Allow self-hosted environments** を有効化する必要があります。
🔗 https://code.claude.com/docs/en/self-hosted-environments-quickstart#set-up-an-environment-and-runner

### Auto mode becomes the default `CLI`
8月14日より、Pro・Max・Team プランの新規セッションでは auto mode がデフォルトの権限モードになります。自分でデフォルトモードを設定している場合は、一度切り替えプロンプトを承認しない限りそのままです。組織が管理するデフォルト設定も変更されません。モードはいつでも切り替えできます。これらのプランではすでに、auto mode が行う分類器の呼び出しが使用量制限にカウントされなくなっています。
🔗 https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode

## ✨ その他のアップデート

- VS Code 拡張機能に **Focus ビュー** が追加されました。ターンごとにツールのアクティビティを 1 行の折りたたみ行の後ろに隠せます。コマンドメニューまたは `Ctrl+Alt+F`（Mac では `Ctrl+Option+F`）で切り替え可能です。
- サンドボックスの認証情報ファイルが Linux および WSL2 で `mode: "mask"` に対応。サンドボックス内のコマンドはダミーのコピーを読む一方、サンドボックスプロキシが egress 時に実際の値に置き換えます。`extract`、JWT 対応 `decode`、AWS SigV4 再署名オプションも追加されました。
- マーケットプレイスが新しい `archive` ソースを使ってプラグインを zip アーカイブとして配布できるようになりました。オプションの SHA-256 ピンを使って HTTPS 経由でダウンロードするため、git や npm なしでインストールできます。
- `/review` が `/code-review` のエイリアスになりました。また `/code-review` を effort レベルなしで実行すると前回使ったレベルを再利用します。
- `/fork` でコピーしたセッションが、元のセッションのチェックアウトではなく専用の worktree でコード変更を行うようになりました。
- `/plugin` からインストールしたプラグインは、安全な場合に現在のセッションで即座に有効化されます。インストールサマリーに「Plugin is now active.」またはリロードが必要な場合は `/reload-plugins` を実行するよう表示されます。
- worktree でコードを変更したバックグラウンドセッションが、タスクに必要な場合のみコミット・プッシュしてドラフト PR を開くようになりました。また `CLAUDE.md` の git 指示に従って動作します。
- 1 セッションあたり 200 サブエージェントの上限が撤廃されました。長時間実行セッションでも新しいサブエージェントが拒否されなくなります（同時実行数と深さの制限は引き続き適用）。
- リポジトリのチェックイン設定から Remote Control の自動接続を有効化できなくなりました。ユーザーまたは管理設定で `remoteControlAtStartup` を設定する必要があります（プロジェクト/ローカル設定での無効化は引き続き可能）。
- Worktree の隔離が強化され、ファイル編集だけでなく、メインチェックアウトへ到達する Bash コマンドや git リダイレクトもブロックされます。セッションのサブエージェントにも適用されます。
- Bash コマンドが権限チェックの一部を隠せなくなりました。また、タブや不可視の Unicode パディングを使って承認ダイアログでコマンドの一部を隠すことも不可能になりました。
- PreToolUse 自動許可フックが、要約やコンパクションなどの Claude Code 内部サイドタスクでのツール制限を回避できなくなりました。
- Ultraplan リサーチプレビューが削除されました（`/ultraplan` コマンドおよび `ultraplan` キーワードも削除）。代わりにプランモードまたは Claude Code on the web をご利用ください。

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w32
