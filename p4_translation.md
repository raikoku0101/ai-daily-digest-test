## 1. Introduction (はじめに)

組織内の異なるデータソース（データベース、ファイル、長文書、マルチメディア）にまたがる自然言語分析を実現するデータエージェントの評価ベンチマーク「DataSpace」を紹介する。既存ベンチマークは構造化クエリ・検索・分析を個別に評価しているが「完全な表形式出力の取得」と「言語横断型の異種ワークスペース統合」という現実的な要件を統一的に扱っていない。DataSpaceは410個のタスク、7,439個の成果物（計15GB）を含み、CSV・JSON・SQLite・Markdown・PDF・動画という6つのモダリティをカバーする。

## 2. Related Work (関連研究)

先行研究は3系統に分類される。(1) Spider・BIRDなど従来のText-to-SQLベンチマークは決定論的評価を提供するが複数ソース統合が限定的。(2) HotpotQA・MMLongBench-Docなどは長文書を扱うが完全な表形式結果を要求しない。(3) DABStep・FDABenchなどはマルチモーダルに対応するが評価方法が一貫していない。DataSpaceはこれらすべての課題を統合して解決する。

## 3. ベンチマーク構築 (Benchmark Construction)

DataSpace-Builderは4段階パイプライン：(1) Cross-Language Transformation：英語Text-SQLインスタンスから質問・データベース・SQLを言語変換。(2) Constraint-Aware Relational Sampling：主キー・外部キー・述語値の制約を満たしつつ行をサンプリング。(3) Modality Routing & Artifact Rendering：各表をルールベースでCSV・JSON・SQLite・Markdown・PDFに割り当て、長文書はLLMが事実根拠付きでセクションを生成、動画はクエリ条件付きで映像を構成。(4) Human Review：11名の専門家が盲検レビュー。

## 4. タスク定式化 (Task Formulation)

入力は自然言語質問 q_i とワークスペース W_i のペア。エージェントはファイル検査・SQL実行・文書抽出・動画理解などのツールを呼び出し、最終的にCSV形式の表形式結果を返す。評価は参照結果と「完全一致」を要求し、部分的正答は許容しない。

## 5. 実験結果 (Experiments)

6モデル（Grok 4.5、GPT-5.6 Sol、Kimi K3等）と5エージェントハーネス（DataSpace-Agent、Smolagents、Claude Code等）を評価。最高精度66.34%（Grok 4.5）で76タスクは全モデルが失敗。同一バックボーク下でハーネス選択により15.36ポイント差。マルチモーダルタスクで全バックボーンが1.8〜14ポイント低下、結合処理で9.7〜19.8ポイント低下を確認。

## 6. 結論 (Conclusion)

DataSpaceは言語横断型・異種ワークスペース上の完全表形式出力を要求する初の統一的ベンチマーク。マルチモーダル統合と結合処理が今後の改善対象として浮上しており、信頼性の高いデータエージェント開発へ向けた基盤を提供する。
