## 1. Introduction (はじめに)

CLI（コマンドラインインターフェース）ベースのソフトウェアエンジニアリングエージェントは急速に発展していますが、「OpenHands 環境での学習データに過度に依存している」という問題に直面しています。モデルは学習時の枠組み（スキャフォールド、scaffold）では高性能を示すものの、異なる環境への転用時に著しく性能が低下します。基盤モデル（foundation model）ではこの低下が見られないことから、微調整（fine-tuning）がスキャフォールド固有の振る舞いに依存していることが示唆されています。

## 2. Method (手法)

提案手法 DCAS は、バックエンド置換傍受層（backend-substitution interception layer）として機能し、API 通信をスキャフォールドとモデルバックエンド間でルーティングします。計画構造（planning structure）を二つの側面から分析：明示的計画（explicit planning：実行前に生成される計画アーティファクト）と暗黙的計画（implicit planning：エージェントループ全体の構造的規約）。スキャフォールド修正なしにクロススキャフォールド評価と計画対応の軌跡収集（trajectory collection）を実現します。

## 3. Experiments (実験)

制御された計画源介入実験（controlled planning-source intervention experiments）により、計画品質が高いレバレッジ効果を持つことを確認。単一スキャフォールドの小規模 DCAS 収集データで微調整したモデルは、「非学習スキャフォールドでも一貫した性能向上」を達成します。計画の二つの側面は学習データ内で経験的に分離可能（empirically separable）であることが実証されました。

## 4. Conclusion (結論)

スキャフォールド間の性能低下の根本原因が計画構造にあることを示し、計画を固定されたアーティファクトから学習可能なモデル能力（learnable model capability）へ移行することの重要性を提示。この知見は AI エージェント開発における汎用性向上に広く貢献する可能性があります。
