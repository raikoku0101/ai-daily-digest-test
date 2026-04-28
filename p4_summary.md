**4. Why Fine-Tuning Encourages Hallucinations and How to Fix It (なぜファインチューニングはハルシネーションを促進するのか、そしてその修正方法)**
**著者**: First Author et al. (2026)
**arXiv**: https://arxiv.org/abs/2604.15574

**まとめ**:
SFT（教師あり微調整）が新しい事実知識を学習させる際、事前学習で獲得した既存知識の忘却（事実的健忘：Factual Forgetting）を引き起こすメカニズムを解明した研究。FFN 層の意味的重複による局所的干渉が主因であることを特定し、①新知識不要な場合の FFN 凍結と②Self-Distillation（自己蒸留）の2つの対策を提案。どちらの手法も既存知識忘却率を約 15% から約 3% に削減しつつ、必要な新知識習得速度は維持する。LLM カスタマイズの信頼性向上に直結する実践的知見を提供。
