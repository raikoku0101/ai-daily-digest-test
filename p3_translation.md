## 1. Introduction (はじめに)

消費者向けGPU（consumer-grade GPU）でのLLMファインチューニングは費用対効果に優れますが、GPUメモリ制限とPCIe接続の低帯域幅が大きな制約です。パイプライン並列処理（pipeline parallelism）とCPUオフローディング（CPU offloading）を組み合わせることでこれらを緩和できます。しかし既存のパイプラインスケジュールには「weight binding 問題（重み結合問題）」という根本的制限があり、LMヘッドなど不均等なモデルステージが最重負荷 GPU にボトルネックを生じさせ、深刻なパイプラインバブル（pipeline bubble）が発生します。

## 2. Method (手法)

RoundPipeは weight binding 制約を打破する革新的なパイプラインスケジュール手法です。GPUをステートレスな実行ワーカープール（stateless execution worker pool）として扱い、計算ステージ（computation stage）をラウンドロビン方式で動的に割り当てることで、ほぼゼロバブル（near-zero bubble）のパイプラインを実現します。技術的には以下の3要素を統合: (1) 優先度認識転送スケジューリングエンジン（priority-aware transfer scheduling engine）、(2) 細粒度分散イベント同期プロトコル（fine-grained distributed event synchronization protocol）、(3) 自動レイヤー分割アルゴリズム（automatic layer partitioning algorithm）。

## 3. Experiments & Results (実験と結果)

8×RTX 4090サーバーでの評価では、1.7B〜32Bパラメータモデルのファインチューニングにおいて、最先端ベースラインと比較して1.48〜2.16倍のスループット向上を達成しました。特に重要な成果として、単一サーバーでQwen3-235Bモデルの31Kシーケンス長（sequence length）のLoRA（Low-Rank Adaptation）ファインチューニングが可能になりました。これは従来、大規模クラスターが必要とされていた規模のモデルです。

## 4. Conclusion (結論)

RoundPipeはオープンソースのPythonライブラリとして公開されており、包括的なドキュメントとともに提供されています。高価なクラスター環境なしに、個人研究者や小規模チームでも大規模LLMのファインチューニングが現実的に行えるようになり、AI研究の民主化（democratization of AI research）に大きく貢献します。
