**1. GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning**
**著者**: GradCuit Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2608.02585

**まとめ**:
LLMのパラメータを凍結したままTransformer中間層に最適化可能な潜在状態を挿入し、報酬加重勾配で直接更新するテスト時最適化手法。因果自己注意による「circuit-like gradient flow」により、離散トークンを介さない直接的なクレジット割当を実現。5種類のバックボーンモデル×3ベンチマークで平均64.5%の精度を達成し、Chain-of-Thoughtを6.6ポイント上回る。解釈可能性分析では「because」「therefore」等の推論接続詞が最大の勾配強度を持つことも判明。
