**2. Long Context Pre-Training with Lighthouse Attention**
**著者**: Lighthouse Attention Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.06554

**まとめ**:
128K〜1Mトークン超の長文脈学習における二次的なアテンション計算コスト問題を解決するため、Lighthouse Attentionを提案。対称なQ/K/Vピラミッド池化・パラメータ不要のℓ2ノルムスコアリング・FlashAttention再利用という3つの設計原則により、学習専用の線形計算量アテンションを実現。学習後半で通常のSDPAに復帰する2段階訓練で、512Kコンテキストで17〜21倍の高速化と1.4〜1.7倍の総学習時間短縮を達成。
