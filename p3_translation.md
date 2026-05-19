## 1. Introduction (はじめに)
現在のオーディオ生成手法は圧縮された潜在空間 (latent space) に依存しており、中間表現による情報損失とパイプラインの複雑性増加という課題があります。本論文は raw waveform space で直接高忠実度オーディオを生成する WavFlow を提案。主な課題は生波形の高次元性・振幅のばらつき・データ不足の 3 点で、「waveform patchify」と「振幅リフティング (amplitude lifting)」で解決し、500 万の高品質ビデオ-テキスト-オーディオ三つ組を活用して訓練します。

## 2. Related Work (関連研究)
潜在空間オーディオ生成は連続潜在モデル (AudioLDM、TANGO) と離散コーデックベース合成 (AudioGen、V-AURA) に分かれます。一方、raw 空間モデリングは WaveNet、WaveGrad などで試みられましたが、グローバルセマンティック制御が欠けていました。画像領域での x 予測が「ノイズ予測より学習しやすい」という知見を WavFlow はオーディオに応用します。

## 3. Method (手法)
WavFlow は条件付きフローマッチング (CFM: Conditional Flow Matching) で x 予測を採用。生波形 x を waveform patchify で 2D 格子 (C×D) に変形し、RMS 正規化と振幅スケーリング (3.0 倍) で信号を増幅。MultiModal DiT (MMDiT) バックボーンでビデオ CLIP 特徴量とテキスト埋め込みを結合。推論時は classifier-free guidance で条件付き生成を実現し、waveform unpatchify で 1D 波形に戻します。

## 4. Experiments (実験)
VGGSound (約 500 万件) と AudioCaps (約 100 万件) の大規模データセットで訓練・評価。VGGSound では FD_PaSST 59.98・IS_PANNs 17.40・DeSync 0.44 を達成し MMAudio や HunyuanVideo-Foley を上回る結果。AudioCaps では FD_PANNs 10.63・IS_PANNs 12.62 で最高性能を記録。アブレーション研究でパッチサイズ D=200 が最適であることを確認。

## 5. Conclusion (結論)
WavFlow は波形パッチ化・x 予測フローマッチング・信号前処理を組み合わせることで、中間圧縮が高品質合成の前提条件ではないことを証明。オーディオトークナイザー不要で潜在空間手法と同等以上の性能を達成し、マルチモーダルオーディオ生成の新たなパラダイムを提示。今後は音声・歌唱合成への拡張が課題。
