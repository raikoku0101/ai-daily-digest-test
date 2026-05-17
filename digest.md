# AI Daily Digest — 2026-05-18

## Claude Code / Anthropic アップデート

### v2.1.143 (2025-05-15)
**主要機能**:
- **プラグイン依存関係の強制適用**: `claude plugin disable` で依存プラグインがある場合に拒否（コピー可能な無効化チェーンヒント付き）。`claude plugin enable` は推移的依存関係を自動で有効化。
- **プロジェクテッドコンテキストコスト表示**: `/plugin` マーケットプレイスのブラウズペインにターン毎・呼び出し毎のトークン推定コストを追加。
- **`worktree.bgIsolation: "none"` 設定**: バックグラウンドセッションが `EnterWorktree` なしで直接作業コピーを編集可能に（worktree が難しいリポジトリ向け）。
- **PowerShell の `-ExecutionPolicy Bypass` 自動適用**: `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` でオプトアウト可能。
- **バックグラウンドセッションのモデル/エフォート保持**: アイドル復帰後も設定が維持されるように。
- **Shift+Tab の auto モード追加**: アタッチされたエージェントセッションでのサイクルに auto モードが追加。

**バグ修正**:
- `.credentials.json` の `scopes` が非配列の場合に CLI が起動時にハングする問題、またはOAuth トークンリフレッシュが無音で中断する問題を修正。
- Windows Terminal / WSL での `claude agents` の右クリックペースト問題を修正。

**ユーザーへの影響**: プラグイン管理が安全になり、コスト可視化でトークン消費を事前把握できる。worktree 非対応環境でもバックグラウンドエージェントが利用しやすくなった。

---

### v2.1.142 (2025-05-14)
**主要機能**:
- **`claude agents` の新フラグ群**: `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions` でディスパッチされたバックグラウンドセッションを細かく設定可能。
- **Fast モードが Opus 4.7 に更新**: デフォルトが Opus 4.6 から 4.7 へ。`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` で 4.6 に固定可能。
- **ルートレベル `SKILL.md` のプラグインをスキルとして認識**: `skills/` サブディレクトリがなくても機能。
- **LSP サーバー情報の表示**: `/plugin` 詳細ペインおよび `claude plugin details` でプラグインが提供する LSP サーバーを表示。

**バグ修正**:
- `MCP_TOOL_TIMEOUT` がリモート HTTP/SSE MCP サーバーのフェッチタイムアウトに反映されず、常に60秒に制限されていた問題を修正。

**ユーザーへの影響**: バックグラウンドエージェントのカスタマイズ性が大幅向上。Fast モードの性能アップ（Opus 4.7 利用）でコーディング速度改善。

---

### v2.1.141 (2025-05-13)
**主要機能**:
- **フック JSON 出力に `terminalSequence` フィールド追加**: 制御端末なしでデスクトップ通知・ウィンドウタイトル・ベルをフックから送出可能。
- **`CLAUDE_CODE_PLUGIN_PREFER_HTTPS`**: SSH キーなし環境向けに GitHub プラグインソースを HTTPS でクローン。
- **`ANTHROPIC_WORKSPACE_ID` 環境変数**: ワークロードアイデンティティフェデレーション用。フェデレーションルールが複数ワークスペースを対象とする場合にスコープを特定ワークスペースに限定。
- **`claude agents --cwd <path>`**: セッション一覧をディレクトリにスコープ。
- **`/feedback` に過去セッション添付機能**: 直近24時間または7日間のセッションを含められるように。
- **Rewind メニューの「Summarize up to here」**: 最近のターンを保持しつつ、それ以前のコンテキストを圧縮。

**ユーザーへの影響**: フックの表現力向上でCI連携が強化。ワークスペースIDによるセキュリティ管理が精密化。フィードバック送信が容易になった。

