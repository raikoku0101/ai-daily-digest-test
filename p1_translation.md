## 1. Introduction（はじめに）
世界モデルのスケーリングは「クロールビデオ＋計算増加」という非効率な戦略に依存している。本論文はゲーム開発が検証可能なフィードバック機構を提供する未活用リソースであり、エンジンの自動検証（衝突判定、物理演算）と開発者の人間的判断を組み合わせることでスケーラブルな報酬信号を生み出せると主張する。

## 2. The Thesis of Verification（検証命題）
「検証可能性（verifiability）」を中心概念として定義。タスクが自動検証可能であるとは、出力が明示的な正確性基準（プログラム実行、定理チェック、数値比較）によって低コストで評価できる場合を指す。RLHEV（Reinforcement Learning with Human-Engine Verification）フレームワークを提案し、エンジン診断と人間承認を結合する制約付き最適化問題として定式化。

## 3. Why Current Spatial Data Fails（現在の空間データの限界）
ビデオ生成・3D生成・物理シミュレーター三領域で検証困難性が進展を阻害していることを論じる。ビデオモデルはFréchet Video Distance等の曖昧なプロキシに依存し物理的一貫性を直接検証できない。著者らはこれを「検証不可能性税（unverifiability tax）」と呼ぶ。

## 4. Game Development as Human-Engine Verification（実装）
AWoMo（Agentic World Model）は4インターフェース（意図入力・アクション出力・検証・レビュー）を備える。UWDP（Unified World-Development Protocol）という型付きマルチモーダルプロトコルにより開発作業を構造化されたstate-action-check-reviewトレースに変換する。エンジン検証（幾何学、物理、スクリプト実行、到達可能性）と人間のグローバル受理判断による二重検証構造。

## 5. Experiments（実験結果）
UnitySceneBench（200例）でFull RLHEVが最高スコア0.681を達成。スケーリング実験で訓練データ増加に伴う性能向上を確認、生成品質0.8197に到達。OOD汎化テストでUnity分布シフト時に0.25→0.75へ大幅改善。Unity→Unreal/Godotのクロスエンジン転移でも正の信号を確認。具体化された政策学習ではR2R、MuJoCoで+0.79%～+48.43%の改善。

## 6. Discussion（議論）
次段階として「再帰的自己改善ループ」—モデルが世界を構築し、エージェントがテストし、テスト結果が次世代訓練を改善する—を展望。世界モデルスケーリングの新たなパラダイムを提示する先駆的研究。
