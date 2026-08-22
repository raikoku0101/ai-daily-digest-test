## 1. はじめに（Introduction）
大規模言語モデルの長文脈処理は重要な機能だが、アテンション機構の二次計算量（quadratic complexity）がプリフィル（prefilling）段階でボトルネックとなっている。FlashPrefill V2は先行研究FlashPrefillをプロトタイプから本番環境へ実用化することを目指す。ブロックスパースアテンション（block-sparse attention）により重要なアテンションパターンのみを計算し、計算量を削減する。

## 2. 手法（Method）
FlashPrefill V2は3つの主要改良を導入。①**平均補正項（mean correction term）**の追加で極度の疎性（sparsity）下でも近似誤差を抑制。②**PackGQA**メモリアクセス、**ワープ特殊化（warp specialization）**、**ピンポンパイプライニング（pingpong pipelining）**を備えた疎行列アテンション演算子を再設計しFlashAttention-3/4と整合。③ページング化KVキャッシュ（paged KV cache）と連続バッチ処理（continuous batching）を標準サポートし、SGLang等の推論フレームワークへの統合を実現。

## 3. 実験と結果（Experiments & Results）
NVIDIA H20 GPU上で評価。128K文脈長においてFlashAttention-2比で**FP8精度で47.26倍、BF16精度で27.19倍のスピードアップ**を達成。FP8精度ではFlashAttention-3/4準拠の密行列ベースラインに対しても30.49倍のスピードアップを実現し、量子化要件を満たしながら実用的な性能を提供する。
