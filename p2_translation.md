## 1. Introduction (はじめに)

ヒューマノイドロボットの制御システムは近年大きな進歩を遂げていますが、「ロボット、環境、タスク関連オブジェクト間の豊かな相互作用（interaction-rich behavior）をモデル化すること」が根本的な課題として残っています。従来の教師あり学習（supervised learning）では、空間コンテキスト（spatial context）・時間力学（temporal dynamics）・ロボット動作（robot actions）・タスク意図（task intent）を大規模かつ同時に捉えることが困難です。ExoActorはこの課題を根本から解決する新しいフレームワークとして提案されました。

## 2. Method (手法)

ExoActorの核心となるアイデアは、三人称（外部視点、exocentric）映像生成を相互作用力学（interaction dynamics）のモデリング統一インターフェースとして使用することです。大規模映像生成モデル（large-scale video generation model）の汎化能力を活用し、タスク指示とシーン文脈から、ロボット・環境・オブジェクト間の協調相互作用を暗黙的に符号化した実行プロセスを合成します。生成された映像から人間モーション推定（human motion estimation）を行い、汎用モーションコントローラ（general motion controller）で実行可能なヒューマノイド行動列（humanoid action sequence）に変換します。

## 3. Experiments & Results (実験と結果)

ExoActorは新しいシナリオへの汎化性能（generalization performance）を実証しています。追加の実世界データ収集（real-world data collection）なしに、未見の相互作用シナリオへの適応能力を検証。従来のヒューマノイド制御手法と比較して、インタラクション豊かなタスクでの汎化精度が大幅に向上しています。映像生成モデルが持つ世界の物理的動力学に関する暗黙知識が、制御への転移を可能にしています。

## 4. Conclusion (結論)

ExoActorは「相互作用豊かなヒューマノイド行動をモデル化するスケーラブルなアプローチ」を提供し、大規模生成モデル（large-scale generative model）が汎用ヒューマノイド知能（generalizable humanoid intelligence）の進展を促進する新しい道を開きます。映像生成とロボット制御の統合という新パラダイムは、今後のエンボディドAI（embodied AI）研究の方向性を示す重要な成果です。
