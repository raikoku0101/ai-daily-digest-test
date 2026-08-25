**5. Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit LLMs**
**著者**: GPT-OSS Research Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.20953

**まとめ**:
構造的圧縮後にMXFP4量子化されたLLMを、従来のQATより約7倍高速に回復する新手法 QAH（Quantization-Aware Healing）を提案。圧縮後チェックポイントではなく元の非圧縮モデルから直接蒸留することで、学生モデルの精度天井を打破。60Bモデルが9ベンチマーク中7つでbfloat16版に匹敵し、LiveCodeBenchでは120B教師と同等の性能66.5点を達成した。
