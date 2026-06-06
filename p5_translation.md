## 1. Introduction (はじめに)
VLA（Vision-Language-Action）モデルにおける「知覚と行動の構造的ミスマッチ」という根本的課題に取り組む。VLM は言語と視覚を意味空間で整列させるが、ロボット操作は 3 次元物理空間に存在するためエンドツーエンドのマッピングは困難。AffordanceVLA はアフォーダンス（Affordance）という構造化された中間表現を導入し、何を操作するか・どこで操作するか・どのように操作するかを段階的に予測することでこの乖離を解決する。

## 2. Related Work (関連研究)
既存 VLA 研究は2つの系統に分かれる。第一は動画予測やビジュアルフォーサイト（Visual Foresight）を中間表現とする方法で、冗長性が高く計算コストが大きい。第二は構造化された低次元表現（テキスト推論、キーポーズなど）を用いるアプローチ。本研究はアフォーダンスを「空間的に接地され、意味的に条件付けられ、行動に結合した」中間表現として位置づけ、VLM 内部に内在化される点が特徴。

## 3. Method (手法)
AffordanceVLA は Mixture-of-Transformer（MoT）アーキテクチャ上に3つの専門化エキスパートを配置：
- Understanding Expert: 視覚と言語の融合による命令認識表現を生成
- Affordance Generation Expert: Which2Act（対象物体の視覚潜在表現）・Where2Act（2 次元相互作用位置特定）・How2Act（3 次元幾何推論）を並列予測
- Action Expert: 接地されたアフォーダンス表現に基づき制御行動を生成
UAA（Understanding–Affordance–Action）進行的注意機構により各エキスパート間の情報流を制御。

## 4. Training Strategy (訓練戦略)
三段階の進行的課程（Progressive Curriculum）：
Stage I: VQA データセット（AGD20K、RefSpatial、PRISM）上で汎用アフォーダンス基盤を習得
Stage II: 大規模合成ロボット操作データ（InternData-A1）との共訓練。LLM による指示分解 + VLM によるキーフレーム注釈で 100,000 以上の高品質ラベルを自動生成
Stage III: 下流タスク（LIBERO、CALVIN、実世界）への適応的微調整

## 5. Experiment (実験)
シミュレーション評価：
- LIBERO: 95.8% の平均成功率を達成
- CALVIN ABC→D: 5 連続タスク完了率 75.9%（平均鎖長 4.33）
実世界実験：基本タスク 88.3% 平均成功率。複雑タスク（引き出し、トースター）では Pi0（44.8%）に対し 82.9% を達成。

## 6. Key Findings (主要知見)
データスケーリング単独では空間的ギャップを埋められず、構造化された中間表現が本質的。全データの 40% で提案法が Pi0 のフルデータ性能を超過。三専門家の分離と段階的注意機構により「表現崩壊（Representation Collapse）」を防止。Stage II の大規模共訓練が OOD 一般化を大幅改善（CALVIN: 3.81→4.33）。

## 7. Conclusion (結論)
AffordanceVLA はアフォーダンスを内在化された中間表現として活用することで、VLM の意味空間と 3 次元物理制御の構造的ミスマッチを解決する。複雑な実世界タスク（特に長期視野型実行と命令感度）における堅牢性向上が実証された。
