## 1. Introduction (はじめに)
ロボットの実装において、Vision-Language-Action (VLA) モデルとWorld-Action Models (WAM) が急速に進化している一方で、既存の推論ランタイムはこれらモデルの要件に対応していない。本論文は、異種デバイス上での「閉ループ制御内での多率実行（Multi-Rate Execution）」「レイテンシ優先のバッチ1推論（Latency-First Inference）」「トークンI/O以上の拡張可能なインターフェース（Extensible Interface）」という3つの要件に対応する、C++ベースのポータブル推論ランタイム「Embodied.cpp」を提示する。

## 2. Related Work and Motivation (関連研究と動機)
VLAモデルはAR-Token型・VLMバックボーン型・階層型・非同期型に分類され、WAMモデルは予測段階と行動生成の結合方式によって異なる。既存ランタイム（llama.cpp、ONNX Runtime、vLLM-Omni）は「要求応答型（Request-Response）」を想定した設計であり、ロボット統合・マルチレート実行・異種ハードウェア対応における課題支援が不足している。

## 3. System Architecture (システムアーキテクチャ)
Embodied.cpp は「入力アダプタ（Input Adapter）→シーケンスビルダ（Sequence Builder）→バックボーン実行（Backbone Execution）→ヘッドプラグイン（Head Plugin）→デプロイメントアダプタ（Deployment Adapter）」の5層アーキテクチャで実装される。設計原則は (1) モジュール式多率実行、(2) レイテンシ優先融合実行、(3) 拡張可能な演算子とI/Oサポートである。

## 4. Evaluation (評価)
HY-VLAとpi0.5の閉ループ実験では、それぞれ100.0%と91.0%のタスク成功率を達成した。LingBot-VAの単一Transformerブロック評価では、量子化（Quantization）により重みメモリを312.2 MiBから88.1 MiBに削減しつつ、出力精度を維持している。マルチレート実行の効率性も複数プラットフォームで実証されている。

## 5. Conclusion (結論)
多様化するモデルファミリーにおいて、共有実行パスが収束しつつある。Embodied.cpp はこの共通インフラと差異化されたプラグイン部分を分離し、将来の拡張に対応可能な設計を実現している。具現化AI（Embodied AI）の現場展開における実用的なインフラとして、ロボティクス研究・産業両方への貢献が期待される。
