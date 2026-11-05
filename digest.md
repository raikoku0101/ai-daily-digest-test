# AI Daily Digest — 2026-11-06

## Claude Code / Anthropic アップデート

### v2.1.318 (2026-11-04)

**主要機能**
- **Mod 有効化の記録**: セッション中に Claude Code が作成した mod を有効にするよう問われた際、ユーザーの回答が記録されるようになった
- **AWS assume_role サポート**: Claude apps gateway の `mantle` upstream に `assume_role` を追加。別 AWS アカウントのロール切り替えと開発者ごとの AWS コスト帰属が可能に
- **Mod の effort オプション**: `$.model.fork` に `effort` オプションを追加。サイドジョブを `low` effort で実行でき、結果に使用した effort が報告される
- **サインイン有効期限**: `claude auth status` に `loginExpiresAt`、`claude -p` の JSON 結果に `credential_expires_at` を追加

**ユーザーへの影響**: mod 開発者は fork の effort を細かく制御できるようになった。企業利用では AWS コスト管理が改善される。

---

### v2.1.317 (2026-11-03)

**主要機能**
- **スケジュールコネクター警告**: `/schedule` で不要なコネクターが付いた場合に警告と削除方法を表示
- **メールアドレス送信チェック**: Web/シェルツールがアカウントのメールアドレスをネットワークに送信する前に確認を求める
- **Hook の onFailure: "block"**: Agent SDK のフック callback に `onFailure: "block"` を追加。失敗した callback がアクションをブロックできるように
- **設定未読み込み通知**: Claude Desktop の Code タブで組織のリモート管理設定が読み込まれていない場合に通知

**ユーザーへの影響**: セキュリティとプライバシー強化。意図しないメール漏洩や、フック失敗時の予期しないアクション実行を防止できる。

---

### v2.1.316 (2026-10-31)

**主要機能**
- **CLAUDE_CODE_DISABLE_ULTRATHINK**: `ultrathink` キーワードを無効化する環境変数を追加
- **グループプール予算**: Claude apps gateway にグループメンバーが共有する月次予算を追加。`pooled_budget` で管理
- **CLAUDE_CODE_SUBAGENT_EFFORT**: セッションの effort を継承する代わりに、サブエージェントのデフォルト effort を設定できる新しい環境変数

**ユーザーへの影響**: 組織での予算管理が柔軟に。サブエージェントの計算コストをより細かく制御できるようになった。

