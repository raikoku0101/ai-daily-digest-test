# 📅 Claude Code 週刊アップデート — Week 22 · May 25–29, 2026

> Claude Opus 4.8 で Claude Code を実行し、ダイナミックワークフローで大規模タスクを調整し、security-guidance プラグインでセキュリティ問題を検出し、Opus 4.8 のファストモードをより低価格でご利用ください。

## 🚀 主要機能 (4 件)

### Claude Opus 4.8 `new model`
Opus 4.8 が Max・Team Premium・Enterprise 従量課金・Anthropic API のデフォルトモデルになりました。デフォルトで高エフォートで動作し、難しいタスクには `/effort xhigh` を使用してください。v2.1.154 以降が必要です。
🔗 https://code.claude.com/en/model-config#available-models

### Dynamic workflows `research preview`
ワークフローは、Claude がタスクのために作成し、バックグラウンドで多数のサブエージェントにまたがって実行するオーケストレーションスクリプトです。コードベース全体の監査、大規模なマイグレーション、相互確認が必要なリサーチクエスチョンなど、1 つの会話で調整しきれないタスクに活用してください。`/workflows` で実行を管理できます。
🔗 https://code.claude.com/en/workflows

### Security guidance plugin `plugin`
security-guidance プラグインは、Claude のコード変更を脆弱性についてレビューし、同一セッション内で修正します。各編集時に高速なパターンチェック、各ターン終了時にモデルレビュー、コミットまたはプッシュ時により深いエージェントレビューを実行します。プロジェクトルールは `.claude/claude-security-guidance.md` に追加できます。
🔗 https://code.claude.com/en/security-guidance

### Fast mode on Opus 4.8 `research preview`
ファストモードが Opus 4.8 をデフォルトとして $10/$50 per MTok で利用可能に。通常料金の 2 倍の価格で約 2.5 倍の速度を実現します。Opus 4.7 と 4.6 は $30/$150 のまま変わりません。Opus 4.6 のファストモードは廃止予定です。
🔗 https://code.claude.com/en/fast-mode#understand-the-cost-tradeoff

## ✨ その他のアップデート

- `claude agents` で、シェルコマンドの先頭に `!` を付けると、アタッチ・デタッチ可能なバックグラウンドジョブとして実行できます。`claude --bg --exec 'pytest -x'` としても利用可能です
- `.claude/skills` ディレクトリのプラグインが自動的に読み込まれるようになりました（マーケットプレイス不要）。`claude plugin init <名前>` で新しいプラグインの雛形を作成できます
- 新しい `/reload-skills` コマンドで再起動不要でスキルディレクトリを再スキャンできます。また `SessionStart` フックが `reloadSkills: true` を返すことで、インストールしたスキルを同一セッション内で利用可能にできます
- スキルとコマンドのフロントマターに `disallowed-tools` を設定することで、スキルが有効な間はそのツールをモデルから除外できます
- 新しい `MessageDisplay` フックイベントにより、フックがアシスタントのメッセージテキストを表示時に変換・非表示にできます
- プライマリモデルが見つからない場合、毎回エラーにする代わりに、設定された `--fallback-model` にセッション全体で切り替わるようになりました
- プラグインが `plugin.json` またはマーケットプレイスエントリで `defaultEnabled: false` を宣言できるようになり、有効化するまでオフの状態でインストールされます
- Vim モード：NORMAL モードで `/` を押すと逆方向ヒストリ検索が開き、Bash/Zsh の vi モードと同じ操作感になりました
- テレメトリ無効時や Bedrock・Vertex・Foundry 環境でも、ストリーミングツール実行が常に有効になりました
- `←←` でエージェントビューを開く操作が Bedrock・Vertex・Foundry およびテレメトリ無効時でも動作するようになりました
- Claude in Chrome：`/chrome` → 「Select browser…」から接続中のブラウザを選択できます。複数接続時はブラウザアクション実行中にチャット内で選択することも可能です
- `claude mcp list` と `claude mcp get` で、未承認の `.mcp.json` サーバーが自動承認・接続されるのではなく、承認待ちとして表示されるようになりました（出力がパイプされる場合）

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w22
