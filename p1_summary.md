**1. Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL**
**著者**: PRISM 研究チーム et al. (2026)
**arXiv**: https://arxiv.org/abs/2604.28123

**まとめ**:
マルチモーダル LLM の標準ポストトレーニング（SFT→RLVR）において SFT が引き起こす分布ドリフト問題を解決する 3 段階パイプライン PRISM を提案。SFT と RLVR の間にブラックボックスオンポリシー蒸留による「事前アライメント」段階を挿入し、知覚・推論フィードバックを分離する MoE 判別器で分布を修正。Qwen3-VL 4B/8B で複数の RL アルゴリズムにわたり平均 +4.4〜+6.0 ポイントの改善を達成。
