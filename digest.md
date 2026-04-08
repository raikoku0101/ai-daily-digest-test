# AI Daily Digest — 2026-04-08

## 今日のハイライト
- Claude Code v2.1.97リリース: フォーカスビュー切替・ステータス行設定追加、CJKテキスト補完改善
- LLMをQAエンジニアとして評価するゲームベンチマーク「GBQA」が最多36 upvotes獲得
- ThinkTwice手法: LLMの推論と自己改善を同時最適化し推論精度を向上

## Claude Code / Anthropic アップデート

### v2.1.97 (2026-04-08)
- フォーカスビュートグルと`refreshInterval`ステータス行設定を追加
- パーミッション問題・MCP接続・レジューム選択画面のバグを修正
- 画像ハンドリングとCJKテキストのスラッシュコマンド補完を改善

### v2.1.96 (2026-04-08)
- Bedrock利用時に403エラーが発生するリグレッション（v2.1.94起因）を修正
- `AWS_BEARER_TOKEN_BEDROCK` / `CLAUDE_CODE_SKIP_BEDROCK_AUTH` 環境変数が正常動作するよう復旧

### v2.1.94 (2026-04-07)
- Amazon Bedrock（Mantle経由）のサポートを追加
- デフォルトのeffortレベルをhighに変更
- エージェントのレート制限ハンドリング・プラグインスキルフック・CJKテキスト破損を修正

## 注目論文 TOP 5

1. **GBQA: LLMをQAエンジニアとして評価するゲームベンチマーク** ▲36 [論文](https://huggingface.co/papers/2604.02648)
   ゲームを活用したQA（品質保証）タスクでLLMの能力を多角的に評価するベンチマークを構築
   LLMがソフトウェアテストの自動化に使えるかを定量評価し、次世代QA自動化への道を開く

2. **ThinkTwice: LLMの推論と自己改善を同時最適化する手法** ▲31 [論文](https://huggingface.co/papers/2604.01591)
   推論ステップと自己修正ステップを統合的に学習する新しいトレーニング戦略を提案
   複雑な推論タスクで精度と信頼性が向上し、自律的エラー修正能力を獲得

3. **Vanast: 合成トリプレット監督による仮想試着・人物アニメーション** ▲28 [論文](https://huggingface.co/papers/2604.04934)
   合成データによるトリプレット学習で衣服の仮想試着と人物動作アニメーションを統合
   ファッションECや映像制作での高品質な試着・合成映像生成への応用が期待される

4. **Watch Before You Answer: 視覚的根拠付きポスト学習** ▲23 [論文](https://huggingface.co/papers/2604.05117)
   回答前に視覚情報を精査するポスト学習パイプラインでマルチモーダルモデルの精度を改善
   視覚QAや医療画像診断など高精度な視覚理解が求められる分野への応用が見込まれる

5. **LLMのアジェンティックスキルはリアル環境でどこまで使えるか？** ▲23 [論文](https://huggingface.co/papers/2604.04323)
   実環境に近い設定でLLMのツール使用・タスク実行能力を体系的にベンチマーク
   エージェントAIの実用化における課題を明らかにし、改善指針を提供

## AI ニュース

1. **旧来のAIが新しいAIを上回る—その理由とは** 4pts [記事](https://qz.com/ai-generative-chatbots-llm-machine-learning)
   最新の大規模LLMが一部タスクで既存・特化型モデルに劣るという現象を分析
   モデル規模やコストが必ずしも性能に直結しないことを示し、特化型AIの再評価を促す

2. **「I love you」「too」: LLMのAttentionをわかりやすく解説** 4pts [記事](https://kaamvaam.com/machine-learning-ai/llm-attention-explanation/)
   具体的な文例を使ってTransformerのAttention機構の仕組みを直感的に説明
   LLMの内部動作理解を深めたい開発者・研究者・学習者に有用な教育コンテンツ

3. **ローカルLLMと機械学習で植物管理を実現** 1pts [記事](https://www.viam.com/post/practical-ai-local-llm-and-machine-learning-for-plant-care)
   エッジデバイス上のローカルLLMと機械学習を組み合わせて植物の状態を自動監視
   プライバシー重視のオフラインAI活用の可能性と農業・IoT分野への応用を示す

4. **LLM実験録（その1）: ファインチューニングで学んだこと** 3pts [記事](https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/18/experiments-in-llms.html)
   実践的なLLMファインチューニング手法を試行錯誤した知見をまとめた技術ブログ
   独自データでモデルをカスタマイズする際の実装上の注意点と成果を共有

5. **LLM実験録（その3）: OpenAI Functionsを試す** 2pts [記事](https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/30/experiments-in-llms-3.html)
   OpenAI Functions（現Tool Use）の仕組みと実装パターンを実験ベースで解説
   LLMに外部ツールを呼ばせる機能の基礎を学べる実践的チュートリアル
