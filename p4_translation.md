## 1. はじめに (Introduction)

本論文は、音声と視覚モダリティを融合させる Audio-Visual Intelligence (AVI) の包括的サーベイです。大規模基盤モデル時代において Meta MovieGen や Google Veo-3 といった先進事例が「統合型音声-視覚アーキテクチャ (Unified Audio-Vision Architecture)」の重要性を示しており、マルチモーダル知覚・生成・推論が急速に進展しています。既存研究は断片的な状況にあり、タスク定義・評価方法が不統一のため、本調査で統一的フレームワークを確立します。

## 2. 調査範囲 (Scope / Taxonomy)

本論文が扱う AVI の領域は 3 大カテゴリに分類されます。第一に「理解 (Understanding)」（音声認識・音源位置特定等）、第二に「生成 (Generation)」（映像駆動音声合成・動画から音声生成等）、第三に「インタラクション (Interaction)」（対話・具現化エージェント・マルチモーダルインターフェース等）。24 表 16 図により異なるタスクファミリー間の構造的比較を可能にしています。

## 3. 主要技術 (Key Methods)

中核となる技術方法論は複数層から構成されます。「モダリティトークン化 (Modality Tokenization)」によるモダリティ統一、「クロスモーダル融合 (Cross-Modal Fusion)」による相互理解、自己回帰型および拡散ベース (Diffusion-Based) 生成アーキテクチャ、大規模事前学習・Instruction Alignment・選好最適化 (Preference Optimization) です。

## 4. 主要知見 (Key Findings)

調査から浮上する主要課題は「同期性 (Synchronization)」「空間推論 (Spatial Reasoning)」「制御可能性 (Controllability)」「安全性 (Safety)」の 4 点です。代表的データセットとベンチマークの整理および評価メトリクスの統一提案も行われています。AVI が AI 研究の中心的フロンティアとして位置づけられることが明確になりました。

## 5. 今後の展望 (Future Directions)

同期精度向上・空間的推論能力の拡張・細粒度制御機能の実装・倫理的安全性強化が急務とされています。GitHub リポジトリを公開することで継続的な知識統合と研究コミュニティ全体での方法論共通化が推進されることが期待されます。本論文は AVI 分野の基準文献として機能することを目指しています。
