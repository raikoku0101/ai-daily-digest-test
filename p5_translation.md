## 1. Introduction (はじめに)

従来のMLLM（Multimodal Large Language Model）は人間の視野に限定された透視投影（Perspective Projection）パラダイムに基づき、空間理解に課題を抱えている。本研究は「360°パノラマセンシングがスーパーセンシング（Spatial Supersensing）の形態を提供する」という仮説を立て、ERP（等距円筒図法, Equirectangular Projection）パノラマを「パノラマネイティブ」に理解するフレームワークPanoWorldを提案する。既存手法がERPを複数の透視図に分解するのに対し、ERPを連続的・観察者中心の空間として直接推論することを目指す。

## 2. Method (手法)

**能力分類体系**: 4つの能力ファミリーを定義:
- **意味的アンカリング（Semantic Anchoring）**: 言語を視覚エンティティに基礎付ける
- **球面グラウンディング（Spherical Grounding）**: ヤー角λ・ピッチ角φで方向を局在化
- **参照フレーム変換（Reference Frame Transformation）**: 観察者回転下での関係推論
- **深度認識3D空間推論（Depth-aware 3D Reasoning）**: 球面観測を3D構造に結合

**大規模メタデータ構築パイプライン**: 570K個のERPパノラマから幾何認識検出メタデータ・言語基礎セマンティクス・深度認識空間メタデータを構造化グラフとして構築。

**Spherical Spatial Cross-Attention（SSCA）**: パッチ埋め込み後に視覚トークンが球面方向トークンをクエリし、球面幾何信号を抽出。ゲート付き残差更新（Gated Residual Update）で融合し、事前学習バックボーンを保持したまま球面幾何を注入。

## 3. Experiments & Results (実験と結果)

Qwen3.5-VLをベースモデルにパノラマネイティブ命令コーパスで微調整。3ベンチマークで評価:

**PanoSpace-Bench（独自ベンチマーク）**: 全体56.5%（ベースラインQwen3.5の30.8%から大幅向上）。絶対方向93.7%、BFOVミーンIoU 73.3%で顕著な改善。

**H*Bench**: ゼロショット転移で56.1%、微調整後70.0%。透視図ベースライン最強手法（38.4%）を大幅に上回る。

**R2R-CE Val-Unseen（視覚ナビゲーション）**: 54.3% Success Rate、52.1% SPL。GridMM（49.0% SR）を5.3ポイント上回りRGB専用手法を超越。

## 4. Conclusion (結論)

パノラマネイティブ空間学習フレームワークPanoWorldを提案。4つの能力ファミリーの定義・570K ERPパノラマの大規模メタデータパイプライン・Spherical Spatial Cross-Attentionにより、複数ベンチマークで有意な改善を実証。360°推論には専用の幾何適応が不可欠であることを確立。今後はパノラマ固有アーキテクチャの標準透視画像タスクへの転用が課題。
