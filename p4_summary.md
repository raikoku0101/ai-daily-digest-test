**4. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL**
**著者**: Co-RL Authors et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.17253

**まとめ**:
グラウンドトゥルースラベルなしで複数モデルが相互に報酬を与え合う協調型マルチエージェント強化学習(Co-RL)を提案。N個の独立エージェントが同じ未ラベルプロンプトに回答し、ピアの多数決との一致度で報酬を決定する。異なるモデル族（Qwen、Llamaなど）の組み合わせによる誤りの非相関性が鍵で、LLMで3.0〜8.6%、VLMで2.3〜7.2%の性能向上を達成。理論的にも「初期確率の和>1なら両エージェントが正答収束」を証明した。
