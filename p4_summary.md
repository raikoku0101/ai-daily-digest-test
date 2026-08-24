**4. FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving**
**著者**: FlashPrefill V2 Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.19758

**まとめ**:
長文脈LLM推論のプリフィル段階を高速化するブロックスパースアテンション実装「FlashPrefill V2」を提案。平均補正・ワープ特化・ページングKVキャッシュ対応の3つの改良により、NVIDIA H20 GPUで128Kコンテキスト時にFlashAttention-2比最大47.26倍の高速化を実現した。
