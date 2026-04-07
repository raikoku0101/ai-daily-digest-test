# AI Daily Digest — 2026-04-07

## 今日のハイライト
- Self-Distilled RLVR が82 upvotesで最注目：強化学習を自己蒸留で改善する新手法が話題
- Claude Code v2.1.92リリース：Bedrockセットアップウィザードとper-model cost breakdownを追加
- HackerNewsでは「古いAIが新しいAIを上回る理由」と LLM Attention 解説記事が同率首位

## Claude Code / Anthropic アップデート
**v2.1.92** (2026-04-04)
- `forceRemoteSettingsRefresh` ポリシー設定を追加
- Bedrock インタラクティブセットアップウィザードを追加
- モデル別コスト内訳（per-model cost breakdown）表示を追加
- サブエージェント起動失敗・prompt-type Stop フックのバグ修正

**v2.1.91** (2026-04-02)
- アノテーション経由で MCP ツール結果の永続化オーバーライドに対応
- `disableSkillShellExecution` 設定を追加
- ディープリンクでのマルチライン入力をサポート
- `bin/` ディレクトリ配下のプラグイン実行ファイルに対応

**v2.1.90** (2026-04-01)
- `/powerup` インタラクティブレッスン機能を追加
- `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` 環境変数を追加
- レート制限ダイアログの無限ループとプロンプトキャッシュミスのリグレッションを修正

## 注目論文 TOP 5

1. **Self-Distilled RLVR（自己蒸留強化学習）** — 82 upvotes — https://huggingface.co/papers/2604.03128
   手法：強化学習（RLVR）において、モデル自身の出力を蒸留ターゲットとして利用し、外部報酬なしに推論能力を向上させる。
   意義：ラベルなしデータで継続的な自己改善が可能になり、LLMの自律的な能力向上に道を開く。

2. **A Simple Baseline for Streaming Video Understanding（ストリーミング動画理解のシンプルなベースライン）** — 55 upvotes — https://huggingface.co/papers/2604.02317
   手法：リアルタイムのストリーミング動画に対してシンプルなフレームサンプリング＋言語モデルを組み合わせた軽量なベースラインを提案。
   意義：複雑なアーキテクチャ不要で高い性能を達成し、動画LLMの評価基準として実用性が高い。

3. **Token Warping Helps MLLMs Look from Nearby Viewpoints（トークンワーピングで多視点認識を改善）** — 23 upvotes — https://huggingface.co/papers/2604.02870
   手法：マルチモーダルLLM（MLLM）に視点変換を模倣するトークンワーピング機構を導入し、隣接視点からの見え方を推定。
   意義：ロボティクスや自動運転など、多視点理解が求められる実世界応用への展開が期待される。

4. **Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?（エージェント型マルチモーダル評価）** — 22 upvotes — https://huggingface.co/papers/2604.03016
   手法：マルチモーダルモデルのエージェント的能力（計画・ツール利用・自律実行）を多段階タスクで定量評価するベンチマークを構築。
   意義：単純なVQAを超えた実用的なエージェント評価指標として、モデル選定・開発の指針になる。

5. **Test-Time Scaling Makes Overtraining Compute-Optimal（テスト時スケーリングで過学習を最適化）** — 15 upvotes — https://huggingface.co/papers/2604.01411
   手法：推論時の計算量を増やす「テスト時スケーリング」により、訓練時の過学習を計算コスト最適な形に変換する理論的枠組みを提示。
   意義：モデルの訓練コスト削減と推論精度の両立に向けた設計指針を提供し、効率的なLLM開発に貢献。

## AI ニュース

1. **「I love you」「too」：LLM のアテンション機構を解説** — 4pts — https://kaamvaam.com/machine-learning-ai/llm-attention-explanation/
   内容：Transformer のアテンション機構を「I love you」という具体例を使ってわかりやすく図解した解説記事。
   注目理由：初心者から中級者まで幅広く参考になる入門コンテンツとして HN コミュニティで評価されている。

2. **古いAIが新しいAIを上回っている理由** — 4pts — https://qz.com/ai-generative-chatbots-llm-machine-learning
   内容：最新のLLMが必ずしも旧世代モデルを上回らないケースを分析し、ベンチマーク設計や用途特化の重要性を論じた記事。
   注目理由：「最新＝最良」という思い込みを問い直す視点が業界で議論を呼んでいる。

3. **LLM実験レポート Part 1：ファインチューニング** — 3pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/18/experiments-in-llms.html
   内容：実際にLLMをファインチューニングした経験から得られた知見・ノウハウをまとめた実践的レポート。
   注目理由：ハンズオンの試行錯誤が詳細に記録されており、LLM開発者の参考資料として継続的に参照されている。

4. **LLM実験レポート：OpenAI Functions の活用** — 2pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/30/experiments-in-llms-3.html
   内容：OpenAI の Function Calling 機能を使った実験と、ツール統合パターンの検証結果をレポート。
   注目理由：Function Calling の初期実装知見として、エージェント開発者にとって参考価値が高い。

5. **LLM実験レポート：ベクターDB と埋め込み** — 2pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/vector/embeddings/2023/06/23/experiments-in-llms-2.html
   内容：ベクターデータベースと埋め込みモデルを組み合わせた RAG（検索拡張生成）の実験と比較検証。
   注目理由：RAG 構築の基礎知識として今なお参照価値が高く、LLMアプリ開発の入門資料として機能している。
