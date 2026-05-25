**1. Rethinking Cross-Layer Information Routing in Diffusion Transformers**
**著者**: Anonymous et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.20708

**まとめ**:
Diffusion Transformer（DiT）の残差接続が引き起こす「前向きマグニチュード膨張」「後向き勾配減衰」「ブロック間冗長性」の3問題を体系的に分析。学習可能・タイムステップ適応型の非逐次集約を行うDiffusion-Adaptive Routing（DAR）を提案し、ImageNet 256×256でFIDを9.67→7.56に改善、学習収束を8.75倍高速化。REPAと組み合わせると初期段階で2倍の学習加速を実現し、既存手法と直交するアーキテクチャ改善軸を提示。
