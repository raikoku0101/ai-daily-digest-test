**1. Efficient Pre-Training with Token Superposition**
**著者**: (Meta / 共著者) et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.06546

**まとめ**:
Token-Superposition Training (TST) は LLM 事前学習の効率を根本から改善するドロップイン手法。連続トークンをバッグ化して multi-hot クロスエントロピーで学習する「超位相フェーズ」と標準学習に戻す「回復フェーズ」の2段階構成により、10B A1B MoE モデルで同一ロス条件下の学習時間を最大 2.5 倍短縮。並列化・オプティマイザ・アーキテクチャの変更が不要で既存インフラに即時適用可能な実用性が最大の強み。
