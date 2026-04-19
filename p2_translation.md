## 1. Introduction (はじめに)

複数入力ビューから効率的に3Dシーンを復元する問題に取り組む。既存のフィードフォワード手法は「ビュー中心の密な予測（view-centric dense prediction）」に依存し、入力ビュー数が増えると表現サイズが急増する。GlobalSplatは「整列第一、復号化後（align-first, decode-after）」という原則でグローバル潜在表現を先に構築。16KガウシアンのみでRealEstate10Kにて28.5 PSNRを達成。

## 2. Related Work (関連研究)

従来の最適化ベース3DGS手法は高品質だが計算コストが高い。ピクセル整列・密なボクセル予測に依存するフィードフォワード手法（DUSt3R、MVSNeRF等）は入力ビュー増加で線形にガウシアン数が増大する問題を抱える。全体的な幾何一貫性（geometric consistency）と表現効率のバランスを同時達成した手法は限定的だった。

## 3. Method (手法)

GlobalSplatの核は双分岐エンコーダアーキテクチャ（dual-branch encoder architecture）。固定サイズ2048個の潜在シーントークン（latent scene tokens）に対し、幾何（位置・スケール・回転・不透明度）と外観（色）を分離処理。複数ビューを反復的注意メカニズム（iterative attention mechanism）で融合。段階的容量カリキュラム（progressive capacity curriculum）で訓練初期は16候補ガウシアンを1個に統合し、徐々に2/4/8個へ展開。表現の肥大化を防ぎながら詳細構造を習得。

## 4. Experiments & Results (実験・結果)

RealEstate10K（屋内映像）とACID（航空映像）で評価。GlobalSplat 16K版は24入力ビューで28.53 PSNR、32K版で29.48 PSNR。Zpressor（393Kガウシアン）など密な手法と競合する品質を維持しながら、ピークGPUメモリ1.79GB、推論時間77.88ms、ディスク容量3.8MBという優れた効率性を実現。

## 5. Conclusion (結論)

グローバル潜在表現への整列を先行させることでビュー中心の冗長性を排除。固定予算のガウシアン集合でも高品質な多視点合成（novel view synthesis）が可能。コンパクト性・推論速度・メモリ効率において新しい実用的到達点を確立し、3DGSベースNVSの効率・品質トレードオフを大幅に改善。
