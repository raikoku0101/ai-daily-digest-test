## 1. Introduction (はじめに)

大規模言語モデル（LLM）はインタラクティブエージェントとして利用されていますが、長期的な意思決定（Long-Horizon Decision Making）の最適化は困難です。既存手法が主に反応的（Reactive）であるため、長い軌跡（Trajectory）上での探索（Exploration）とクレジット割り当て（Credit Assignment）が弱化しています。本論文は戦略的軌跡抽象化（Strategic Trajectory Abstraction, StraTA）を提案し、エージェント型強化学習（Agentic RL）に明示的な軌跡レベルの戦略（Trajectory-Level Strategy）を導入します。

## 2. Method (手法) — StraTA フレームワーク

StraTA フレームワークは以下の3つの主要成分で構成されます。

1. **戦略サンプリング**: 初期タスク状態からコンパクトな戦略（Compact Strategy）をサンプリング
2. **条件付き行動実行**: サンプリングされた戦略に基づいて後続行動（Subsequent Actions）を条件付け
3. **階層的 GRPO 訓練**: 戦略生成と行動実行を共同訓練

さらに多様な戦略ロールアウト（Diverse Strategy Rollout）と批判的自己判断（Critical Self-Judgment）メカニズムで強化されています。

## 3. Experiments & Results (実験・結果)

ALFWorld、WebShop、SciWorld の3つのベンチマークで評価。StraTA は ALFWorld で 93.1%、WebShop で 84.2% の成功率を達成し、強力なベースラインを一貫して上回ります。SciWorld では総合スコア 63.5% に達し、クローズドソースのフロンティアモデル（Frontier Closed-Source Models）を超えました。

## 4. Conclusion (結論)

明示的な軌跡レベル戦略を導入するシンプルなフレームワークが、エージェント型 RL のサンプル効率と最終性能の両方を一貫して改善することを示しました。階層的な同時訓練が鍵であり、今後のエージェント型 AI 研究に重要な方向性を提供します。
