# AI Daily Digest — 2026-09-03

## 今日のハイライト
- **Qwen-Drive-1.0 (337 upvotes)**: 自動運転向けVLM登場。3D認識・QA・運動計画を統合し、業界標準ベンチマークをリード。
- **Claude Code v2.1.259**: 組織向け `managedMcpServers`、ヘッドレス `--permission-prompts none`、GitLab MR表示など多数の企業向け機能を追加。
- **UI-Venus-2 & ZimaBlue**: GUIエージェントとロボット操作向け世界モデルの実用化研究が相次いで公開。


## Claude Code アップデート

**v2.1.259** (2024-09-02)
- `managedMcpServers` 設定追加：組織が全ユーザーに HTTP/SSE MCP サーバーを提供可能に
- `--permission-prompts none` オプション追加：無人ヘッドレスホスト向けに自動拒否モード
- GitLab MR コマンド (`glab mr create/merge` 等) のサマリー表示対応
- `claude plugin validate --json` で機械可読な検証レポート出力
- 複数セッション同時実行時の `~/.claude.json` 上書き競合バグを修正

**v2.1.258** (2024-09-01)
- macOS 12 (Monterey) で起動できないリグレッションを修正 (v2.1.255 で混入)
- リモート・スケジュールセッションで「non-empty content」エラーになるバグを修正

**v2.1.257** (2024-09-01)
- Claude Fable 5.1 (`claude-fable-5-1`) 追加・デフォルト化：1M コンテキスト、$10/$50/Mtok
- 時刻フォーマット設定 (`timeFormat`/`timeZone`) 追加
- Auto モードに Containment Escape ルール追加：クラウドメタデータ取得等を自動承認しない
- `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` 環境変数追加：全サブエージェントのモデル強制指定

## 注目論文 TOP 10

**1. Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving**
👍 337 upvotes | arXiv: https://arxiv.org/abs/2609.00111
自動運転向けの視覚言語基盤モデル。3D認識・視覚Q&A・運動計画を共有表現で統合した統一フレームワークを提案。大規模マルチモーダル学習により、複雑な交通シナリオでの判断力を大幅に向上させる。

**2. SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers**
👍 70 upvotes | arXiv: https://arxiv.org/abs/2609.01343
Mixture-of-Experts（MoE）にLooped Transformerを組み合わせたアーキテクチャの研究。トークンあたりの計算量・パラメータ数・キャッシュを揃えた条件下で、4種類のモデルサイズにわたってスケーリング則を導出。訓練効率と下流性能を両立する設計指針を提供する。

**3. UI-Venus-2 Technical Report**
👍 54 upvotes | arXiv: https://arxiv.org/abs/2609.00028
モバイル・Web・デスクトップ環境を横断する汎用マルチモーダルGUIエージェント。統一的なクローズドループ推論-行動フレームワークと環境カバレッジ拡大・堅牢な検証機構を実装。複雑なUI操作タスクでの汎化性能を大幅に改善した。

**4. ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training**
👍 39 upvotes | arXiv: https://arxiv.org/abs/2609.00188
大規模一人称視点映像からの世界行動モデル学習フレームワーク。3段階カリキュラムとslow-fastアーキテクチャを採用し、ロボット操作タスクへの汎化能力を持つ世界モデルを構築。実環境での多様な操作を可能にする。

**5. From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix**
👍 31 upvotes | arXiv: https://arxiv.org/abs/2609.01572
本番トラフィックから収集した社内リクエスト分布を使い、GRPO専門家モデルをSLERPでマージして自社ホスト型LLMを構築。指示追従・関数呼び出し・内部タスクで、より大型のベースラインを低コストで上回ることを実証。

**6. Safin-1: Safety from Within through Memory-Native State Evolution**
👍 19 upvotes | arXiv: https://arxiv.org/abs/2609.00092
安全性をモデルの内部状態として埋め込むメモリルーティングアーキテクチャ。Memory-Anchor Routing（MAR）とContext History全体の状態進化を組み合わせ、テスト時適応をサポート。外部フィルターに頼らず、モデル内部から安全性を担保する新アプローチ。

**7. AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling**
👍 16 upvotes | arXiv: https://arxiv.org/abs/2608.26623
エージェント的ツール呼び出しにおけるLLM-as-a-judgeの信頼性を系統的に研究する初のベンチマーク。DAGワークフロー上で3,808インスタンスを使用し、構造的な上限（ceiling limits）を明らかにした。難易度別の評価で審判LLMの限界を定量化する。

**8. DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory**
👍 14 upvotes | arXiv: https://arxiv.org/abs/2609.00768
言語モデルの自己進化を改善する手法。モデルの内部失敗履歴から階層的なエラー原因メモリを構築し、ダブル信頼度フィルタリングで訓練方向を導出。自己改善ループの質と効率を大幅に向上させる診断誘導型アプローチ。

**9. Agents in the Large: Perception-Centered Architecture for Persistent Agents**
👍 7 upvotes | arXiv: https://arxiv.org/abs/2608.30478
持続的な言語エージェント向けの知覚中心アーキテクチャ。エピソードタスク・コンテキスト・環境変化からのシグナルを知覚することで、サービス手順を継続的に適応・進化させる。長期運用シナリオでの堅牢性を重視した設計。

**10. Learning Where Outcomes Change: Credit-Addressable Reasoning for Multimodal Geometry**
👍 3 upvotes | arXiv: https://arxiv.org/abs/2608.30457
実行可能なコードトレースと局所的な強化学習を用いた信用割り当て可能な推論手法。構造化イベントとの信用割り当てを整合させることで、マルチモーダル幾何推論を改善。空間的な問題解決での精度向上に貢献する。

