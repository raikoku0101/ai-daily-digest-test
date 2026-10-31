# AI Daily Digest — 2026-11-01

## Claude Code / Anthropic アップデート

### v2.1.316 (2026-10-31) — 最新
**主要新機能:**
- `CLAUDE_CODE_DISABLE_ULTRATHINK` 環境変数追加: `ultrathink` キーワードによる超高思考モードを無効化できるようになった
- **プールグループバジェット**: Claude apps gateway でグループメンバーが共有できる月次バジェットを追加。`pooled_budget` で管理 API から設定可能
- `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP`: プライベート CA がループ状の相互認証を必要とするサーバー向けに証明書を保持するオプション
- `CLAUDE_CODE_SUBAGENT_EFFORT`: サブエージェントの思考レベルをデフォルト設定できる新環境変数

**ユーザーへの影響:** ultrathink の誤発動を防ぎたいチームや、エンタープライズ向けグループバジェット管理が必要な組織に直接的な利点あり。

---

### v2.1.314 (2026-10-30)
**主要新機能:**
- `permissions.blockWritesOutsideWorkingDirectories`: Write/Edit/NotebookEdit がワーキングディレクトリ外のパスへの書き込みを全モードで拒否するセキュリティ強化
- Claude apps gateway の upstream に `groups` リスト追加: 特定 IdP グループのみを特定 upstream に誘導可能に
- `guardrail_trace`: Bedrock guardrail フィルターの発火ログ（マッチしたテキストなし）を記録

**バグ修正:**
- VS Code 拡張からサインインした後、managed settings と組織ポリシーがセッション内で取得されなくなる問題を修正

**ユーザーへの影響:** セキュリティ意識の高いチームにとって `blockWritesOutsideWorkingDirectories` は重要な保護機能。VS Code ユーザーには組織ポリシー適用の安定性向上。

---

### v2.1.312 (2026-10-27)
**主要新機能:**
- `oidc.user_id_claim`: Microsoft Entra ID の `oid` など `sub` 以外のクレームでユーザーを識別可能に
- **クリックして送信**: フルスクリーンモードで「今すぐ送信」ヒントをクリックするだけでキューのメッセージを即時送信

**バグ修正:**
- 大きな CLAUDE.md やルールファイルを途中から読み込み後に上書きしてしまう問題を修正
- Write ツールが読み込みを先に行うよう改善

**ユーザーへの影響:** エンタープライズ IdP 統合が柔軟化。大型プロジェクトで CLAUDE.md が消えていた問題が解消される重要修正。

