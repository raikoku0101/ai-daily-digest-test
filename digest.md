# 📅 Claude Code 週刊アップデート — Week 20 · May 11–15, 2026

> すべての Claude Code セッションを 1 つの画面で管理する「エージェントビュー」、条件が満たされるまで Claude が自律的に作業を続ける「/goal」、そしてデフォルトで Opus 4.7 上で動作するようになった「ファストモード」が登場しました。

## 🚀 主要機能 (3 件)

### Agent view `research preview`
`claude agents` コマンドで、すべての Claude Code セッションを 1 画面で確認できます。実行中・入力待ち・完了済みのセッションを一覧表示。バグ修正・プルリクレビュー・フレイキーテスト調査を 3 つの行として並列実行しながら、別ウィンドウで作業を続け、必要なときだけ介入できます。任意の行にアタッチして全会話に入り、`←` キーで一覧へ戻ることができます。バックグラウンドセッションは端末なしでも動き続けます。
🔗 https://code.claude.com/en/agent-view

### /goal `v2.1.139`
完了条件を設定すると、Claude がその条件を満たすまで各ターン後に自律的に作業を続けます。毎ターン後に高速モデルが条件の充足を確認し、未達の場合はコントロールを返さずに次のターンを開始します。「すべてのコールサイトがコンパイルを通過してテストがパスするまでモジュールを移行する」といった検証可能な終了状態を持つ大規模な作業に最適です。条件達成後はゴールがクリアされ、インタラクティブ・`-p`・Remote Control のいずれでも動作します。
🔗 https://code.claude.com/en/goal

### Fast mode on Opus 4.7 `research preview`
`/fast` のデフォルトが Opus 4.6 から Opus 4.7 に変更されました。ファストモードは高速 Opus 構成で、同等のモデル品質を約 2.5 倍の速度で提供します（トークン単価は高め）。素早いイテレーションやライブデバッグに最適です。料金は Opus 4.6 ファストモードと同じ $30/$150 per MTok のまま変わりません。Opus 4.6 に固定したい場合は `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` を設定してください。
🔗 https://code.claude.com/en/fast-mode#use-fast-mode-on-opus-4-7

## ✨ その他のアップデート

- `claude agents` にディスパッチフラグ (`--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions`) が追加され、バックグラウンドセッションを細かく設定可能に。`claude agents --cwd <path>` でセッション一覧をディレクトリ単位に絞り込めるように
- 新しいフック `args: string[]` の exec 形式により、シェルを介さずコマンドを直接起動できるようになり、パスのプレースホルダーのクォートが不要に
- `PostToolUse` フックに新しい `continueOnBlock` 設定オプションが追加。フックの拒否理由を Claude にフィードバックしてターンを継続できる（終了させない）
- フック JSON 出力に新しい `terminalSequence` フィールドが追加。制御端末なしでデスクトップ通知・ウィンドウタイトル・ベル音を出力できる
- Rewind メニューに「ここまでを要約」オプションが追加。最近のターンは保持しつつ以前のコンテキストを圧縮できる
- `ANTHROPIC_API_KEY`、`apiKeyHelper`、または `ANTHROPIC_AUTH_TOKEN` が設定されている場合、Claude.ai ログインと併用していても Remote Control・`/schedule`・Claude.ai MCP コネクタ・通知設定が無効になる。これらの機能を使うには API キーを解除する必要がある
- MCP stdio サーバーがフックと同様に環境変数 `CLAUDE_PROJECT_DIR` を受け取るようになり、プラグイン設定のコマンド内で `${CLAUDE_PROJECT_DIR}` を参照できる
- `claude plugin details <name>` でプラグインのコンポーネント一覧とセッションごとの推定トークンコストを表示できるように。`/plugin` の詳細ペインでプラグインが提供する LSP サーバーも一覧表示される
- ルートレベルに `SKILL.md` があり `skills/` サブディレクトリがないプラグインがスキルとして認識されるようになった
- `/feedback` で過去 24 時間または 7 日間の直近セッションを含められるようになり、現在のセッションをまたぐ問題の報告が可能に
- Agent ツールの `subagent_type` が大文字・小文字とセパレータを問わずマッチするようになり、`"Code Reviewer"` が `code-reviewer` として解決される

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w20
