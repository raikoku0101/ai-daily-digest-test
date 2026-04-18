**5. Switch-KD: Vision-Language Modelのための視覚切替知識蒸留**
**著者**: Switch-KD著者ら et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.14629

**まとめ**:
VLM（Vision-Language Model）の大規模モデルを軽量モデルに圧縮する際、視覚と言語モダリティを分離して蒸留する既存手法の限界を解決。学生の視覚出力を教師の言語デコーダに「切り替える」Visual-Switch Distillationと、動的bi-directional logits差分損失（DBiLD）を組み合わせ、0.5Bの学生モデルで3B教師モデルから平均3.6ポイントの性能改善を達成。
