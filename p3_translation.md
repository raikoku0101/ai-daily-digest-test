## 1. はじめに (Introduction)

ゼロショット合成行動認識（Zero-Shot Compositional Action Recognition）は、既知の動詞とオブジェクトの組み合わせから未知の組み合わせを認識する能力を評価するタスクである。しかし現在のモデルは「引き出しを開ける」という行動を認識する際に、動詞「開ける」を時間的な動き（Temporal Evidence）から推論するのではなく、オブジェクト「引き出し」の存在から直接推測するという「ショートカット学習」に依存している。これがゼロショット汎化の大きな障害となっている。

## 2. 手法 (Method)

本研究では RCORE（Robust COmpositional REpresentations）を提案する。主な構成要素は：
- 共起事前確率正則化（Co-occurrence Prior Regularization: CPR）: 動詞とオブジェクトの共起バイアスを明示的にモデル化し、その影響を低減する。
- 時間順序正則化（Temporal Order Regularization: TORC）: モデルが時系列的な動き情報に基づいて動詞を認識するよう促す。
これらの正則化を組み合わせることで、オブジェクト駆動ショートカットへの依存を抑制する。

## 3. 実験・結果 (Experiments/Results)

Something-Something Compositional（Sth-com）および Epic-Kitchens 100 Compositional（EK100-com）の2つのベンチマークで評価。RCORE は従来手法と比較してショートカット診断指標（Shortcut Diagnostic）を削減し、合成的一般化（Compositional Generalization）を改善。未見の動詞-オブジェクト組み合わせの認識精度が向上した。

## 4. まとめ (Conclusion)

本研究は行動認識モデルが「オブジェクトを見て動詞を判断する」という本質的な欠陥を正面から解決しようとする試みである。RCORE により、真に時間的動きから動詞を推論するより堅牢な表現学習が可能になった。視覚言語モデル（Vision-Language Model）の弱点を解消し、実世界の多様な行動認識シナリオへの適用に向けた重要なステップとなる。
