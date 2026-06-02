**2. Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding**
**著者**: Jianuo Huang et al. (2026)
**arXiv**: https://arxiv.org/abs/2605.29707

**まとめ**:
投機的デコーディング（Speculative Decoding）の自己回帰ドラフターが持つ「品質は高いが遅い」問題を解決するため、因果モデリングとドラフト生成を分離するDominoフレームワークを提案。並列ドラフトバックボーンで予備分布を生成し、軽量Domino headで因果精緻化を行うことで、Qwen3モデルにてTransformersで最大5.49倍、SGLangで最大5.8倍のスループット改善を達成した。
