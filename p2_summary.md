**2. LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget**
**著者**: LongStraw Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2607.14952

**まとめ**:
推論時は100万トークン超のコンテキストが利用可能なのに対し、RL後学習は256K以下に留まるという大きなギャップを解決するフレームワークです。固定GPUバジェット（8基のH20 GPU）で2Mトークン超のRL学習を実現する実行スタックを提案。GRPO（Group Relative Policy Optimization）を用いてメモリ効率と計算効率を両立し、4.46Mポジションまでのストレステストをクリアしています。
