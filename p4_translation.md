## 1. Introduction (はじめに)

ピクセル空間連続トークン自己回帰(AR)生成は、離散トークン化や事前学習済みトークナイザーを不要にします。しかし高次元パッチ生成による単一ステップの大きな誤差と、教師強制訓練(Teacher-Forced Training)における訓練推論ギャップ(Train-Inference Gap)が課題です。既存手法(x予測やノイズ注入)は部分的な改善に留まります。本研究は「Parallel Rollout Approximation (PRA)」を提案し、これら 2 つの課題に統合的に対処します。

## 2. Related Work (関連研究)

自己回帰画像生成には離散化トークンを用いた VQ-VAE 系手法と連続値生成手法があります。訓練推論ギャップを軽減する試み(x予測・ノイズ注入)が存在しますが、精密なロールアウト訓練は逐次サンプリング(Sequential Sampling)コストが高く実用的でありませんでした。拡散モデル(Diffusion Models)も高品質生成を実現しますが、AR インターフェースとは異なるパラダイムです。

## 3. Method (手法)

PRAは低次元中間状態を生成し、ピクセルデコーダーで「ピクセル空間トークン(Pixel-Space Tokens)」に復元します。推論時と同一の「中間状態→ピクセル経路」を位置独立に並列構築することで、逐次サンプリングなしで推論ライクな学習を実現。"pixel-in, pixel-out AR interface"を保持しながら、教師強制訓練の弱点を克服します。PRA-S (135M) と PRA-L (511M) の 2 スケールを構築。

## 4. Experiments (実験)

ImageNet-1K 256×256 解像度のクラス条件付き生成(Class-Conditional Generation)で評価しました。PRA-S (135M パラメータ) と PRA-L (511M パラメータ) の 2 スケールでの比較実験を実施。同時に ImageNet 分類プローブ精度(Classification Probing Accuracy)も測定し、統合的なピクセル空間理解・生成モデルとしての可能性を探りました。

## 5. Results (結果)

PRA-S は FID 2.58 を達成し、従来のビリオンスケール(Billion-Scale)ピクセル AR 結果 FID 3.60 を上回りました。PRA-L はさらに FID 1.94 を実現し、ピクセル空間 AR モデルの新 SOTA を確立。ImageNet 分類プローブ精度でも他の AR・拡散モデルを上回り、統合的なピクセル空間理解・生成の可能性を示しています。

## 6. Conclusion (結論)

PRA は訓練推論ギャップと高次元誤差という 2 大課題に対して計算効率的な解法を提示しました。低次元中間状態を介する設計により、ビリオン規模モデルを必要とせず数百 M パラメータで SOTA を達成するスケール効率を実現。統一的なピクセル空間理解・生成基盤(Unified Pixel-Space Foundation Model)への道を拓く重要な成果です。
