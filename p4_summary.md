**4. GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding**
**著者**: GPTQ-2D Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2607.27042

**まとめ**:
LLM量子化の標準手法GPTQを拡張し、重み行列の左右両側に非特異基底行列を適用する「二辺適応丸め(Two-Sided Adaptive Rounding)」を提案した理論的研究。従来の単辺丸めを二辺に拡張すると計算量が4次(quartic)になるという障壁を、反対角線(anti-diagonal)を並列処理するアルゴリズムで3次(cubic)に削減。従来の4次アルゴリズムと同等の結果を保ちながら計算コストを大幅に削減し、大規模モデルの実用的な量子化への道を拓く。
