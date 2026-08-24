**4. FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving**
**著者**: FlashPrefill V2 チーム (2026)
**arXiv**: https://arxiv.org/abs/2608.19758

**まとめ**:
長文脈 LLM のプリフィル段階を Block-Sparse Attention で高速化する本番対応実装 FlashPrefill V2 を提案。平均補正項による精度維持、ワープ特化・ピンポンパイプライニングによる GPU 最適化、SGLang 等への統合で 128K コンテキストにて FlashAttention-2 比 47.26x の高速化を達成。長文脈 LLM サービングの実運用に直接活用可能。
