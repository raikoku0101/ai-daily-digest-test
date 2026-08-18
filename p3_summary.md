**3. Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization**
**著者**: Yixuan Wang, Yifei Chen, Haichao Zhang et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.16072

**まとめ**:
複数報酬目標を持つ言語モデルの強化学習では、固定重みの重み付き和で報酬を統合する既存手法では「すでに習熟した目標」に計算資源が無駄に使われる問題があった。SA-MRPOは各報酬目標を独立して標準化し、バッチレベルの飽和度（saturation）推定に基づき動的に貢献度を調整することで、未達成目標への集中的最適化を実現。AIME24で最大5%・AMC23で平均3.8%・コーディングで最大2.3%の性能向上を達成しながら、習熟済み目標のパフォーマンスは維持した。
