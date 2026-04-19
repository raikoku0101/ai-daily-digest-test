## 1. Introduction (はじめに)

OpenAI o1やQwen3など推論モデルは思考過程（thinking）と最終答（final answer）を分離して生成する。大規模教師モデルの合成データでSFTする手法は一般的だが、推論モデルに対しては機能しないケースがある。GPT-OSS-120BをQwen3-8Bの教師として使うと、LiveCodeBench-Proで3.25%、OJBenchで10.02%の性能低下が発生。原因は「文体的相違（style discrepancy）」と「分布の不一致（distribution mismatch）」。

## 2. Method (手法) — TESSSYフレームワーク

提案するTESSY（Teacher–Student Cooperation Data Synthesis）は、教師と学生を交互に使い合成データを生成。「能力トークン（capability tokens）は教師が、文体トークン（style tokens）は学生が生成」という分業が基本思想。交互生成（学生→教師→学生…）、固定トークン数（k=20）ごとに境界予測器（boundary predictor）が切断位置を判定、意図しないトークンを削除。最終答は学生のみが生成。

## 3. Experiments (実験)

教師：GPT-OSS-120B、学生：Qwen3-8B。プログラミング関連80K問題（37K一意）でSFT。評価：LiveCodeBench-V5/V6/Pro、OJBench、AIME、OlympiadBench。比較手法：Teacher-Only、Teacher-Reference、Teacher-Score、TESSY。

## 4. Results (結果)

TESSSYは全指標で改善。LCB-V5: 55.09%→62.87%（+7.78%）、LCB-Pro: 25.35%→36.69%（+11.34%）、OJBench: 18.75%→25.43%（+6.68%）。Teacher-Only（教師データのみ）は深刻な性能低下を招く対照結果。TESSSYは教師トークンを77.65%含みつつ学生の文体分布との整合性を保持。

## 5. Analysis (分析)

Qwen3-30B-A3Bを学生として使ってもTESSYは有効。DeepSeek-R1やQwen3-235Bなど異なる教師でも一貫した改善。平均トークン数を7,594〜8,938削減して生成効率も向上。PCA可視化でTESSYデータは教師と学生の分布の中間に位置することを確認。

## 6. Conclusion (結論)

推論モデルのファインチューニングにおいて、データ分布の一致性が性能を大きく左右する。TESSSYにより教師の高い推論能力と学生の自然な文体を両立させた合成データ生成が可能になった。今後の課題は、能力・文体境界の正確な識別と、さらに多くのタスク・モデルへの拡張。
