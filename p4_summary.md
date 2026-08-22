**4. FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving**
**著者**: FlashPrefill V2 Authors et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.19758

**まとめ**:
LLMの長文脈プリフィル計算のボトルネックを解決するブロックスパースアテンション手法のV2。平均補正項の追加・疎行列アテンション演算子の再設計・SGLang等推論フレームワーク統合を実現。NVIDIA H20で128K文脈長においてFlashAttention-2比FP8で47.26倍、BF16で27.19倍のスピードアップを達成し、実用的な長文脈サービングを大幅に改善する。
