**4. One Model, Many Latencies: Universal Speech Enhancement for Diverse Real-Time Applications**
**著者**: NVIDIA Speech Research Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2606.25621

**まとめ**:
リアルタイム音声強化において、アプリごとの異なるレイテンシ要件を1つのモデルで対応する手法を提案。先読みフレーム数の調整でアルゴリズム遅延、early-exit機構で計算遅延を制御。2段階訓練戦略と並列畳み込みで専用モデルと同等の品質を達成し、モデル重みをHugging Faceで公開（nvidia/Real-time_RE-USE）。
