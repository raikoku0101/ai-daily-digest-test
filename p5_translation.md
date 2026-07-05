## 1. Introduction (はじめに)
長文脈での大規模言語モデル（LLM）の動作理解は重要な課題です。従来手法はアテンションヘッド（Attention Head）が「文字通りコピー（Literal Copy）」する箇所のみを検出していましたが、実際にはモデルは関連文脈の意味を「合成（Synthesis）」して回答を生成します。この非字義的検索（Non-Literal Retrieval）を担うヘッドの特定が、モデルの解釈可能性（Interpretability）向上に不可欠です。

## 2. Method (手法)
LOCOS（Logit-Contribution Scoring）を提案。出力値回路（OV-Circuit: Output-Value Circuit）が最終的にどの方向に寄与するかを測定する手法で、出力値の投射を「答えトークン非埋め込み方向（Answer Token Unembedding Direction）」に対して計算します。「針あり（With-Needle）」と「針なし（Without-Needle）」のソース位置を単一フォワードパスで対比させることで、従来手法が見逃す「書く」メカニズムも評価します。

## 3. Experiments & Results (実験・結果)
Qwen3・Gemma-3・OLMo-3.1 の 3 モデルファミリーで検証。NoLiMa 非字義的検索ベンチマークで「上位ヘッドの平均除外（Mean Ablation）」実験を実施。Qwen3-8B では 50 ヘッド除外時に ROUGE-L が 0.401 から 0.000 に低下（既存手法は 0.292 を維持）。MuSiQue（0.55→0.08）・BABI-Long（0.62→0.20）でも大幅な低下を確認。ランダムヘッド除外の対照群は基準値から 0.05 内に留まりました。

## 4. Conclusion (結論)
LOCOS は出力値の寄与を直接測定することで、従来手法が見逃す非字義的検索ヘッドを高精度に特定します。LLM の長文脈処理メカニズムの解釈可能性を大きく前進させ、モデルの安全性評価・機能編集への応用が期待される重要な基礎研究です。
