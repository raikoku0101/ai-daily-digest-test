## 1. はじめに（Introduction）
大規模言語モデル（LLM）エージェントによるコード生成の課題に取り組む。既存システムの多くは「あらかじめ定義されたリポジトリ構造」を前提とするが、ゼロからの開発では自然言語要件から完全なソフトウェアプロジェクトを構築しながらモジュラーなアーキテクチャを維持する必要がある。この「zero-to-all」シナリオの基本的矛盾を解決することが研究動機となっている。

## 2. 手法（Method）
Repo0は「継続的構造進化フレームワーク（continuous structure evolution framework）」として機能。中核は**Dual-DAG（Dual-Directed-Acyclic-Graph）**で、要件レベルのDAGとコンポーネントレベルのDAG、およびそれらの対応関係で構成。モジュラリティ（modularity）指標に基づいた構造アクションを通じて、構造的収束（structural convergence）に達するまでコンポーネント境界を反復的に進化させ、その後テスト駆動開発（TDD: Test-Driven Development）によるコード生成を実行する。

## 3. 実験と結果（Experiments & Results）
6つの実世界リポジトリを対象にGPT-5 miniとDeepSeek V3.2で評価。Repo0は機能カバレッジ（functional coverage）とパス率（pass rate）で最高成果を達成。従来の強力なベースラインRPGと比較して、機能カバレッジで最大20.08ポイント、パス率で最大29.74ポイント向上。

## 4. 結論（Conclusion）
アブレーション研究（ablation study）および構造進化分析により、Dual-DAGアーキテクチャ状態、モジュラリティ誘導の構造進化、明示的な構造収束の重要性が実証された。実装コードとデータはGitHubで公開済み。
