## 1. Introduction (はじめに)
既存のビデオモーション転送(video motion transfer)は固定された構造的対応に依存しており、参照対象と対象物の形態が大きく異なる場合に機能しない。本研究は「Motion Beyond Morphology」という視点を導入し、異なる形態間で意味のある動的特性(dynamic properties)を適応的に保持するアプローチを提案する。スケルトン抽出(skeleton extraction)や軌跡指定なしに、参照動画から直接転送できる。

## 2. Related Work (関連研究)
従来の構造条件付きアニメーション(pose-guided methods)は人間や特定の構造を持つキャラクターに限定されている。最近の参照ベース手法(MotionClone、DisMo等)は暗黙的特徴抽出を用いるが、ソース固有の情報を保持する傾向がある。複数の運動表現(軌跡・トラッキング・ポーズ)はそれぞれ補完的な強みを持つ。

## 3. Method (手法)
**Stage I: Abstract Motion Bootstrapping**
意味的運動学(semantic kinematics)、深度対応グローバル軌跡(depth-aware global trajectories)、密度点トラック(dense point tracks)、6-DoF軸、エッジの5種の多粒度運動ビューを統一インターフェースで学習。抽出した運動条件を異なるカテゴリーの対象条件と組み合わせ、動的特性を共有するクロスカテゴリーペアを生成。「motion fidelity」「target fidelity」「reference leakage」「video quality」の4基準でフィルタリング。

**Stage II: Cross-Category Motion Internalization**
Stage Iの明示的運動条件を生参照動画に置き換え、クロスカテゴリーペアで訓練することで形態固有のショートカットを回避し、転送可能な動力学(transferable dynamics)を内在化させる。

## 4. Experiments (実験)
OpenVMT-Dataset(10K動画ペア)とOpenVMT-Bench(Same/Near/Far分割)を導入。I2V(Image-to-Video)とT2V(Text-to-Video)の両設定で評価。DisMo、Wan-Move、Tora等の最先端手法と比較。

## 5. Results (結果)
全指標でSOTA達成。「HMF(Hybrid Motion Fidelity)」全カテゴリーで最高スコア。「G-Mot.」でI2V/T2V共に最高値。人的評価でI2V 93.0%、T2V 97.3%の選好率。ソース漏洩(source leakage)を最小化しながら運動忠実性と対象保持のバランスを実現。

## 6. Conclusion (結論)
2段階フレームワークにより、多粒度運動抽象化をクロスカテゴリー監督構築に活用し、直接ビデオ条件付き転送に内在化。形態的対応を超えたオープンカテゴリーモーション転送を実現した。
