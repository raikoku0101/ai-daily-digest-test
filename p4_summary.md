**4. AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment**
**著者**: (Anonymous et al.) (2025)
**arXiv**: https://arxiv.org/abs/2605.17602

**まとめ**:
T2I生成モデルの人間選好アラインメントに用いられる報酬モデルの不透明性・高コスト問題を解決する AutoRubric-T2I を提案。VLM ジャッジ向けの評価基準（ルーブリック）を選好ペアから自動合成し、ℓ₁正則化ロジスティック回帰で識別力の高い Top-N を選択。アノテーションデータの 0.01% 未満で、MMRB2 ベンチマークで強力なベースラインを上回る性能を達成。解釈可能な報酬信号でダウンストリームの T2I RL 訓練も改善し、スカラー報酬の欠点を補う新アプローチを確立した。
