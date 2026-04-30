**2. Large Language Models Explore by Latent Distilling**
**著者**: ESamp Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.24927
**upvotes**: 52

**まとめ**:
標準的な確率的サンプリングが語彙レベルの変動にとどまる問題に対し、Exploratory Sampling (ESamp) を提案。軽量な潜在蒸留器 (Latent Distiller) をテスト時にオンライン学習させ、LLM の浅層→深層隠れ表現の写像予測誤差を「意味的新規性 (Semantic Novelty)」として活用。並列生成間で蒸留器を共有することで協調的な意味領域の分散探索を実現し、サンプリング予算を大幅削減しながら推理・コード生成・創作文章で性能向上を達成。
