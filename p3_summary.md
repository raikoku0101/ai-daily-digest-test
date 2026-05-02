**3. Efficient Training on Multiple Consumer GPUs with RoundPipe**
**著者**: Yibin Luo, Shiwei Gao, Huichuan Zheng et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.27085

**まとめ**:
コンシューマーグレード GPU での LLM ファインチューニングを高速化する新パイプラインスケジュール手法「RoundPipe」を提案。既存手法の「重み結合問題（weight-binding problem）」を解消し、GPU をステートレスワーカーのプールとして扱うことでラウンドロビン方式の動的ステージ配分を実現する。8×RTX 4090 サーバーで 1.7B〜32B モデルのファインチューニングを既存比 1.48〜2.16 倍に高速化し、単一サーバーで Qwen3-235B の LoRA ファインチューニングを可能にした。高価なサーバーグレード GPU なしに大規模 LLM の民主的な学習を実現する実用的成果。
