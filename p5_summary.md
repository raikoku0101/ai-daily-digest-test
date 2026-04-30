**5. Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models**
**著者**: TIDE Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.26951
**upvotes**: 35

**まとめ**:
拡散型 LLM (dLLM) のアーキテクチャをまたいだ知識蒸留フレームワーク TIDE を提案。教師・生徒が異なるアーキテクチャ・注意機構・トークナイザーを持つ場合にも対応する初の統合アプローチ。Tidal (動的蒸留強度調整)・CompDemo (補完的デモンストレーション)・Reverse Calm (異トークナイザー間射影) の 3 モジュールにより、16B MoE 教師から 0.6B 学生へ蒸留し 8 ベンチマーク平均 +1.53 ポイント、HumanEval で同規模自己回帰モデルを +16.48 ポイント上回る性能を実現。
