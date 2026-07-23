# 📅 Claude Code 週刊アップデート — Week 29 · July 13–17, 2026

> 公開済みアーティファクトから MCP コネクターを通じてライブデータを取得できるようになりました。また、新しいスクリーンリーダーモードで Claude Code をスクリーンリーダーと併用できるようになりました。

## 🚀 主要機能 (2 件)

### Artifacts call your MCP connectors `web`
公開済みアーティファクトが、誰かがそれを閲覧するたびに MCP コネクターを呼び出せるようになりました。これにより、ダッシュボードはセッション作成時のスナップショットではなく、ライブデータを表示し、必要に応じてアクションを実行できます。各呼び出しは閲覧者自身のアカウントの接続を通じて実行され、閲覧者はページが最初にコネクターを呼び出す前にアクセスを承認します。今週は公開共有リンク、Team・Enterprise プランでの共同編集のためのエディタロール、Claude Tag セッションから作成されたアーティファクトも追加されました。
🔗 https://code.claude.com/en/artifacts#pull-live-data-with-mcp-connectors

### Screen reader mode `CLI`
スクリーンリーダーモードは、ビジュアルなターミナルインターフェースをプレーンなリニアテキストに置き換えます。ボックス、スピナー、画面内書き換えの代わりに、Claude Code は VoiceOver や NVDA などのスクリーンリーダーが順番に読み上げられるラベル付き行を出力するため、権限の承認や出力のレビューをエンドツーエンドで行えます。セッションごとにフラグで有効化、シェルごとに `CLAUDE_AX_SCREEN_READER` 環境変数で、またはすべての場所で `axScreenReader` 設定を使って有効にできます。
🔗 https://code.claude.com/en/accessibility#turn-on-screen-reader-mode

## ✨ その他のアップデート

- `/fork` は会話を新しいバックグラウンドセッションにコピーし、作業を続けながら `claude agents` に独自の行を追加するようになりました。以前の「セッション内フォークサブエージェント」機能は `/subtask` に改名されました
- Auto モードは Amazon Bedrock、Google Cloud の Agent Platform、Microsoft Foundry で `CLAUDE_CODE_ENABLE_AUTO_MODE` のオプトインが不要になりました。管理者は `disableAutoMode` で無効化できます
- 2 分以上かかる MCP ツール呼び出しは、セッションを使い続けられるよう自動的にバックグラウンドに移行します。`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` でしきい値を調整または無効化できます
- 新しい `claude auto-mode reset` コマンドでデフォルトの Auto モード設定を復元できます。`--yes` フラグで確認プロンプトをスキップできます
- 新しい企業向けランチャーサポート: `CLAUDE_CODE_PROCESS_WRAPPER` または `processWrapper` 設定で、Claude Code がバイナリから起動するプロセス（バックグラウンドサービスやエージェントビューセッション）を必要なラッパー実行可能ファイルを通して実行できます
- `vimInsertModeRemaps` 設定で `jj` から Escape へのような2キーの挿入モードシーケンスを vim モードにマッピングできます
- `--forward-subagent-text` および `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` でサブエージェントのテキストとシンキングブロックを stream-json 出力に含めることができます
- セッション全体の上限でループの暴走を防止: WebSearch 呼び出しとサブエージェントの生成はそれぞれデフォルト 200 に設定され、`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` と `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` で調整できます
- 「常に許可」の権限ルールがリポジトリのルートに保存されるようになり、git ワークツリーで許可された承認がセッションやワークツリーをまたいで永続化されます
- Amazon Bedrock、Google Cloud の Agent Platform、AWS 上の Claude Platform がデフォルトで Claude Opus 4.8 を使用するようになりました
- 折りたたまれたツールのサマリー行にライブ経過時間カウンターが表示されるようになり、長時間実行中のツール呼び出しが止まっているように見えなくなりました

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w29
