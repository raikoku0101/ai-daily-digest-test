**4. MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning**
**著者**: Ionut-Vlad Modoranu, Mher Safaryan, Dan Alistarh (2026)
**arXiv**: https://arxiv.org/abs/2605.07850

**まとめ**:
従来 LoRA の「固定ランク設定」問題を解決するため、対角スケーリング行列 P を挿入することで全ランクレベルで勾配情報を均等に伝播させる MatryoshkaLoRA を提案。マトリョーシカ人形のように階層的にネストされた低ランク表現を一度の学習で習得し、推論時に動的ランク選択ができる。新評価指標 AURAC（ランク精度曲線下面積）で既存ランク適応手法を上回る精度を達成。
