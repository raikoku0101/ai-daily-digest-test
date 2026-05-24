**1. SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers**
**著者**: Yurui Zhu et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.22668

**まとめ**:
Diffusion Transformer (DiT) が学習解像度を超えた高解像度画像生成で性能低下する問題を解決する訓練不要手法 SEGA を提案。各デノイジングステップで潜在表現のスペクトル構造を解析し、RoPE コンポーネントごとに動的に注意スケーリングを調整することで、グローバル構造の保持と細部の忠実度を同時に実現。複数の高解像度設定でSOTAの訓練不要ベースラインを上回り、4096²以上の超高解像度生成でも安定した品質を達成した。
