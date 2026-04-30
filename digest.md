# AI Daily Digest — 2026-05-01

## Claude Code / Anthropic アップデート

### v2.1.123 (2025-04-29)

**バグ修正**
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` 設定時に OAuth 認証が 401 リトライループに陥る問題を修正。

**ユーザーへの影響**: ベータ機能を無効化した環境で認証が正常に機能するようになります。

---

### v2.1.122 (2025-04-28)

**主要機能**
- `ANTHROPIC_BEDROCK_SERVICE_TIER` 環境変数を追加。`default`・`flex`・`priority` から Bedrock サービスティアを選択可能。リクエスト時に `X-Amzn-Bedrock-Service-Tier` ヘッダーとして送信されます。
- `/resume` 検索ボックスに PR URL を貼り付けると、その PR を作成したセッションが検索できるように (GitHub / GitHub Enterprise / GitLab / Bitbucket 対応)。
- `/mcp` が、手動追加サーバーと同じ URL で隠れていた claude.ai コネクターを表示し、重複削除のヒントを提示するように改善。

**バグ修正 / 改善**
- OpenTelemetry: `api_request`/`api_error` ログの数値属性が文字列ではなく数値で出力されるように修正。
- OpenTelemetry: `@`-メンション解決の `claude_code.at_mention` ログイベントを追加。

**ユーザーへの影響**: AWS Bedrock 利用者はサービスティアを柔軟に制御できます。過去セッションからの PR 追跡や MCP 管理 UI が大幅に使いやすくなります。

---

### v2.1.121 (2025-04-28)

**主要機能**
- MCP サーバー設定に `alwaysLoad` オプションを追加。`true` にするとそのサーバーの全ツールがツール検索の遅延をスキップして常時利用可能になります。
- `claude plugin prune` コマンドを追加。孤立した自動インストール済みプラグイン依存関係を削除。`plugin uninstall --prune` でカスケード削除も可能。
- `/skills` にテキストフィルター検索ボックスを追加。長いリストでスクロールなしにスキルを検索できます。
- PostToolUse フックが全ツールで `hookSpecificOutput.updatedToolOutput` によるツール出力置き換えに対応 (以前は MCP のみ)。

**バグ修正**
- フルスクリーンモード: 上にスクロールして過去の出力を読んでいる際に、プロンプト入力でスクロール位置が最下部に戻る問題を修正。

**ユーザーへの影響**: MCP ツールの常時ロード、プラグイン管理の改善、フックの柔軟性向上など、開発者・ヘビーユーザー向けの機能強化が多数含まれます。

