## 1. Introduction (はじめに)

テキスト→画像生成（T2I; Text-to-Image）モデルの人間嗜好との整合(alignment)には、報酬モデル(reward model)が不可欠である。既存のBradley-Terry型報酬モデルは「大規模な人間嗜好コーパス(preference corpus)で訓練されるため、訓練コストが高く、適応が困難で評価基準が不透明」という課題を抱えている。本研究では、ビジョン言語モデル（VLM; Vision-Language Model）を用いた明示的ルーブリック(rubric)自動合成フレームワークを提案し、解釈可能で効率的な報酬信号生成を目指す。

## 2. Method (手法)

AutoRubric-T2Iは以下の流れで機能する。まず嗜好ペア(preference pair)から推論トレース(reasoning trace)を合成し、候補ルーブリック群を生成する。次にVLM判定器(VLM judge)で各ルーブリック下の画像ペアをスコア化し、ペアワイズ(pairwise)なスコア差分を得る。最後にℓ₁正則化ロジスティック回帰精緻化器で「ノイズや冗長なルールを除去し、最も識別力を持つTOP-Nルーブリックを選別」する手法を採用している。

## 3. Experiments & Results (実験と結果)

MMRB2等のベンチマークで、AutoRubric-T2Iは「アノテーション済み嗜好データの0.01%未満で大規模報酬モデル訓練の必要性を大幅に削減」しながら従来手法を上回る性能を実現。さらにFlow-GRPOパイプラインでの拡散モデル(diffusion model)T2Iタスクでも、スカラー報酬モデル(scalar reward model)より生成品質改善を検証した。

## 4. Conclusion (結論)

解釈可能かつ効率的なT2I報酬モデリングの新たな方向性を提示。自動ルーブリック学習(automatic rubric learning)により、従来の大規模データ依存から脱却可能であることが示唆される。特にデータ効率の高さは、新しいT2Iモデルの評価・チューニングに即座に活用できる実用的価値を持つ。
