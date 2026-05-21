# 📅 Claude Code 週刊アップデート — Week 20 · May 11–15, 2026

> エージェントビューで全ての Claude Code セッションを一画面で管理し、条件が満たされるまでゴールに向けて Claude を動かし続け、Opus 4.7 でのファストモードをデフォルトで実行します。

## 🚀 主要機能 (3 件)

### Agent view `research preview`
`claude agents` で全ての Claude Code セッションを一画面で確認できます：実行中のもの、入力待ちのもの、完了したもの。バグ修正、プルリクエストのレビュー、フレーキーテストの調査を 3 行として派遣し、別ウィンドウで作業を続け、行が必要なときだけ介入できます。任意の行にアタッチして会話全体に入り、`←` を押してリストに戻れます。バックグラウンドセッションはターミナルがアタッチされていなくても動き続けます。
🔗 https://code.claude.com/en/agent-view

### /goal `v2.1.139`
完了条件を設定すると、Claude は各ステップをプロンプトなしに複数ターンにわたって目標に向けて動き続けます。各ターン後、高速モデルが条件を満たしているかチェックし、満たされていなければコントロールを返さずに次のターンを開始します。全コールサイトがコンパイルされてテストがパスするまでモジュールを移行するなど、検証可能な終了状態を持つ大規模な作業に便利です。条件が満たされるとゴールはクリアされ、インタラクティブ、`-p`、リモートコントロールで動作します。
🔗 https://code.claude.com/en/goal

### Fast mode on Opus 4.7 `research preview`
`/fast` がデフォルトで Opus 4.6 の代わりに Opus 4.7 で実行されるようになりました。ファストモードは高速 Opus 設定で、同じモデル品質でトークンあたりコストが高くなる代わりに約 2.5 倍の速度で動作し、高速イテレーションとライブデバッグに便利です。価格は Opus 4.6 ファストモードと同じく MTok あたり $30/$150 のまま変更ありません。ファストモードを Opus 4.6 に固定するには `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` を設定してください。
🔗 https://code.claude.com/en/fast-mode#use-fast-mode-on-opus-4-7

## ✨ その他のアップデート

- `claude agents` がバックグラウンドセッションを設定するディスパッチフラグ（`--add-dir`、`--settings`、`--mcp-config`、`--plugin-dir`、`--permission-mode`、`--model`、`--effort`、`--dangerously-skip-permissions`）を取得し、`claude agents --cwd <path>` でセッションリストをディレクトリにスコープできるようになりました
- 新しいフック `args: string[]` exec フォームがシェルを使わずにコマンドを直接実行するため、パスのプレースホルダーにクォートが不要になりました
- `PostToolUse` フックの新しい `continueOnBlock` 設定オプションにより、フックの拒否理由を Claude に返してターンを終了せずに継続します
- フック JSON 出力の新しい `terminalSequence` フィールドにより、フックが制御端末なしでデスクトップ通知、ウィンドウタイトル、ベルを送信できるようになりました
- リワインドメニューに「ここまでを要約」が追加され、直近のターンを保持しながら以前のコンテキストを圧縮できるようになりました
- `ANTHROPIC_API_KEY`、`apiKeyHelper`、または `ANTHROPIC_AUTH_TOKEN` が設定されている場合、Claude.ai ログインと併用していても、リモートコントロール、`/schedule`、Claude.ai MCP コネクター、通知設定が無効になりました。これらの機能を使用するには API キーを削除してください
- MCP stdio サーバーが環境変数 `CLAUDE_PROJECT_DIR` をフックと同様に受け取るようになり、プラグイン設定のコマンドで `${CLAUDE_PROJECT_DIR}` を参照できるようになりました
- `claude plugin details <name>` でプラグインのコンポーネントインベントリとセッションあたりの予想トークンコストが表示され、`/plugin` 詳細ペインにプラグインが提供する LSP サーバーも表示されるようになりました
- ルートレベルの `SKILL.md` があり `skills/` サブディレクトリがないプラグインがスキルとして表示されるようになりました
- `/feedback` に過去 24 時間または 7 日間の最近のセッションを含められるようになり、現在のセッションをまたぐ問題に対応できるようになりました
- Agent ツールの `subagent_type` が大文字小文字・区切り文字を無視してマッチするようになり、`"Code Reviewer"` が `code-reviewer` に解決されるようになりました

📄 原文: https://code.claude.com/docs/en/whats-new/2026-w20
