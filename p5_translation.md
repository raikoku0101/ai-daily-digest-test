## 1. Introduction (はじめに)
既存の MLLM（Multimodal Large Language Model）は狭い視野角の透視図法（Perspective）画像に限定されている。360°パノラマセンシングは周囲環境全体を一度に捉えることでナビゲーション・ロボット探索・3D シーン理解に新たな可能性を提供する。ERP（正距円筒図法: Equirectangular Projection）パノラマを連続した観察者中心空間として推論する「pano-native 理解」を提案。既存手法がパノラマを複数の透視図に分解する問題に対して、直接的で効率的なパノラマ表現からの推論を実現する統一的フレームワーク PanoWorld を構築。

## 2. Method (手法)
pano-native 理解を 4 つの能力ファミリーに分解：①意味的アンカリング（何が存在するか）、②球面定位（Spherical Localization：観察者中心座標系での位置）、③参照フレーム変換（Referential Frame Transformation：回転・再配向での関係変化）、④深度対応 3D 空間推論（Depth-Aware 3D Spatial Reasoning）。570K の ERP パノラマから幾何認識型・言語接地型・深度対応のメタデータを構築する大規模パイプラインを開発。モデルアーキテクチャでは球面空間クロスアテンション（SSCA: Spherical Spatial Cross-Attention）を導入し、視覚トークンが球面方向情報から幾何情報を取得できる仕組みを実装。

## 3. Experiments (実験)
提案の PanoSpace-Bench での評価：PanoWorld が基盤モデルから精度 30.8 → 56.5 へ大幅向上、絶対方向定位で 93.7・BFOV mIoU で 73.3 を達成。H*Bench（人間中心視覚探索）への転移では従来の透視図法手法より優位性を示す。VLN（Vision-Language Navigation）ベンチマーク R2R-CE でも最先端性能（SPL 52.1）を実現。アブレーション研究で能力別訓練データ・検証モジュール・アーキテクチャ各要素の必要性を確認。

## 4. Conclusion (結論)
ERP パノラマを連続的な観察者中心空間として推論する能力構造化フレームワークを確立。大規模検証済みメタデータ・能力整合型指示チューニングデータ（Capability-Aligned Instruction Tuning）・球面幾何認識モデルアダプテーションを組み合わせることで既存手法を大幅に上回るパノラマ理解を実現。完全視野角環境における空間推論の新たな研究方向を示唆する。ロボット自律走行・VR/AR・屋内ナビゲーションへの応用が期待される。
