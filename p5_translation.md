## 1. Introduction (はじめに)
既存のドキュメントOCR（光学文字認識）技術は平文やMarkdownを主対象としており、科学出版に不可欠なLaTeXの構造的・実行可能な特性を失っている。本研究は科学PDFのページレベルからコンパイル可能なLaTeX形式への再構成に焦点を当て、TexOCR-Bench（ベンチマーク）とTexOCR-Train（大規模訓練コーパス）を構築し、専用モデルを提案する。

## 2. Method (手法)
TexOCRモデルは2Bパラメータ規模で、教師あり微調整（SFT: Supervised Fine-Tuning）と強化学習（RL: Reinforcement Learning）を組み合わせて訓練。LaTeXユニットテストから導出される検証可能な報酬を使用し、compilability（コンパイル可能性）とreferential integrity（参照整合性）を直接的に強制する。RLベースのアプローチがSFT単独より構造的・コンパイル関連メトリクスで優れている。

## 3. Experiments & Results (実験と結果)
TexOCR-Benchで21の最先端モデルを多次元評価。既存システムはconsistent section structure（一貫した見出し構造）、correct float placement（正確な図表配置）、valid label-reference links（有効なラベル参照リンク）などの重要な不変条件を頻繁に違反することが判明。TexOCRはこれらの指標で既存OCRシステムとLLMベースのアプローチを上回る。

## 4. Conclusion (結論)
科学文書のデジタルアーカイブ・アクセシビリティ向上に貢献するTexOCRフレームワークを提案。コンパイル可能性と参照整合性を評価軸に取り入れたTexOCR-Benchは、将来の文書理解研究のための標準的評価環境として機能する。LaTeX編集支援ツールや学術データベース構築への応用が期待される。
