## 1. Introduction (はじめに)

言語モデル開発における進歩は、アーキテクチャやプリトレーニングコーパス(pretraining corpus)、訓練手法といった選択判断に基づいています。本論文は、信頼性の高い性能予測の必要性に対し、既存手法の限界を指摘しています。交差エントロピー損失(cross-entropy loss)は下流タスク性能との関連性が低く、直接評価(direct evaluation)は計算コストが高くかつ初期段階では情報量が限定的です。

## 2. Method (手法)

提案手法は、専門家による解答(expert-written solutions)に対する次トークン分布(next-token distribution)から「トークン統計情報の集約」を通じてプロキシメトリクス(proxy metrics)を構築します。具体的には、エントロピー(entropy)、上位k精度(top-k accuracy)、専門家トークンランク(expert token rank)などの統計量を活用し、モデル候補の能力を評価する信号源として利用しています。

## 3. Experiments (実験)

三つの評価シナリオで検証されています。①異種推論モデル群の選択：Spearman相関係数0.81を達成(交差エントロピーの0.36と比較)。②25候補コーパスのプリトレーニングデータ選択：直接評価比で約10,000倍の計算効率改善。③18倍の計算範囲での訓練時予測(training-time forecasting)：既存手法の半分のエラーで達成。

## 4. Results & Conclusion (結果と結論)

「専門家軌跡(expert trajectories)は幅広く有用な信号源である」として、モデル開発ライフサイクル(model development lifecycle)全体における信頼性の高い性能予測を実現しています。提案プロキシメトリクスは損失ベースおよび計算ベースの従来手法を一貫して上回り、パレート最適境界(Pareto-optimal frontier)を拡張しています。LLM研究の開発サイクル短縮に直結する実用的な貢献です。
