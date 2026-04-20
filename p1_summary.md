**1. Elucidating the SNR-t Bias of Diffusion Probabilistic Models**
**著者**: （Hugging Face Daily Papers掲載）et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.16044

**まとめ**:
拡散確率モデル（DPM）の推論時に発生するSNR-タイムステップ（SNR-t）バイアスを初めて体系的に解明。訓練時と推論時でSNRの対応が崩れる根本原因を数学的に証明し、ウェーブレット領域で周波数成分ごとに補正するDCW（Differential Correction in Wavelet domain）を提案。学習不要・プラグイン可能な軽量手法でFIDを最大42.6%削減し、FLUX等の最新モデルでも画質改善を確認。
