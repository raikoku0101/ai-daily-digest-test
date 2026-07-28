**2. Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification**
**著者**: Haopeng Li, Yitong Li, Junsong Chen et al. (2025)
**arXiv**: https://arxiv.org/abs/2607.24027

**まとめ**:
拡散トランスフォーマーによる動画生成で長いトークン列がアテンション計算のボトルネックとなる問題に対し、トレーニング不要な動的スパースアテンション手法 Sol-Attn を提案。オンライン・ソフトマックスパスでのブロック閾値処理とプロキシスコアの再利用により、動的予算制御と高精度な近似を両立。動画生成で2.1倍、編集タスクで2.3倍の高速化を達成しながら視覚品質を維持した。
