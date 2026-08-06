# 📅 Claude Code 週刊アップデート — Week 29 · July 13–17, 2026

> MCP コネクターを通じて公開アーティファクトにライブデータを取り込む機能と、スクリーンリーダー向けの新モードが追加されました。

## 🚀 主要機能 (2 件)

### Artifacts call your MCP connectors `web`
公開済みアーティファクトが閲覧のたびに MCP コネクターを呼び出せるようになりました。これにより、セッション作成時のスナップショットではなく、ダッシュボードがリアルタイムデータを表示し、オンデマンドでアクションを実行できます。各呼び出しは閲覧者自身のアカウントの接続を通じて実行され、ページの最初のコネクター呼び出し前に閲覧者がアクセスを承認します。今週はさらに、公開共有リンク、Team・Enterprise プランでの共同編集のためのエディターロール、Claude Tag セッションから作成されるアーティファクトも追加されました。
🔗 https://code.claude.com/en/artifacts#pull-live-data-with-mcp-connectors

### Screen reader mode `CLI`
スクリーンリーダーモードは、ビジュアルなターミナルインターフェースをプレーンな線形テキストに置き換えます。ボックス、スピナー、インプレース再描画の代わりに、Claude Code はラベル付きの行を順番に出力するため、VoiceOver や NVDA などのスクリーンリーダーが順序通りに読み上げ、権限承認や出力確認をエンドツーエンドで行えます。フラグでセッションごとに有効化、`CLAUDE_AX_SCREEN_READER` 環境変数でシェルごとに設定、または `axScreenReader` 設定で全体に適用できます。
🔗 https://code.claude.com/en/accessibility#turn-on-screen-reader-mode

## ✨ その他のアップデート

- `/fork` が会話を新しいバックグラウンドセッションにコピーし、`claude agents` に独自の行を持ちながら作業を継続できるようになりました。以前の `/fork` で起動していたインセッションのフォークされたサブエージェントは `/subtask` に変更されました
- Amazon Bedrock、Google Cloud の Agent Platform、Microsoft Foundry での Auto モードに `CLAUDE_CODE_ENABLE_AUTO_MODE` のオプトインが不要になりました。管理者は `disableAutoMode` で無効化できます
- 2 分以上実行される MCP ツール呼び出しが自動的にバックグラウンドに移動し、セッションを使いやすい状態に保ちます。`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` でしきい値の調整や無効化が可能です
- 新しい `claude auto-mode reset` がデフォルトの Auto モード設定を復元します。`--yes` で確認プロンプトをスキップできます
- 新しいコーポレートランチャーサポート: `CLAUDE_CODE_PROCESS_WRAPPER` または `processWrapper` 設定で、Claude Code が独自のバイナリから起動するプロセス（バックグラウンドサービスやエージェントビューセッションなど）を必須ラッパー実行ファイル経由で実行できます
- `vimInsertModeRemaps` 設定で `jj` など 2 キーのインサートモードシーケンスを Vim モードで Escape にマッピングできます
- `--forward-subagent-text` と `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` でサブエージェントのテキストとシンキングブロックをストリーム JSON 出力に含めることができます
- セッション全体のキャップで暴走ループを防止: WebSearch 呼び出しとサブエージェントの起動はそれぞれデフォルトで 200 回に制限され、`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` と `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` で調整可能です
- 「常に許可」の権限ルールがリポジトリルートに保存されるようになり、git ワークツリーで付与された承認がセッションやワークツリーをまたいで永続化されます
- Amazon Bedrock、Google Cloud の Agent Platform、AWS 上の Claude Platform がデフォルトで Claude Opus 4.8 を使用するようになりました
- 折りたたまれたツールサマリー行にライブの経過時間カウンターが表示されるようになり、長時間実行中のツール呼び出しが止まっているように見えず、視覚的に進行中であることが確認できます

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w29
