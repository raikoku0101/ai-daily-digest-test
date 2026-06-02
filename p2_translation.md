## 1. Introduction (はじめに)

推測的デコーディング（Speculative Decoding）はLLM推論を高速化する重要手法ですが、ドラフト品質とコストのトレードオフに制約されています。自己回帰ドラフター（autoregressive drafter）はトークン間の因果依存関係（causal dependencies）を適切にモデリングできますが逐次処理のオーバーヘッドがあり、並列ドラフター（parallel drafter）はコストを削減できる一方で依存関係モデリングが弱化するという根本的なジレンマが存在します。

## 2. Method (手法)

Dominoフレームワークは以下の2段階で動作します：
1. **並列ドラフトバックボーン（parallel draft backbone）**: ドラフトブロック全体の予備分布（preliminary distribution）を並列に生成
2. **Domino head（軽量因果精緻化モジュール）**: 接頭辞依存の因果情報（prefix-dependent causal information）を用いて予備分布を精緻化

さらに「base-anchored training curriculum（基底アンカー訓練カリキュラム）」により訓練安定性を向上。因果モデリングと高コストな自己回帰実行を完全に分離することが核心的アイデアです。

## 3. Results (結果)

Qwen3モデルでの検証結果：
- **Transformersバックエンド**: エンドツーエンドで最大5.49倍のスピードアップ
- **SGLangサービング**: 最大5.8倍のスループット改善

既存の投機的デコーディング手法と比較して、ドラフト品質を維持しつつ推論コストを大幅削減。LLMサービングの実運用コスト削減に直結する成果です。
