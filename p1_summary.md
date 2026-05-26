**1. ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention**
**著者**: ThriftAttention Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.23081
**upvotes**: 28

**まとめ**:
Blackwell GPU の FP4（4ビット）テンソルコアを活用しながら、重要な Attention ブロックのみを選択的に FP16 で処理する「混合精度 Attention」手法を提案。FP4 ブロックの僅か 5% を FP16 で処理するだけで、FP4→FP16 の性能差の 89.1% を回復し、エンドツーエンドで最大 2 倍の推論高速化を達成。長文コンテキスト LLM 推論の実用的な高速化手法として即座に応用可能。
