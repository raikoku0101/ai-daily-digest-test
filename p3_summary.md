**3. Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering**
**著者**: Flash-GMM Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2606.10896

**まとめ**:
GPU上でガウス混合モデル (GMM) を大規模処理するための融合 Triton カーネル Flash-GMM を提案。N×K 次元の責任行列 (responsibility matrix) の GPU メモリ展開を不要にし、O(KD) メモリで動作することで既存実装比 20 倍高速化・100 倍大規模なデータセット処理を実現。ANN (近似最近傍探索) の IVF 索引に統合し、責任値ベースの多重割り当てにより同一計算予算で最大 1.7 倍の効率改善を達成した。
