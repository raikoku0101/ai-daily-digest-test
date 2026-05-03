**3. Efficient Training on Multiple Consumer GPUs with RoundPipe**
**著者**: Anonymous et al. (2026)
**arXiv**: https://arxiv.org/abs/2604.27085

**まとめ**:
消費者向け GPU での LLM ファインチューニングにおける「重みバインディング問題（Weight Binding Issue）」を解決する新パイプラインスケジュール RoundPipe を提案。GPU をステートレス実行ワーカープールとして扱いラウンドロビン動的ディスパッチを実現し、8× RTX 4090 で最先端比 1.48〜2.16 倍の高速化を達成。単一サーバーで Qwen3-235B の LoRA 訓練も実現した。
