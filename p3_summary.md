**3. Efficient Training on Multiple Consumer GPUs with RoundPipe**
**著者**: Anonymous et al. (2026)
**arXiv**: https://arxiv.org/abs/2604.27085

**まとめ**:
コンシューマー GPU（RTX 4090 × 8台）でのLLMファインチューニングを阻む「weight binding 問題」を解決する RoundPipe を提案。GPUをステートレスな実行ワーカープールとして扱いラウンドロビン方式で計算ステージを動的割り当て、パイプラインバブルをほぼゼロに削減。1.7B〜32Bモデルで最大2.16倍高速化、単一サーバーでQwen3-235BのLoRAファインチューニングを実現した民主化技術。
