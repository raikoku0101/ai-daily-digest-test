**2. Long Context Pre-Training with Lighthouse Attention**
**著者**: Lighthouse Attention Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.06554

**まとめ**:
超長文脈（512K トークン以上）での Transformer 訓練を効率化する Lighthouse Attention を提案。訓練時のみ使用する階層的選択ベースの注意機構で、Q/K/V を対称プーリングして重要トークンを選定し FlashAttention を実行。530M パラメータの Llama-3 実験で、98K 文脈で 1.4～1.69 倍、512K 文脈ではフォワードパスで 21 倍の高速化を達成しながら、密集 SDPA 復帰後のモデルはベースラインと同等性能を維持することを実証した。
