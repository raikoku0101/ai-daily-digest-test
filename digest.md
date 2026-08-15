# AI Daily Digest — 2026-08-16

## Claude Code / Anthropic アップデート

### v2.1.233 (2025-08-14)
**主要機能**:
- GitLab MR URL サポートが `--worktree` フラグと `claude agents` ビューに追加（MR は `!N` 形式で表示）
- `forward_user_identity` オプション設定：Anthropic upstream でサインイン済みユーザーのアイデンティティをヘッダーとして送信可能に
- Linux での Bash ツールコマンドに memory cgroup サポートを追加（`CLAUDE_CODE_TOOL_MEMORY_LIMIT`）— 暴走ビルドがセッションを止めるのを防止
- `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` 環境変数で WebFetch のキャッシュ TTL を設定可能に

**バグ修正**:
- Claude がパーミッションプロンプト待機中に環境がシャットダウンすると、クラウドセッションが「lost」とマークされる問題を修正

**ユーザーへの影響**: GitLab ユーザーは MR を直接 worktree から参照可能に。Linux 環境での安定性向上。

---

### v2.1.232 (2025-08-13)
**主要機能**:
- サブエージェントのフォーキングがデフォルト有効に：`subagent_type: "fork"` で会話履歴とプロンプトキャッシュを継承
- プロンプトで `@` を入力して他の Claude セッションを名前でメンション可能
- `SendMessage` が同名のライブセッションに直接配信
- セッション名の一意性管理：重複名には `name-word-word` 形式のバリアントを自動付与
- `/config` に「Dialog expiry」と「他セッションからのメッセージ」設定行を追加
- GitLab トークンファミリーとルーティング可能なトークンのシークレット自動リダクション機能を追加

**ユーザーへの影響**: マルチエージェント協調作業が大幅に強化。セキュリティも向上。

---

### v2.1.231 (2025-08-13)
**バグ修正（クリティカル）**:
- Slack など、事前登録済み OAuth クライアントを使用する MCP サーバーで MCP OAuth サインインが redirect URI ミスマッチで失敗する問題を修正

**ユーザーへの影響**: Slack MCP など OAuth 認証を使う MCP サーバーが正常に動作するように。

