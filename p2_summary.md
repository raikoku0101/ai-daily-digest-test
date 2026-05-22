**2. Long Context Pre-Training with Lighthouse Attention**
**著者**: Anonymous et al. (2026)
**arXiv**: https://arxiv.org/abs/2605.06554

**まとめ**:
超長文脈（128K〜1M+トークン）学習の二乗計算コストをボトルネックとする問題に対し、学習専用の階層的選択型注意「Lighthouse Attention」を提案。対称Q/K/Vプーリングとカーネル外部でのtop-k選択により、530Mモデル・98Kトークン長で標準SDPAより1.4〜1.7倍高速化し、同等品質を達成。推論時はそのまま標準SDPAに戻せる。
