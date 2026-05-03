## 1. Abstract (概要)

本論文は「RoundPipe」という新型パイプライン並列化スケジュールを提案。消費者向け GPU（RTX 4090 など）上での LLM 微調整（Fine-tuning）の課題として、GPU メモリ制限と低速 PCIe 接続があります。既存手法の「重み結合問題（Weight Binding Issue）」を解決し、GPU を「ステートレス実行ワーカー（Stateless Execution Worker）」のプールとして扱う設計により、ほぼゼロバブル（Near-Zero-Bubble）のパイプラインを実現しています。

## 2. Introduction (はじめに)

大規模言語モデルの微調整は計算コスト削減の観点で重要ですが、消費者向け GPU のメモリ容量制約が課題です。パイプライン並列化（Pipeline Parallelism）と CPU オフロード技術の組み合わせは有効ですが、「重み結合問題」により不均一なモデルステージ（例：LM ヘッドが大きい層）を GPU に固定割り当てすると、最重負荷 GPU がスループット全体を制限しパイプラインバブルが深刻化します。RoundPipe はこの制約を突破し、ラウンドロビン方式で動的にステージを GPU 間に分散配置します。

## 3. Method (手法)

RoundPipe の主要技術要素は 3 つです。① **優先度考慮転送スケジューリングエンジン（Priority-Aware Transfer Scheduling Engine）**: データ転送の効率化で通信オーバーヘッドを削減。② **細粒度分散イベントベース同期プロトコル（Fine-Grained Distributed Event-Based Synchronization Protocol）**: 複数 GPU 間の正確な同期を保証しながら実装複雑性を低減。③ **自動レイヤー分割アルゴリズム（Automated Layer Partitioning Algorithm）**: モデル構造に基づいて最適なステージ分割を決定。これらによりステージの動的再割り当てが可能になり、パイプラインバブルを最小化します。

## 4. Experiments (実験)

評価環境は 8× RTX 4090 サーバー。実験対象モデルは 1.7B〜32B 規模で、既存のパイプライン並列化手法と比較。測定指標はスループット（トークン/秒）・学習時間・メモリ利用効率。LoRA 微調整（Parameter-Efficient Fine-Tuning: PEFT）による実験も実施し、Qwen3-235B という極めて大規模なモデルでの動作確認も行っています。

## 5. Results & Conclusion (結果・結論)

RoundPipe は既存の最先端手法に対して 1.48〜2.16 倍のスピードアップを達成。単一サーバー環境で Qwen3-235B モデルを 31K シーケンス長で微調整できる点は従来手法では達成困難でした。消費者向け GPU の制限を効果的に克服し、コスト効率的な大規模 LLM 訓練を民主化するソリューションとして、オープンソース Python ライブラリとして公開済みです。
