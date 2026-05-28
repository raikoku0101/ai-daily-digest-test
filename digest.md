# 📅 Claude Code 週刊アップデート — Week 20 · May 11–15, 2026

> 全 Claude Code セッションをエージェントビューで一画面から管理、ゴール条件が満たされるまで Claude が自動で作業を継続、そしてファストモードがデフォルトで Opus 4.7 上で動作するようになりました。

## 🚀 主要機能 (3 件)

### Agent view `research preview`
`claude agents` を実行すると、全 Claude Code セッションを一画面で確認できます。実行中のセッション、あなたの入力待ちのセッション、完了済みのセッションが一覧表示されます。バグ修正、プルリクエストレビュー、不安定なテストの調査を 3 行として並列にディスパッチし、別のウィンドウで作業を続けながら、必要なときだけ介入できます。各行にアタッチすればフルの会話へ移行でき、`←` キーで一覧に戻れます。バックグラウンドセッションはターミナルがアタッチされていなくても継続して動作します。
🔗 https://code.claude.com/en/agent-view

### /goal `v2.1.139`
完了条件を設定すると、Claude はあなたがその都度プロンプトを入力しなくても、ターン間にわたってその条件に向けて作業を継続します。ターンが終わるたびに高速モデルが条件を満たしているかチェックし、満たされていなければ制御を返す代わりに Claude が次のターンを開始します。コンパイルとテストが全て通るまでモジュールを移行するといった、検証可能な完了状態がある大きな作業に最適です。条件が満たされるとゴールはクリアされ、インタラクティブモード・`-p` オプション・リモートコントロールのいずれでも動作します。
🔗 https://code.claude.com/en/goal

### Fast mode on Opus 4.7 `research preview`
`/fast` はデフォルトで Opus 4.6 ではなく Opus 4.7 上で動作するようになりました。ファストモードは高速 Opus 設定で、同等のモデル品質をトークンあたりのコストは上がるものの約 2.5 倍の速度で提供し、高速な反復作業やライブデバッグに最適です。料金は Opus 4.6 ファストモードと同様、入力 $30 / 出力 $150 per MTok のまま変わりません。Opus 4.6 に固定したい場合は `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` を設定してください。
🔗 https://code.claude.com/en/fast-mode#use-fast-mode-on-opus-4-7

## ✨ その他のアップデート

- `claude agents` にディスパッチフラグ (`--add-dir`、`--settings`、`--mcp-config`、`--plugin-dir`、`--permission-mode`、`--model`、`--effort`、`--dangerously-skip-permissions`) が追加され、バックグラウンドセッションを設定できるようになりました。また `claude agents --cwd <path>` でセッション一覧を特定ディレクトリに絞り込めます。
- フック `args: string[]` の exec 形式が追加され、シェルを介さずに直接コマンドを実行できるため、パスのプレースホルダーをクォートする必要がなくなりました。
- `PostToolUse` フック向けに新しい `continueOnBlock` 設定オプションが追加されました。フックの拒否理由を Claude にフィードバックしながらターンを終了せずに継続します。
- フック JSON 出力に新しい `terminalSequence` フィールドが追加され、制御端末なしでもデスクトップ通知・ウィンドウタイトル・ベル音を発信できます。
- Rewind メニューに「ここまで要約」が追加され、最近のターンを残したまま以前のコンテキストを圧縮できます。
- `ANTHROPIC_API_KEY`、`apiKeyHelper`、または `ANTHROPIC_AUTH_TOKEN` が設定されている場合、Claude.ai ログインと併用していても、リモートコントロール・`/schedule`・Claude.ai MCP コネクター・通知設定が無効になります。これらの機能を使うには API キーを解除してください。
- MCP stdio サーバーの環境変数に `CLAUDE_PROJECT_DIR` が渡されるようになり、フックと同様に、プラグイン設定のコマンド内で `${CLAUDE_PROJECT_DIR}` を参照できます。
- `claude plugin details <name>` でプラグインのコンポーネント一覧とセッションあたりの推定トークンコストを表示できます。また `/plugin` の詳細ペインにプラグインが提供する LSP サーバーも表示されるようになりました。
- ルートレベルに `SKILL.md` があり `skills/` サブディレクトリがないプラグインが、スキルとして認識されるようになりました。
- `/feedback` で、現在のセッションをまたぐ問題に対して、過去 24 時間または 7 日間の最近のセッションを含められるようになりました。
- Agent ツールの `subagent_type` が大文字・小文字・区切り文字を無視してマッチするようになり、`"Code Reviewer"` が `code-reviewer` に解決されます。

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w20
