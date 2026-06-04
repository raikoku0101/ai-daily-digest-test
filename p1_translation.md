## 1. Introduction (はじめに)

本論文は、検索拡張生成（RAG: Retrieval-Augmented Generation）パイプラインに特化した小規模言語モデル（SLM: Small Language Model）ファミリーであるOptimal Cognitive Core（OCC）を紹介。提供されたコンテキストのみに基づいて忠実に回答することを目指し、「大規模化よりも堅牢な推論能力」を重視する設計原則を採用。OCC-RAG-0.6BおよびOCC-RAG-1.7Bは、2〜6倍大きい汎用モデルと同等またはそれ以上のパフォーマンスを達成。

## 2. Model Design Principles (モデル設計原理)

OCC-RAGは3つの中核能力を備えるべきと定義。第1に、複数のコンテキスト部分にわたるマルチホップ推論能力。第2に、事前学習知識（パラメトリック知識）への依存を回避し文脈への忠実性を保つこと。第3に、証拠が不十分な場合に適切に回答を控える校正された拒否（calibrated refusal）能力。ミッドトレーニング（mid-training）は、推論トレース（reasoning trace）の構造的信号を提供することで、これらの目標を実現する重要な段階。

## 3. Training Data (訓練データ)

3.25Mの質問応答ペアからなるコーパスを構築。単一ホップ質問（280万）、マルチホップ質問（43万）、回答不可能な例（4.3万）で構成。知識グラフ（knowledge graph）の抽出とパス抽出により、マルチホップ推論の構造的制御を実現。全訓練例に明示的な推論トレースを付与し、「クエリ分析」「ソース分析」「推論」「ステータス」「回答」の5セクションで構成。

## 4. Mid-training (ミッドトレーニング)

Qwen3-0.6B-BaseとQwen3-1.7B-Baseから開始し、約9×10⁹トークンに対して教師あり微調整（SFT: Supervised Fine-Tuning）を実施。マルチホップ例を1エポック内で3回提示するオーバーサンプリングにより単一ホップ例とのバランスを確保。各モデルの訓練に8個のNVIDIA H100 GPUを使用し、17〜28時間のウォールクロック時間を要した。

## 5. Evaluation (評価)

HotpotQA、MuSiQue、TAT-QA、ConFiQA、MuSiQue-Unの5つのベンチマークで評価。OCC-RAG-0.6BはGemma3-4BおよびSmolLM3-3Bを全次元で上回り、OCC-RAG-1.7Bは全モデル中で忠実性（faithfulness）と拒否性能（refusal performance）で最高結果を達成。メモリ化率（memorization rate）をQwen3-0.6Bの8.2から5.2に削減。

## 6. Conclusion (結論)

タスク特化型の小規模モデルが、適切な訓練カリキュラムと監督形式を通じて忠実性を習得できることを実証。構造化ミッドトレーニング、証拠アンカー推論トレース（evidence-anchored reasoning traces）、校正された拒否により、効率性を損なうことなく堅牢で透明性の高いQAシステムの構築が可能。
