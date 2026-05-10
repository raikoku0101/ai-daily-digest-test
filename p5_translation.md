## 1. はじめに (Introduction)

大規模言語モデル（LLM: Large Language Model）をインタラクティブエージェントとして活用する際、長期的な意思決定の最適化が課題です。従来の手法は主に反応的なアプローチ（reactive approach）に依存しており、長い軌跡全体における探索（exploration）と信用割当（credit assignment）を弱めるという問題があります。本研究はエージェント強化学習（RL: Reinforcement Learning）に明示的な軌跡レベル戦略（trajectory-level strategy）を導入する新アプローチを提案します。

## 2. 手法 (Method)

戦略的軌跡抽象化（StraTA: Strategic Trajectory Abstraction）は、初期タスク状態からコンパクトな戦略をサンプリングし、その戦略に基づいて後続アクションを条件付けるフレームワークです。階層的GRPO（Group Relative Policy Optimization）スタイルのロールアウト設計を採用し、多様な戦略ロールアウトと批判的自己判断（self-critique）によって強化されます。戦略生成とアクション実行を共同訓練することでより効果的な意思決定を実現します。

## 3. 実験・結果 (Experiments/Results)

ALFWorld・WebShop・SciWorldの3ベンチマークで評価しました。StraTA はサンプル効率（sample efficiency）と最終パフォーマンスの両面で強いベースラインを上回ります。具体的にはALFWorldで93.1%・WebShopで84.2%の成功率、SciWorldで63.5%の総合スコアを達成し、最先端の閉鎖型モデル（closed-source model）を上回りました。

## 4. 結論 (Conclusion)

StraTA は言語モデルベースエージェントにおいて軌跡レベル戦略を明示的に統合することで、長期的意思決定タスクの性能を大幅に向上させます。複数の標準ベンチマークで一貫した改善を実現し、次世代エージェント学習（agentic learning）の指針となる可能性を示しています。
