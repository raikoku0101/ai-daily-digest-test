**4. VIA-SD: Verification via Intra-Model Routing for Speculative Decoding**
**著者**: VIA-SD Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2606.12243

**まとめ**:
LLM 推論の高コスト問題に対処する Speculative Decoding (投機的デコーディング) を改善する多段階フレームワーク VIA-SD を提案。既存のバイナリな受理/棄却判定を超え、大規模ベリファイアからイントラモデルルーティング (intra-model routing) で導出したスリムサブモデルを中間検証器として使用。拒否率を 0.10〜0.22 削減し、既存 SD ベースラインより 10〜20% 高速化、非ドラフティングデコーディングと比較して 2.5〜3 倍の加速を達成した。
