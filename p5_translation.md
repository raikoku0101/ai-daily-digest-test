## 1. Introduction (はじめに)
マルチモーダル大言語モデル(MLLM)は視覚理解に優れるがパラメータ知識に限定されており、動的な知識集約問題に対応できない。本論文は「vision-in-the-loop search」という新パラダイムを提案。検索途中に発見した画像が後続クエリを駆動し、複数ターンにわたって視覚的証拠が推論を導く。既存手法は視覚を入力段階または答え段階に限定し、中間推論での視覚依存性を見落としていた。

## 2. Method (手法) — データ合成 (EventVoyage-VL)
WikipediaとニュースからイベントをグラフG=(V,E,M,I,A,F)として正規化。Visual Co-occurrence Networks・Temporal Event Chains・Spatial Co-location Structures等の構造的述語で部分グラフを抽出し、視覚的に解決される依存関係を持つ合成QAを生成。品質管理では完全性・制約最小性・情報漏洩・画像テキスト一致・counterfactual removal(視覚なしで複数解が存在すること)を検証。

## 3. Method (手法) — エージェント設計
TextSearch・ImageSearch・ReverseImageSearch・WebVisit・FetchImage・CropImage・PythonInterpreterの7ツールを装備。能動的画像獲得(active image acquisition)により、Image discoverability(URL参照)とobservability(実読込み)を分離。視覚レジスタVが複数ターンで観察を保存し、FetchImageとCropImageのみがポリシーコンテキストに視覚トークンを導入する設計。

## 4. Training (訓練)
難易度層別化：Direct-answer probeでツールなし解不可問題を選定し、8回ロールアウトでeasy/medium/hardに分類。強い教師モデルがmedium/hard問題の軌跡を再生成しLLMジャッジで検証。SFT損失で言語主幹のみを更新(視覚エンコーダ・multimodal mergerは凍結)。強化学習なし。

## 5. Results (結果)
10のマルチモーダル情報検索ベンチマークで評価。30B-A3B: Direct Answer 20.7→Agentic 40.7→DeepVoyager-VL 58.6(+17.9)。8B: 17.5→35.3→54.8(+19.5)。オープンソースエージェントとして30B-A3Bが10中9、8Bが10中8ベンチマークで最高スコア。Vision-DeepResearch・LMM-Searcherを凌駕。

## 6. Ablation (アブレーション)
+7K VIL(Vision-in-the-Loop)軌跡の追加で8B+5.4・30B+6.5ポイント。Summary・ImageSearch・FetchImage・CropImage削除でそれぞれ2.5〜4.0ポイント低下。CropImageはVDR-Benchで特に重要。

## 7. Conclusion (結論)
中間視覚依存性を持つマルチモーダルイベントグラフ由来のデータが、長horizon マルチモーダル検索の効果的な学習路であることを実証。強化学習なしの教師あり微調整のみで、既存エージェントを大幅に上回る性能を達成。
