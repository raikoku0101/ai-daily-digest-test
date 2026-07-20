**4. xHC: Expanded Hyper-Connections**
**著者**: Anonymous et al. (2026)
**arXiv**: https://arxiv.org/abs/2607.14530

**まとめ**:
Transformer の残差ストリーム（residual stream）を N 本の並列ストリームに拡張する Hyper-Connections を、N>4 でも有効にする xHC を提案。多スケール因果畳み込みによる時間的特徴拡張と、k=4 のみの疎更新により情報・計算ボトルネックを解消。18B/28B MoE モデルでバニラ比 +4 ポイント超の改善を、FLOPs 増加わずか 4% で実現し、「展開率（expansion）」という新しいスケーリング軸の実用性を確立した。
