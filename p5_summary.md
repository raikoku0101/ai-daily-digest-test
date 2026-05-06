**5. Video Generation with Predictive Latents**
**著者**: PV-VAE Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2605.02134

**まとめ**:
PV-VAE (Predictive Video VAE) は、動画 VAE の潜在空間に予測的再構成を統合する新手法。ランダムに未来フレームを破棄し、過去観測のみをエンコードしてデコーダが再構成と未来予測を同時実行することで、時間的ダイナミクスを潜在空間に自然に符号化する。UCF101 で 52% の高速化と 34.42 FVD 改善を達成し、光流推定・次フレーム予測・点追跡の下流タスクでも一貫した改善を確認した。
