## 1. Introduction (はじめに)
大規模言語モデル（LLM）エージェントによるコード生成の課題に取り組んでいます。既存システムの多くは「定義済みリポジトリアーキテクチャ」を前提としていますが、実務的なゼロスタート開発では、自然言語要件から完全なソフトウェアプロジェクトを構築する必要があります。この課題に対応するため、Repo0フレームワークが提案されています。

## 2. Method (手法)
**Dual-DAG（二重有向非環グラフ / Dual Directed Acyclic Graph）アーキテクチャ**が中核となります。「要件レベルDAG（Requirement-level DAG）」と「コンポーネントレベルDAG（Component-level DAG）」で構成され、両者の対応関係を明示的に管理します。モジュール性指標（Modularity Metrics）に基づき構造的アクションを実行し、構造的収束（Structural Convergence）に達するまで反復。収束後、テスト駆動開発（TDD）ガイドでコード生成が進められます。

## 3. Experiments & Results (実験と結果)
RepoCraftの6つの実世界リポジトリ（GPT-4.5 miniおよびDeepSeek V3.2使用）で評価。機能カバレッジ（Functionality Coverage）とパス率（Pass Rate）の両指標で最高性能を達成。最強ベースライン（RPG）と比較し、機能カバレッジで20.08ポイント、パス率で29.74ポイント改善しました。

## 4. Conclusion (結論)
アブレーション分析（Ablation Analysis）および構造進化分析により、Dual-DAGアーキテクチャ状態、モジュール性ガイド構造進化、明示的な構造収束の重要性が実証されました。コードとデータはGitHubで公開されています。
