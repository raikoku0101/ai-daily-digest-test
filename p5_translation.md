## 1. Abstract (概要)

本研究は画像編集タスクにおける強化学習応用を提案します。従来の報酬モデルが全体スコアのみを提供し、異なる指示要件を無視した偏った報酬を生成していた問題に対し、「Edit-R1」フレームワークを導入。CoT（Chain-of-Thought）ベースの推論報酬モデル（Reasoning Reward Model: RRM）を構築し、編集指示を複数の原則に分解して評価します。Seed-1.5-VL などの強力 VLM を上回り、3B→7B での明確なスケーリング傾向が確認されました。

## 2. Introduction (はじめに)

テキスト生成では RLHF（Reinforcement Learning from Human Feedback）が重要な役割を果たしていますが、画像編集への応用は未開拓でした。編集タスク全体に対応できる堅牢な汎用報酬モデルの欠如が主な課題で、既存の編集報酬モデルは異なる指示要件を無視して偏った報酬（Biased Rewards）を生成していました。単純なスコアラーから「推論検証器（Reasoning Verifier）」への転換が重要という主張が本研究の核心です。

## 3. Method (手法)

Edit-R1 フレームワークは 3 段階構成です。① **SFT cold-start**: 監督付き微調整（Supervised Fine-Tuning）で CoT 報酬軌跡（CoT Reward Trajectories）を生成するコールドスタート。② **GCPO（Group Contrastive Preference Optimization）**: グループ対照選好最適化という新 RL アルゴリズムが人間のペアワイズ選好データ（Pairwise Preference Data）を活用して Pointwise 型 RRM を強化。③ **GRPO**: 構築された RRM を用いて編集モデルを訓練。Edit-RRM は編集指示を個別の原則（Principle）に分解し、各原則に対して編集画像を評価・集約して解釈可能な細粒度報酬を生成します。

## 4. Experiments (実験)

FLUX.1-kontext などの複数の編集モデルを対象に広範な実験を実施。Edit-RRM の性能が Seed-1.5-VL および Seed-1.6-VL を編集特化報酬モデルとして上回ることを実証。3B→7B パラメータ範囲での明確なスケーリング傾向（Scaling Trend）が観察され、パラメータ数増加に伴う一貫した性能向上が確認されました。

## 5. Results & Conclusion (結果・結論)

Edit-R1 は画像編集モデルに有意な性能向上をもたらし、推論型検証器ベースのアプローチが従来スコアリング手法より優れた報酬信号を提供できることを実証しました。このフレームワークは編集指示の複数側面を同時評価でき、より正確で信頼性の高い画像編集システムの構築を可能にします。他の視覚生成タスクへの拡張も期待されます。
