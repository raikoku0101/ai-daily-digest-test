## 1. Introduction (はじめに)
大規模言語モデル(LLM)のテスト時潜在推論を改善するため、本論文はGradCuitを提案する。既存手法は離散トークンを介して潜在変数と推論経路を接続するため、直接的なクレジット割当が困難である。GradCuitはTransformer中間層に最適化可能な潜在状態を挿入し、自己注意メカニズム(self-attention mechanism)を通じて生成トークンから潜在状態への直接的な勾配伝播(gradient propagation)を実現する。

## 2. Method (手法)
GradCuitの核心は、Transformer層lの隠れ状態空間に潜在変数z^(l)を組み込むことである。プロンプト表現と生成トークン表現の間に挿入された潜在状態は、因果自己注意(causal self-attention)により全ての後続トークンとの微分可能な接続を保つ。報酬勾配(reward gradient)は報酬信号R(x,c)と対数確率の勾配の積の期待値として定義され、この直接的な勾配ルートにより「circuit-like gradient flow」が実現される。

## 3. Experiments (実験)
5つの命令調整バックボーン(LLaMA、Qwen系列)と3つの推論ベンチマーク(GPQA-Diamond、GSM8K、MATH-500)で評価を実施。GradCuitは平均精度64.5%を達成し、Chain-of-Thought(CoT)を6.6ポイント上回った。

## 4. Results & Robustness (結果と堅牢性)
全30設定中23設定で最高精度を記録。学習率変動下で安定性を示し、LatentSeekの精度標準偏差1.53から0.82に低減。ランダム方向バリアント(報酬勾配なし)でもLatentSeekと競合性能を保持し、中間層最適化の有効性を示す。

## 5. Interpretability Analysis (解釈可能性分析)
トークンレベル勾配帰属(gradient attribution)分析により、推論接続詞(because、therefore等)が最高の勾配強度を示すことを発見。層最適化分析では、ネットワーク深さ25-50%の中間層が最適な最適化空間であることが明らかになった。

## 6. Conclusion (結論)
クレジット割当問題をTransformer自己注意回路の微分可能性を活用して解決。モデルパラメータ凍結下で、インスタンス固有の潜在状態を報酬から直接最適化できる堅牢で解釈可能なテスト時スケーリング手法を実現した。
