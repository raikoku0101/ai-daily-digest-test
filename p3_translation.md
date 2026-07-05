## 1. Introduction (はじめに)
近年のマルチモーダル大規模言語モデル（MLLM: Multimodal Large Language Model）は臨床画像推論で有望な成果を上げていますが、既存の学習パイプラインは最終回答の正確性またはシーケンスレベルの選好のみに依存しており、スパースな信用配分（Sparse Credit Assignment）が課題です。医療 VQA（Visual Question Answering）ベンチマーク分析から、早期ステップの推論失敗が連鎖する「失敗カスケード（Failure Cascades）」が不正確な予測の主要原因であることが明らかになりました。

## 2. Method (手法)
MRPO（Medical Reasoning-aware Policy Optimization）アルゴリズムはステップ単位のプロセス報酬を組み込みます。最終答が不正確な場合、早期の無効な推論ステップのトークンに対して指数関数的に大きなペナルティを割り当て、誤差カスケードを遮断しつつ成功パスの学習を損なわない設計を実現。ステップ認識型 RL（Step-Aware Reinforcement Learning）として実装されます。

## 3. Experiments & Results (実験・結果)
3 つのマルチモーダル LLM バックボーン上で評価。Qwen3-VL-8B-Instruct において HuatuoGPT-Vision-34B を 2.79 ポイント上回る性能を達成。MRPO は標準 GRPO（Group Relative Policy Optimization）および最近の RL 基盤手法を一貫して上回り、早期推論失敗率を 64.0% から 13.0% へと劇的に削減しました。

## 4. Conclusion (結論)
ステップ単位の失敗を標的化した軽減により、医療マルチモーダル推論タスクで実用的な効果が得られることを実証。より小さなモデルで大型モデルを上回る性能を実現したことで、医療 AI の安全性・説明可能性・効率性の同時向上への道を開く重要な成果です。
