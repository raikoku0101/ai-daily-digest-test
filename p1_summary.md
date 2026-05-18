**1. Hölder Policy Optimisation (ヘルダー方策最適化)**
**著者**: (Hoelder PO Team) et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.12058

**まとめ**:
LLM 強化学習の GRPO において、トークン集約に Hölder 平均を用いる HölderPO を提案。パラメータ p を動的スケジューリング（高→低）することで、早期の稀な信号増幅と後期の訓練安定性を両立。数学推論ベンチマーク平均 54.9%（vs GRPO 51.2%）、エージェント推論 ALFWorld で 93.8%（vs GRPO 72.8%）を達成し、追加計算コストなしで GRPO の集約問題を解決した。
