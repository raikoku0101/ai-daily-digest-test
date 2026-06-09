## 1. Introduction (はじめに)

音声ベース LLM が「コード生成・構造化分析・数学的導出」などのテキスト固有能力を発揮できない課題に対し、Listen-Write-Speak (LWS) パラダイムを提案。単一の自己回帰 LLM が「聴く(Listen)・書く(Write)・話す(Speak)」の 3 チャネルを並行実行し、可視テキスト出力を主要アウトプットチャネルとして扱う。フルデュプレックス相互作用・自由テキスト出力・聴取中の認知・発話中の認知の 4 要件を同時に満たす初のアプローチ。

## 2. Related Work (関連研究)

既存研究は推論強化音声 LLM・フルデュプレックス音声対話・マルチチャネル出力アーキテクチャの 3 カテゴリに分類。Think-Before-Speak 系（Step-Audio 2 等）は推論後に発話し、Interleaved Think-Speak 系（STITCH 等）は思考と発話を交互実行するが、4 要件を同時達成するものは存在しなかった。

## 3. Method (手法)

標準的な自己回帰 Transformer をアーキテクチャ変更なしに 3 チャネル化：
- **Listening チャネル**: ユーザー音声を常時処理（10 トークン/秒）
- **Visible Writing チャネル**: テキスト出力を常時表示（聴取中は推論、発話中は構造化出力）
- **Speaking チャネル**: 音声応答を発話中のみ生成

特殊 Token Schema で 3 チャネルを実装し、聴取相と応答相の分離で条件付きエントロピーを削減・因果一貫性を保証する。

## 4. Data Construction (データ構築)

秒単位の認知アノテーションが公開コーパスに存在しないため 2 段階パイプラインを設計。Stage 1: 強力な LLM でテキスト QA ペアから streaming_reasoning_chain・voice_response・structured_response を合成。Stage 2: 実音声の CTC アラインメントと組み合わせ Unit 形式に変換。500K の中英訳例を構築。

## 5. Experiments (実験)

MiniCPM-V + Qwen3-8B を基盤モデルとし 32 個の A100 GPU で学習。主要結果：
- URO-Bench 中国語 Pro 平均 84.6（公開ベースラインを上回る）
- VoiceBench AlpacaEval 品質スコア 4.72（GPT-4o-Audio の 4.78 に近接）
- 話す・書く出力の一貫性 92.6%
- フルデュプレックス割り込み時の品質スコア 4.02 を維持

## 6. Conclusion (結論)

LWS は Token Schema のみで単一自己回帰 LLM 内にフルデュプレックス聴取・可視テキスト出力・リアルタイム発話を統合する。「可視テキスト出力は音声対話の第一級チャネルとして機能し、リアルタイム性を損なわない」ことを実験で実証した。
