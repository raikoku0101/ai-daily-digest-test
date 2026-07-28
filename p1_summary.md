**1. Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation**
**著者**: (anonymous et al.) (2025)
**arXiv**: https://arxiv.org/abs/2607.24731

**まとめ**:
On-Policy 蒸留（OPD）と Classifier-Free Guidance（CFG）の組み合わせに潜む「Negative Branch Asymmetry（NBA）」問題を発見・定式化。教師モデルが特権情報（参照画像など）を持つ場合、naïve なマッチングが負の分岐誤差を増大させガイダンス感度が崩壊することを示した。提案手法 PDM（Positive-Direction Matching）により両分岐誤差をゼロに制約し、推論時のスケール変更に対して堅牢な蒸留を実現。動画制御ベンチマークで naïve 手法と比較して MPJPEを約50%改善した。
