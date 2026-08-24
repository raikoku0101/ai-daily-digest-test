## 1. Introduction (はじめに)

長いコンテキストを処理する能力は大規模言語モデルにとって重要ですが、注意機構（Attention Mechanism）の二次計算複雑性がボトルネックとなっています。本論文は、前作 FlashPrefill のアルゴリズムプロトタイプを実運用レベルへ発展させた FlashPrefill V2 を提案しており、プリフィリング（Prefilling）段階での計算効率化に焦点を当てています。

## 2. Method (手法)

FlashPrefill V2 は三つの主要な改善を導入しています。第一に、平均補正項（Mean Correction Term）を加えることで近似誤差を抑制し、極端な疎性下でも性能低下を管理可能に保ちます。第二に、PackGQA メモリアクセス、ワープ特化（Warp Specialization）、ピンポンパイプライニング（Pingpong Pipelining）を採用し、FlashAttention-3/4 と整合させつつ FP8 推論に対応します。第三に、ページング化された KVキャッシュ（Paged KV-Cache）と連続バッチ処理（Continuous Batching）をネイティブサポートし、SGLang など現代的推論フレームワークに統合可能です。

## 3. Experiments and Results (実験と結果)

NVIDIA H20 GPU での評価では、128K コンテキスト長において FP8 精度で FlashAttention-2 比で 47.26 倍、BF16 精度で 27.19 倍の高速化を達成しています。FA3/4 準拠のデンス行列ベースラインとの比較では FP8 で 30.49 倍の高速化を維持しており、実用的な量子化要件を満たしながら高性能を実現しています。

## 4. Conclusion (結論)

本研究は長文脈 LLM 推論の実運用化に向けた重要な進展を示し、ブロック疎行列注意機構（Block-Sparse Attention）による効率化の実現可能性を実証しています。エンタープライズ LLM サービングにおけるコスト削減と性能向上の両立を実現する即戦力実装として価値があります。
