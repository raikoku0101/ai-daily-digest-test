## 1. 問題設定・背景 (Problem Statement & Background)
ゼロショット複合行動認識（ZS-CAR: Zero-Shot Compositional Action Recognition）は、学習時に見たことのない動詞と名詞の組み合わせ（例: 「引き出しを開ける」）を認識するタスクです。現在のモデルは「開ける」という動作を時間的な動きから学習するのではなく、「引き出し」という物体の存在から推測するショートカットに頼っています。

## 2. 物体駆動型ショートカット問題 (Object-Driven Shortcuts)
モデルがラベル付き物体クラスに依存して動詞を予測するメカニズムを詳細に分析。「引き出し」が映っていれば「開ける」と予測、「コップ」があれば「飲む」と予測するパターンが確認されました。これは真の行動理解ではなく統計的相関への依存であり、未知の組み合わせへの一般化を妨げます。

## 3. 提案手法: RCORE (Robust COmpositional REpresentations)
RCOREは2つの主要コンポーネントから構成されます:
- **CPR (Co-occurrence Prior Regularization)**: 動詞-名詞共起の事前確率バイアスを明示的に正則化し、未知の組み合わせへの教師信号を提供
- **TORC (Temporal Order Regularization for Composition)**: 時間順序感度を強化し、物体の存在ではなく時間的動きパターンから動詞を学習

## 4. 実験・結果 (Experiments & Results)
Sth-com（Something-Something Compositional）とEK100-com（EPIC-Kitchens 100 Compositional）の2つのベンチマークデータセットで検証。既存手法と比較して複合一般化性能が大幅向上し、特に未知の動詞-名詞組み合わせでの認識精度が改善されました。

## 5. 応用と展望 (Applications & Future Work)
ロボット操作・家事支援AI・産業監視システムへの直接応用が期待されます。物体依存バイアスの除去は他のビジョンタスクへの応用可能性も示唆しており、今後は多様なデータセットでの汎化性検証が課題です。
