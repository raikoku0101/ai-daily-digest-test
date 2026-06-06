## 1. Introduction (はじめに)
実際のコードベースは数千のファイルから構成され、LLM はインポート、API、プロジェクト規約を理解する必要がある。従来手法は RAG や依存性解析で長い入力を注入するか、リポジトリごとに LoRA を微調整していたが、進化し続けるコードベースではコミットのたびにアダプタを再訓練する必要があり非効率。Code2LoRA はハイパーネットワークがリポジトリ固有の LoRA アダプタを生成し、推論時のトークンオーバーヘッドをゼロにする。

## 2. Related Work (関連研究)
LoRA（低ランク適応 / Low-Rank Adaptation）は効率的な微調整の標準手法。ハイパーネットワーク（Hypernetwork）はタスク記述や単一文書から重みを生成する研究が存在するが、長いリポジトリコンテキストや進化するコードベースへの対応例はなかった。Code2LoRA は Text2LoRA・Doc2LoRA を拡張し、GRU で順序的なコード差分（Code Diff）を集約する新機能を追加する。

## 3. Method (手法)
Code2LoRA は3要素で構成：
(1) リポジトリエンコーダ（Repository Encoder）がファイル埋め込みをリポジトリレベルで集約
(2) ハイパーネットワークが埋め込みを LoRA 重みに変換
(3) 凍結されたベース LLM が推論を実行
Code2LoRA-Static は単一スナップショットからアダプタを直接生成、Code2LoRA-Evo は GRU が差分列（Commit Diff Sequence）を処理して時系列適応を実現。

## 4. Benchmark (ベンチマーク)
RepoPeftBench は 604 個の Python リポジトリで構成：512 個は学習用、92 個は時系列外分布（OOD / Out-of-Distribution）テスト用。各リポジトリはテスト・非テストに分割され、タスクはテストスイートから抽出したアサーション補完問題。静的トラックと進化トラック（Evolutionary Track）の2設定で評価。

## 5. Experimental Setup (実験設定)
ベースモデルは Qwen2.5-Coder-1.5B、エンコーダは Qwen3-Embedding-0.6B。Code2LoRA-Static は約 720M、Code2LoRA-Evo は約 745M の訓練可能パラメータ。RAG、依存性解析コンテキスト、完全微調整（FFT / Full Fine-Tuning）、単一 LoRA、リポジトリごと LoRA、強化 Text2LoRA と比較。

## 6. Results (結果)
静的トラックで Code2LoRA-Static がクロスリポジトリ 63.8%・同一リポジトリ 66.2% の完全一致（Exact Match）を達成、最強ベースラインから +9.9 ポイント向上。進化トラックで Code2LoRA-Evo がクロスリポジトリ 60.3%（単一 LoRA 比 +5.2 ポイント）。時系列 OOD 評価でも 74.1% を達成し、強い汎化性能を実証。

## 7. Conclusion (結論)
リポジトリ知識は長い入力コンテキストではなくパラメータに注入し、ソフトウェア進化を追跡して更新することが最適であることを実証。Code2LoRA はカスタマイズ可能で低コストな AI コード支援ツールの構成要素となる可能性を示す。
