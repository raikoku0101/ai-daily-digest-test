## 1. Introduction (はじめに)
既存のロボット操作ベンチマークは「単純・短時間・特定スキル限定・シミュレーションまたは実世界のどちらか一方」という制限があり、汎用ロボットポリシー (generalist robot manipulation policy) の総合的な評価が困難だった。本研究では RoboDojo を提案し、シミュレーションと実世界を統合した包括的評価基盤を構築する。

## 2. Method (手法)
シミュレーション環境として Isaac Sim を用いた異種並列シミュレーション (heterogeneous parallel simulation) で42タスクを構築し、汎化性能 (generalization)・記憶能力 (memory)・精密性 (precision)・長期実行 (long-horizon execution)・オープン語彙命令追従 (open-vocabulary instruction following) の5次元で評価。実世界評価には RoboDojo-RealEval システムを用い、クラウドアクセス・標準化ハードウェア・シーンリセット・評価プロトコルを整備。

## 3. Experiments & Results (実験・結果)
統合ツール XPolicyLab に30個のポリシーを統合し、両環境で評価を実施。公開リーダーボード (public leaderboard) を構築し、現在のポリシー性能の体系的分析を公開。既存ベンチマークでは測定できなかった長期タスクや記憶能力の評価結果を示した。

## 4. Conclusion (結論)
シミュレーションの拡張性・コスト効率と実世界の妥当性検証を両立する包括的評価基盤を提供。汎用ロボット開発における標準評価プラットフォームとして研究コミュニティの進展を加速させる役割が期待される。
