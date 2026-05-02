**5. Leveraging Verifier-Based Reinforcement Learning in Image Editing**
**著者**: Hanzhong Guo, Jie Wu, Jie Liu et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.27505

**まとめ**:
RLHF がテキスト→画像生成で成功した一方、画像編集への適用は未探索だった主因「バイアスある全体スコア型報酬モデル」を克服するため、推論型検証器（Verifier）を用いた RL フレームワーク「Edit-R1」を提案。Chain-of-Thought を活用した報酬モデルが編集画像を個別原則ごとに評価し、グループ対照的選好最適化（Group Contrastive Preference Optimization）という RL 手法と人間のペアワイズ選好データを組み合わせて学習する。FLUX.1 などの最先端編集モデルの性能を大幅に改善し、スケーラブルな自動検証器による画像編集改善の有効性を実証した。
