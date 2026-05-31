## 1. Introduction (はじめに)
機械学習分野への論文投稿急増により査読システムが過負荷に。LLM ベースの自動査読への関心が高まるが、その品質評価は ROUGE・BLEU などの表面的メトリクスに依存しており、査読の質を正確に測定できていませんでした。本研究は「LLM 査読者が科学的な欠陥をどの程度捉えられるか」という問いに体系的に取り組みます。

## 2. Method (手法)
PRISM（Peer Review Intelligence via Structured Multi-dimensional assessment）は査読品質を 4 次元で評価するフレームワークです：①分析の深さ（Depth of Analysis）、②新規性評価（Novelty Assessment）、③欠陥特定と主要問題の優先付け（Flaw Identification & Major Issues Prioritization）、④多次元的建設性（Multi-dimensional Constructiveness）。議論マイニング・検索拡張検証・合意ベーススコアリングを組み合わせ、ICLR・ICML・NeurIPS のレビューデータセットから層別抽出したコーパスを使用。

## 3. Experiments & Results (実験と結果)
5 つの主要自動査読システムと人間査読者を比較。LLM は個別次元では人間と同等以上のパフォーマンスを示します（分析深度で同等、新規性検証で優位、批判の優先付けで高精度）。しかし「すべての次元で人間基準に一貫して対抗できるシステムは存在しない」ことが判明。各システムは固有のプロファイルを持ち、集約メトリクスでは見落とされる特有の弱点があります。

## 4. Conclusion (結論)
LLM 査読者は人間査読の完全代替ではなく、「特定次元での効果的な補完ツール」として理解すべきです。各システムの強み・弱みを認識した上で戦略的に活用することが重要で、査読支援 AI の実用評価に向けた重要な評価基盤を提供します。
