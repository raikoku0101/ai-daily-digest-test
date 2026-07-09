# 📅 Claude Code 週刊アップデート — Week 26 · June 22–26, 2026

> シェルから `claude mcp login` で MCP サーバーを認証し、`!` プレフィックスでシェルモードのコマンド出力に対して応答を取得し、`/rewind` で `/clear` 実行前の会話を再開できます。

## 🚀 主要機能 (2 件)

### Authenticate MCP servers from the CLI `v2.1.186`
新しい `claude mcp login <name>` および `claude mcp logout <name>` コマンドにより、インタラクティブな `/mcp` メニューを開くことなく、シェルから MCP サーバーを認証できます。`claude mcp login` はサーバーの OAuth フローを直接実行し、`claude mcp logout` は保存された認証情報をクリアします。
🔗 https://code.claude.com/en/mcp#authenticate-from-the-command-line

### Shell mode responds to command output `v2.1.186`
`!` プレフィックスで実行したコマンドは、その出力がトランスクリプトに記録されると Claude から自動的に応答が返されます。例えば `! npm test` を実行するとテスト失敗の説明が自動で返されるため、追加のプロンプトが不要です。応答コストは通常のプロンプトと同じです。以前の動作（出力をコンテキストに追加するが応答なし）を維持したい場合は、`settings.json` で `respondToBashCommands` を `false` に設定してください。
🔗 https://code.claude.com/en/interactive-mode#shell-mode-with-prefix

## ✨ その他のアップデート

- `/rewind` で `/clear` 実行前の会話を再開できるようになりました
- 新しい `sandbox.credentials` 設定により、サンドボックス化されたコマンドが認証情報ファイルや秘密の環境変数を読み取れないようにブロックできます
- 組織が設定したモデル制限が、モデルピッカー・`--model`・`/model`・`ANTHROPIC_MODEL` に適用されるようになりました。制限されたモデルを選択すると「組織の設定により制限されています」というメッセージが表示されます
- 新しい `autoMode.classifyAllShell` 設定で、すべての Bash および PowerShell コマンドを自動モードの分類器を通じてルーティングできます。また、拒否理由がトランスクリプト・拒否トースト・`/permissions` に表示されるようになりました
- 新しい `claude_code.assistant_response` OpenTelemetry ログイベントにモデルの応答テキストが含まれます。既にプロンプトコンテンツをログに記録しているデプロイメントはアップグレード後に自動受信されるため、プロンプトのみ保持したい場合は `OTEL_LOG_ASSISTANT_RESPONSES=0` を設定してください
- バックグラウンドのサブエージェントがパーミッションプロンプトを自動拒否する代わりにメインセッションに表示するようになりました。ダイアログにはどのエージェントが要求しているかが表示され、Esc でそのツールのみを拒否できます
- `/install-github-app` で GitHub App のみをインストールし、Actions ワークフローやシークレット手順をスキップできるようになりました
- サンドボックスのネットワーク権限ダイアログで許可したホストが、毎回再確認されることなくセッション中ずっと記憶されるようになりました
- ストリーミングレスポンスの CPU 使用量が約 37% 削減され、ターミナル出力キャッシュによる長時間セッションのメモリ増加が軽減されました
- `/review <pr>` が `/code-review medium` と同じレビューエンジンを使用するようになりました
- Bash モードの `!` コマンドでライブのファイルパス自動補完が使えるようになりました

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w26
