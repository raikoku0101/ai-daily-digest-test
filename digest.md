# 📅 Claude Code 週刊アップデート — Week 22 · May 25–29, 2026

> Claude Opus 4.8 で Claude Code を使い、ダイナミックワークフローで大規模タスクを自動化。security-guidance プラグインでセキュリティ問題を検出し、Opus 4.8 での高速モードをより低コストで利用できます。

## 🚀 主要機能 (4 件)

### Claude Opus 4.8 `new model`
Opus 4.8 が Max・Team Premium・Enterprise 従量課金・Anthropic API のデフォルトモデルになりました。デフォルトで高精度動作 (high effort) に設定されており、難しいタスクには `/effort xhigh` を使用してください。v2.1.154 以降が必要です。
🔗 https://code.claude.com/docs/en/model-config#available-models

### Dynamic workflows `research preview`
ワークフローとは、Claude がタスクに合わせて作成し、バックグラウンドで多数のサブエージェントを使って実行するオーケストレーションスクリプトです。コードベース全体の監査・大規模マイグレーション・クロスチェックが必要なリサーチなど、1 つの会話で調整しきれないタスクに活用してください。`/workflows` でスクリプトの実行状況を管理できます。
🔗 https://code.claude.com/docs/en/workflows

### Security guidance plugin `plugin`
security-guidance プラグインは、Claude によるコード変更の脆弱性を検出し、同セッション内で修正まで行います。編集のたびに高速パターンチェックを実行し、ターン終了時にモデルレビュー、コミット・プッシュ時にはより深いエージェントレビューを実施します。プロジェクト固有のルールは `.claude/claude-security-guidance.md` に追記できます。
🔗 https://code.claude.com/docs/en/security-guidance

### Fast mode on Opus 4.8 `research preview`
高速モード (Fast mode) のデフォルトが Opus 4.8 になりました。料金は MTok あたり $10/$50 で、標準レートの 2 倍ですが約 2.5 倍の速度を実現します。Opus 4.7 と 4.6 は $30/$150 のまま据え置きです。Opus 4.6 の高速モードは非推奨となりました。
🔗 https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff

## ✨ その他のアップデート

- `claude agents` で、シェルコマンドの先頭に `!` を付けるとバックグラウンドジョブとして実行でき、アタッチ・デタッチが可能。`claude --bg --exec 'pytest -x'` でも利用可能
- `.claude/skills` ディレクトリ内のプラグインが自動的に読み込まれるようになり、マーケットプレイスが不要に。`claude plugin init <name>` で新規プラグインのスキャフォールドも可能
- 新コマンド `/reload-skills` でスキルディレクトリを再スキャン (再起動不要)。`SessionStart` フックが `reloadSkills: true` を返すと、インストールしたスキルを同セッション内で即利用可能
- スキルとコマンドのフロントマターで `disallowed-tools` を設定し、スキルがアクティブな間は特定ツールをモデルから除外可能
- 新 `MessageDisplay` フックイベントにより、アシスタントのメッセージテキストを表示時に変換・非表示にできる
- プライマリモデルが見つからない場合、セッション全体でエラーになる代わりに設定済みの `--fallback-model` に自動切り替えするよう改善
- プラグインが `plugin.json` またはマーケットプレイスエントリで `defaultEnabled: false` を宣言すると、有効化するまでインストールされても起動しない
- Vim モード: NORMAL モードで `/` を押すと逆順ヒストリ検索が開き、Bash・Zsh の vi-mode と同様の操作が可能
- テレメトリ無効時および Bedrock・Vertex・Foundry 環境でも、ストリーミングツール実行が常時有効化
- エージェントビューを開く `←←` ショートカットが、Bedrock・Vertex・Foundry およびテレメトリ無効時でも動作するように
- Claude in Chrome: `/chrome` → 「ブラウザを選択…」または複数ブラウザ接続時のチャット内操作で、使用するブラウザを選択可能
- `claude mcp list` と `claude mcp get` が、出力パイプ時に `.mcp.json` サーバーを自動承認・接続するのではなく「承認待ち」として表示するよう変更

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w22
