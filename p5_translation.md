## 1. Introduction (はじめに)

現代の自動回帰モデル（autoregressive model）において、トークンは計算の基本単位であり、生成長（generation length）は推論コスト（inference cost）と推論性能（reasoning performance）の両方に直接影響します。しかし既存アプローチは粗粒度のシーケンスレベル（sequence-level）処理が中心で、細粒度のトークンレベル（token-level）長さモデリングが不足しています。この欠如により、動的な計算予算配分（dynamic budget allocation）や生成制御が困難です。

## 2. Method (手法)

Length Value Model（LenVM）は残余生成長（remaining generation length）をトークンレベルで予測するフレームワークです。各生成トークンに一定の負の報酬（constant negative reward）を割り当て、長さモデリングを価値推定問題（value estimation problem）として定式化します。この設定により、アノテーション不要で密度高く不偏な教師信号（unbiased supervision signal）を獲得できます。予測するのは残り生成ホライゾン（remaining generation horizon）の単調プロキシとして機能する有界割引リターン（bounded discounted return）です。スケーラブルな事前訓練パラダイム（scalable pretraining paradigm）として設計されています。

## 3. Experiments & Results (実験と結果)

LIFEBench正確長マッチング（exact-length matching）タスクでは、7Bモデルの長さスコアを「30.9から64.8へ改善」し、最先端の閉鎖ソースモデルを大幅に上回りました。GSM8K（トークン予算200、token budget 200）ではLenVMが63%の精度を維持する一方、基準手法は6%に留まるという顕著な差を示しました。トークンレベルの価値推定値（token-level value estimates）は生成ダイナミクス（generation dynamics）の解釈可能な視点も提供します。

## 4. Conclusion (結論)

LenVMは性能と効率のトレードオフを継続的に制御でき、プロンプト境界からの総生成長を高精度に予測します。将来の強化学習訓練（RL training）を支援する長さ特化価値信号（length-specific value signal）としての応用が期待され、LLM推論の効率化と予測可能性向上に向けた重要な基盤技術となります。
