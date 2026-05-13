**3. Your Language Model is Its Own Critic (POISE)**
**著者**: et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.07579

**まとめ**:
POISE（Policy Optimization with Internal State Value Estimation）は、PPO の巨大クリティックや GRPO の複数ロールアウトに代わる軽量ベースライン推定手法。ポリシーモデルの順伝播で既に計算済みの隠れ状態（hidden states）とトークンエントロピー統計から報酬を予測するプローブをオンラインで学習する。クロスロールアウト構成により勾配の不偏性を維持しつつ、単一ロールアウトで固定計算バジェット内のプロンプト多様性を向上させ、学習安定化を達成。
