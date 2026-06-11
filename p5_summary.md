**5. Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency**
**著者**: 著者らの研究グループ (2025)
**arXiv**: https://arxiv.org/abs/2606.07881

**まとめ**:
パイプライン並列学習のバブル（アイドル時間）問題と重み不整合のトレードオフを解消する手法 PACI（Pipeline Asynchronous training with Controlled Inconsistency）を提案。重み保存・予測・グローバル同期なしで、局所勾配累積のみで最大不整合を Δ_max ≤ ⌈(N-1)/a⌉ に有界化。GPT-2 学習で time-to-accuracy を最大 1.69 倍改善しながら品質を維持することを実証した。
