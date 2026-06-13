**2. VIA-SD: Verification via Intra-Model Routing for Speculative Decoding**
**著者**: Yuchen Xian, Yang He, Yunqiu Xu, Yi Yang (ICML 2026)
**arXiv**: https://arxiv.org/abs/2606.12243

**まとめ**:
LLM 推論の高速化技術「Speculative Decoding (推測復号)」を多層階層化した新フレームワーク。従来の「受理か全再計算」という二択に代わり、中程度信頼度トークンをスリムなサブモデルでルーティング検証することで拒否率を 0.10〜0.22 削減。追加学習なしで従来の推測復号比 10〜20% 高速化、非推測復号比 2.5〜3 倍の加速を実現。ICML 2026 採択。
