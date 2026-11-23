# AI Daily Digest — 2026-11-24

## Claude Code / Anthropic アップデート

### v2.1.331 (2026-11-23)
**主要機能**
- **Code Mode がクラウドプロバイダー対応**: Amazon Bedrock、Google Cloud Agent Platform、Microsoft Foundry、AWS上のClaudeプラットフォームでターミナルセッション内のCode Modeが利用可能に
- **ゲートウェイのOIDCグループ設定強化**: `oidc.groups_jsonpath` によりオブジェクトリストからJSONPath (RFC 9535) でグループ情報を読み取り可能
- **`claude doctor` に API接続診断**: APIへの到達確認、HTTPステータスやエラー表示の新セクション追加
- **音声入力の停止通知**: タップモード音声ディクテーションが15秒無音または2分の上限で自動停止する際に通知表示
- **プロキシ圧縮問題の回避**: `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` 環境変数で圧縮レスポンスを切断するプロキシへの対策

**ユーザーへの影響**: クラウドプロバイダー経由でClaudeを利用している企業ユーザーはCode Modeが使えるようになり、エンタープライズ環境での活用が大きく広がる。

---

### v2.1.330 (2026-11-20)
**主要機能**
- **Enterprise Admin Consoleからの組織サインイン**: `claude auth login` 後にAnthropicのEnterprise Admin Consoleで管理された組織の設定が自動適用される
- **easel 組み込みモッド**: チャートの自動描画機能がPro/Max（一部Team/Enterprise）でmacOS/Linuxに追加、`/config` でオフ可能
- **フルサインインリンク表示**: `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` で短縮URLが表示エラーになる場合に完全URLを出力
- **セルフホストランナーの開始ディレクトリ指定**: `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR` で作業開始フォルダを指定可能

**ユーザーへの影響**: Enterprise向けに組織管理が一元化され、使いやすくなった。easelはデータ可視化を自動化し、MCP メトリクス結果の確認効率が向上する。

---

### v2.1.329 (2026-11-19)
**主要機能**
- **フックの信頼ダイアログにフック宣言元を表示**: どのフォルダのhooks設定かを警告ダイアログで確認可能
- **非インタラクティブホストのフック読み込み失敗警告**: Claude Desktopなどでhooksが読み込めない場合に会話内に警告
- **`/tasks` にスケジュールタスク・loopウェイクアップ・ゴール・フォーク表示**: タスク管理UIが大幅強化、`x` で停止確認
- **MCPサーバーのJSONRPCエラーメッセージ表示**: `/mcp` のサーバーページでリモートHTTP MCPサーバーの接続拒否メッセージを表示
- **マーケットプレイス自動更新の可視化**: `/status` に管理マーケットプレイス名を表示する行が追加

**ユーザーへの影響**: セキュリティの透明性向上とタスク管理の強化が目玉。特に `/tasks` の改善でスケジュール実行の監視が容易になった。

