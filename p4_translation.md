## 1. Introduction (はじめに)
長文脈モデリングはLLMの重要な機能ですが、注意機構（Attention Mechanism）の二次計算量（Quadratic Complexity）が「プリフィル段階（Prefill Stage）で特に深刻なボトルネック」となっています。本研究は前作FlashPrefillを実運用対応へ進化させた実装面での改良に焦点を当てています。

## 2. Related Work (関連研究)
FlashAttention系の効率的な注意実装と、疎行列（Sparse Matrix）注意パターンを活用した軽量化手法の既往研究が背景にあります。先行研究との関係性は「瞬時パターン発見（Instantaneous Pattern Discovery）と最大値ベース動的閾値（Max-based Dynamic Thresholding）」を用いた手法として言及されています。

## 3. Method (手法)
三つの改良が実装されました：(1)平均補正項（Mean Correction Term）による近似誤差の抑制、(2)PackGQAメモリアクセスとワープ特殊化（Warp Specialization）を含む疎行列演算子の再設計、(3)ページング化KVキャッシュ（Paged KV Cache）と連続バッチ処理（Continuous Batching）への対応です。

## 4. Experiments & Results (実験と結果)
NVIDIA H20 GPUでの評価により、128K文脈長でFlashAttention-2比47.26倍（FP8精度）、27.19倍（BF16精度）のスピードアップが報告されています。実運用レベルの長文脈LLM推論基盤として機能するソリューションの実装を達成しました。
