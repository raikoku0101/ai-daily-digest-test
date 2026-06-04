# 📅 Claude Code 週刊アップデート — Week 22 · May 25–29, 2026

> Claude Code が Claude Opus 4.8 で動作するようになり、ダイナミックワークフローで大規模タスクのオーケストレーションが可能に。security-guidance プラグインでセキュリティ問題を検出し、Opus 4.8 のファストモードをより低価格で利用できます。

## 🚀 主要機能 (4 件)

### Claude Opus 4.8 `new model`
Opus 4.8 が Max、Team Premium、Enterprise 従量課金、および Anthropic API でのデフォルトモデルになりました。デフォルトで高い推論努力で動作し、より難しいタスクには `/effort xhigh` を使用できます。v2.1.154 以降が必要です。
🔗 https://code.claude.com/docs/en/model-config#available-models

### Dynamic workflows `research preview`
ワークフローとは、Claude があなたのタスクのために作成し、バックグラウンドで多数のサブエージェントにわたって実行するオーケストレーションスクリプトです。コードベース全体の監査、大規模な移行、クロスチェックが必要な調査など、一つの会話で調整しきれない大きなタスクに活用してください。`/workflows` でランを管理できます。
🔗 https://code.claude.com/docs/en/workflows

### Security guidance plugin `plugin`
security-guidance プラグインは、Claude のコード変更を脆弱性について確認し、同じセッション内で修正します。各編集時に高速なパターンチェックを実行し、各ターン終了時にモデルによるレビューを行い、コミットまたはプッシュ時により深いエージェント型レビューを実施します。プロジェクトのルールは `.claude/claude-security-guidance.md` に追加できます。
🔗 https://code.claude.com/docs/en/security-guidance

### Fast mode on Opus 4.8 `research preview`
ファストモードが Opus 4.8 をデフォルトとして採用し、1MTok あたり $10/$50 の価格設定に。標準レートの 2 倍の価格で約 2.5 倍の速度を実現します。Opus 4.7 と 4.6 は $30/$150 のまま据え置き。Opus 4.6 のファストモードは非推奨となります。
🔗 https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff

## ✨ その他のアップデート

- `claude agents` で、シェルコマンドの先頭に `!` を付けるとバックグラウンドジョブとして実行でき、アタッチ・デタッチが可能。`claude --bg --exec 'pytest -x'` としても利用できる
- `.claude/skills` ディレクトリ内のプラグインが自動的に読み込まれるようになり、マーケットプレイス不要。`claude plugin init <name>` で新しいプラグインのひな形を作成できる
- 新しい `/reload-skills` コマンドで再起動なしにスキルディレクトリを再スキャン可能。`SessionStart` フックが `reloadSkills: true` を返すことで、同一セッション内でインストールしたスキルをすぐ利用できる
- スキルとコマンドのフロントマターに `disallowed-tools` を設定することで、スキル有効中は特定ツールをモデルから除外できる
- 新しい `MessageDisplay` フックイベントにより、フックがアシスタントのメッセージテキストを表示時に変換または非表示にできる
- プライマリモデルが見つからない場合、Claude Code は設定済みの `--fallback-model` に自動切り替えして残りのセッションを継続するようになった（従来は毎リクエスト失敗）
- プラグインが `plugin.json` やマーケットプレイスエントリで `defaultEnabled: false` を宣言できるようになり、インストール時は無効状態で配置される
- Vim モード: NORMAL モードで `/` を押すと逆履歴検索が開くようになり、Bash・Zsh の vi-mode と同様の操作が可能
- ストリーミングツール実行が常に有効になった（テレメトリ無効時や Bedrock・Vertex・Foundry でも）
- `←←` でエージェントビューを開く操作が Bedrock・Vertex・Foundry およびテレメトリ無効環境でも動作するようになった
- Claude in Chrome: `/chrome` → 「Select browser...」から接続中のブラウザを選択可能。複数ブラウザが接続されている場合はチャット内でも選択できる
- `claude mcp list` と `claude mcp get` が、未承認の `.mcp.json` サーバーを自動承認・接続せず、出力がパイプ経由の場合は承認待ちとして表示するようになった

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w22
