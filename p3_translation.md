## 1. Introduction (はじめに)
テキスト生成画像 (Text-to-Image, T2I) モデルは高い写真品質を実現しているが、局所的・微細な構造的欠陥が存在する。既存の密集フィードバック手法はピクセルレベルの回帰に依存しており、「どこに欠陥があるか (Where)」「何の欠陥か (What)」「なぜ欠陥か (Why)」「その重要度 (Importance)」という多次元診断が困難。本研究はこの表現の限界を克服するために Structured Defect Grounding (SDG) を提案する。

## 2. Method (手法)
SDG では各欠陥を「位置 (Bounding Box)・種類 (Category)・理由 (Rationale)・重要度 (Importance)」の4タプルとして構造化し、集合予測問題 (Set Prediction) として定式化。成果物: ① 30K 画像の SDG-30K アノテーションデータセット、② 評価プロトコル SDG-Eval、③ Vision-Language Model (VLM) ベースの欠陥検出器、④ BoxFlow-GRPO による拡散モデル (Diffusion Model) のアライメント手法。ボックス由来の空間的報酬 (Box-Derived Spatial Reward) を強化学習で活用し生成モデルの品質を向上させる。

## 3. Results (実験結果)
SDG 検出器は既存の商用 VLM (GPT-4V 等) を上回る構造化欠陥検出性能を達成。SDG に基づく報酬関数は T2I アライメントを一貫して改善し、局所的な画像品質向上を実証。構造化表現によりより細粒度で解釈可能な品質評価が可能に。

## 4. Conclusion (結論)
SDG を現代生成モデルの診断・評価・改善のための統一的インスタンスレベルインターフェースとして確立。構造化表現によって RLHF (Reinforcement Learning from Human Feedback) ループへの統合が容易になり、T2I モデルの系統的な品質管理基盤を提供する。
