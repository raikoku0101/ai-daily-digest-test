**1. How to Fine-Tune a Reasoning Model? — Teacher-Student協調によるSFTデータ合成**
**著者**: (TESSY著者ら) et al. (2026)
**arXiv**: https://arxiv.org/abs/2604.14164

**まとめ**:
推論特化モデル（Qwen3-8Bなど）を強力な教師モデルの合成データでファインチューニングすると、スタイル分布の乖離により推論能力が劣化するという問題を発見。Teacher-Student協調フレームワーク「TESSY」を提案し、教師モデルと生徒モデルを交互に使って生徒スタイルに整合した合成データを生成。コード生成タスクでLiveCodeBench-Pro +11.25%、OJBench +6.68%の大幅改善を達成し、推論モデルのカスタマイズに新たな指針を示した。
