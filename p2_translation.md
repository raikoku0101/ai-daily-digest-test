## 1. Introduction (はじめに)
JetBrainsが開発したMellum 2は、12Bパラメータの混合専門家（Mixture-of-Experts: MoE）言語モデルで、トークンあたり2.5Bの活性パラメータを持つ。コード生成・編集、デバッグ、多段階推論、ツール利用、エージェント機能といった開発者向けタスクに特化した汎用モデル。前任の4B密集モデルMellumを後継し、IDE（統合開発環境）での実運用を想定した設計となっている。

## 2. Model Architecture (モデルアーキテクチャ)
効率的な推論を重視し、Qwen2.5-7Bと同等の単一H100 GPU速度を目標に設計。64個の専門家から8個をルーティングするMoE構造に加え、(1) 4KVヘッドのグループクエリアテンション（Grouped-Query Attention）、(2) レイヤーの3/4に適用するスライディング窓注意機構（sliding window attention）、(3) マルチトークン予測ヘッド（Multi-Token Prediction head）を採用。

## 3. Pre-Training (事前学習)
約10.6兆トークンを3段階のカリキュラムで学習。「ウェブ早期、精選データ後期」パラダイムに従い、フェーズ1では70%がウェブデータ、フェーズ3では59%がコードデータ。Muonオプティマイザ（Muon optimizer）とFP8ハイブリッド精度を採用し、ウォームアップ-ホールド-減衰（Warmup-Hold-Decay）スケジュールを使用。

## 4. Long Context Extension (長文脈拡張)
事前学習後、8,192トークンから131,072トークン（128K）への拡張を実施。層選択的YaRN（layer-selective YaRN）をスライディング窓層を除く全注意層のみに適用することで、均一適用より優れた性能を達成。約117Bトークンの追加学習でRULERスコアが安定化。

## 5. Post-Training (後学習)
SFT（教師あり微調整）とRLVR（検証可能報酬による強化学習）の2段階で実施。「Instruct型」（直接回答）と「Thinking型」（推論トレース付き）の2変種を生成。RLではGRPOアルゴリズムの改良版「IcePop」（訓練-推論間の確率比補正）と報酬シェーピングを適用。

## 6. Evaluation Results (評価結果)
コード生成（EvalPlus 78.4%）、数学（GSM-Plus 80.5%）、ツール利用（BFCL v3 66.3%）で競争力を発揮。知識分野（GPQA Diamond 40.9%）が相対的な弱点。2.5Bアクティブパラメータで4〜14Bの密集モデルと同等以上の性能を実現し、単一H100でQwen2.5-7B（193 tokens/s）と同等速度（192 tokens/s）を達成。
