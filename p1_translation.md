## 1. Introduction (はじめに)
MLLMベースのGUIエージェントは急速に進化しているが、実世界タスク完了の根本ボトルネックは「GUI操作に関する世界知識の不足」である。既存の解決法は高コストな多エージェント体制か、SFT/RLなどの事後学習に依存しており、知識は暗黙的にしか吸収されず、軌跡の記憶に留まりがちだった。本論文はGUI-CIDERという中間学習（mid-training）手法を提案し、GUI操作の世界知識を明示的に内部化する。

## 2. Related Work (関連研究)
GUIエージェント研究は要素グラウンディング（element grounding）やタスク完了向上を追求してきたが、「知識ギャップの明示的解決」への対応は限定的だった。中間学習（mid-training）はプリトレーニングとポストトレーニングの橋渡しとして数学・コーディング領域での知識獲得に活用されてきたが、GUIエージェント向けの体系的研究は未成熟だった。

## 3. Method (手法)
GUI-CIDERは3段階で構成される。**データ合成（data synthesis）**: GUIトラジェクトリから静的計画知識（階層的タスク分解）と動的因果知識（状態遷移・意思決定ロジック）を抽出し、エキスパートモデルで知識豊富なサンプルを生成。**事例再選択（exemplar reselection）**: 因果的サリエンシ関数（causal saliency function）と相対密度推定（density estimation）でコーパスをフィルタリング。保有確率関数 g(x) は因果論理トークン数を報酬し意味的冗長性を罰する設計。**中間学習（mid-training）**: 洗練されたコーパスで次トークン予測を実行し、UIの世界知識をモデルパラメータに直接組み込む。

## 4. Experiment (実験)
5つのベンチマーク（AITZ、AndroidControl、GUI-Odyssey、MMBench-GUI L1、GUI Knowledge Bench）で評価。Qwen3-VL-4B/8B をベースモデルとして使用。GUI-CIDER はタスク成功率で平均9.70%の相対改善を達成。

## 5. Results (結果)
中間学習後のポストトレーニング（post-training）でも効果が持続。4Bモデルが中間学習+ポストトレーニング後に8Bモデルを上回る性能を発揮。GUI-CIDER-8Bは全プラットフォーム（Windows/macOS/Linux/iOS/Android/Web）で大規模モデルを上回るスコアを獲得。GUI Knowledge Bench では8Bエージェントがclaude-sonnet-4.5に近い性能（66.51 vs 66.53）に到達。

## 6. Conclusion (結論)
GUI-CIDERは因果的内部化（causal internalization）と密度認識事例再選択（density-aware exemplar reselection）によってGUIエージェントに明示的なワールドナレッジを組み込む効果的フレームワーク。約100Mトークンの合成データセットを提供し、「知識スケーリング（knowledge scaling）」がより有能なGUIエージェント開発への有望な道筋であることを実証した。
