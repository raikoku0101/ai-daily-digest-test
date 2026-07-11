## 1. Introduction (はじめに)
ゼロショット複合行動認識（Zero-Shot Compositional Action Recognition: ZS-CAR）では、学習済みの動詞とオブジェクトを組み合わせて未知の行動を認識する必要がある。しかし、既存モデルは実際の動作パターンではなく「物体駆動型ショートカット（Object-Driven Shortcuts）」—例えば引き出しが映れば「開ける」と推定—に依存してしまい、新しい組み合わせへの汎化が困難となっている。

## 2. Related Work (関連研究)
既存の ZS-CAR 手法は訓練データにおける動詞-オブジェクトの共起パターン（Co-occurrence Patterns）に過度に適応しており、時間的な動詞手がかり（Temporal Verb Cues）を十分に活用していない。この非対称な学習と疎な合成教師信号が、オブジェクト情報への依存を強める主要因。

## 3. Method (手法)
提案手法 RCORE（Robust COmpositional REpresentations）は 2 つのコンポーネントで構成：
(1) **共起事前分布正則化（Co-occurrence Prior Regularization: CPR）**: 未見の組み合わせに明示的な教師信号を追加し、頻繁な共起パターンを困難な負例（Hard Negatives）として扱う。
(2) **合成用時間順序正則化（Temporal Order Regularization for Composition: TORC）**: 時間順序への感度を強制し、時間的に基礎付けられた動詞表現学習（Temporal Verb Grounding）を促進。

## 4. Experiments (実験)
Sth-com および EK100-com データセットを使用して評価。ショートカット依存度を定量化するための新たな診断指標を導入し、既存手法が訓練共起パターンへの過適応と時間的手がかりの軽視を示すことを実証。

## 5. Results (結果)
RCORE はショートカット診断指標を削減し、複合行動認識性能を向上。特に訓練時に見ていない動詞-オブジェクト組み合わせに対して顕著な改善を達成。既存ベースラインと比較して汎化能力が大幅に向上した。

## 6. Conclusion (結論)
物体駆動型ショートカット学習という根本的問題に対し、時間的接地性と明示的な合成教師信号の組み合わせによる実用的解決策を提示。本手法はロボティクス・AR/VR など実世界の行動認識応用での信頼性向上に直接貢献する。
