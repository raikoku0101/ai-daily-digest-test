**4. CAST: Game Solvers as Turn-Level Teachers for LLM Agents**
**著者**: CAST Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2607.25308

**まとめ**:
ゲームソルバーの状態価値変化をターンレベルの教師信号に変換し、LLMエージェント訓練に活用するCASTを提案。ソルバーアドバンテージ（行動前後の状態コスト差分）をasinh圧縮・RMS正規化で安定化してRLVRに統合。ソコバンでDAPOを+17.4pt上回り、ALFWorld・WebShopへのゼロショット転移でも全訓練済み手法を凌駕。DAPOのピーク性能到達に必要な訓練ステップを1.7〜2.0倍削減する訓練効率も実証。
