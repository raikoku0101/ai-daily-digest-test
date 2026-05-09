## 1. Introduction (はじめに)

本論文は SemEval-2026 Task 8 の Task B（参照文書付き生成）における優勝システムを報告しています。マルチターン RAG（Multi-turn Retrieval-Augmented Generation）における忠実な応答生成において、7つの異なる LLM を組み合わせた異質なアンサンブル（Heterogeneous Ensemble）アプローチを採用。GPT-4o-mini を判定者（Judge）として各インスタンスで最良の候補を選定し、26チーム中第1位を獲得しました。

## 2. Method (手法) — Judge-Orchestrated Ensemble

提案システムはヘテロジニアスな LLM アンサンブル構成で、7つの異なる LLM モデルと2つのプロンプト変種（Prompting Variants）を組み合わせています。GPT-4o-mini が各インスタンスについて最良の候補を選定するジャッジ・オーケストレーション（Judge Orchestration）により、単一モデルを上回る性能を実現。新たに導入した Meno-Lite-0.1 は 7B パラメータのドメイン適応モデル（Domain-Adapted Model）です。

## 3. Results & Analysis (結果・分析)

条件付き調和平均（Conditioned Harmonic Mean）スコア 0.7827 を達成し、最強ベースライン（gpt-oss-120b: 0.6390）を大きく上回りました。アブレーション研究（Ablation Study）では、モデルファミリー・スケール・プロンプト戦略の多様性がアンサンブルの成功に不可欠であることが実証されました。

## 4. Conclusion (結論)

MTRAGEval ベンチマークの注釈上の限界と改善の方向性についても分析し、評価フレームワーク自体への貢献も提供しています。コードは公開されています（GitHub: RaguTeam/ragu_mtrag_semeval）。
