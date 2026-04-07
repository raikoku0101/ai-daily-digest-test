# AI Daily Digest — 2026-04-07

## 今日のハイライト
- VLAモデルの言い換え頑健性を評価するベンチマーク「LIBERO-Para」が70 upvotesでトップ注目論文に
- Claude Code v2.1.94リリース: Amazon Bedrock (Mantle) 対応とデフォルト努力レベルの高精度化
- 旧世代AIが新世代AIを上回るケースとその理由についてHackerNewsで議論が注目を集める

## Claude Code / Anthropic アップデート

### v2.1.94 (2026-04-07)
- Amazon Bedrock powered by Mantle のサポートを追加
- 各種ユーザー向けにデフォルト努力レベルをmediumからhighに変更
- Slackヘッダーをクリック可能なリンク付きコンパクト表示に改善
- 429レートリミットエラーおよびmacOSのConsoleログイン失敗を修正

### v2.1.92 (2026-04-04)
- `forceRemoteSettingsRefresh` ポリシー設定を追加
- インタラクティブなBedrockセットアップウィザードを追加
- `/cost` コマンドにモデル別・キャッシュヒット内訳を追加
- サブエージェント生成問題・Stop hookの失敗・ツール入力バリデーション問題を修正

### v2.1.91 (2026-04-02)
- アノテーションによるMCPツール結果の永続化オーバーライドを追加
- `disableSkillShellExecution` 設定を追加
- ディープリンクでのマルチラインプロンプトをサポート
- `bin/` 配下のプラグイン実行ファイルをサポート
- トランスクリプトチェーンの断絶および複数端末でのキーボードショートカットを修正

## 注目論文 TOP 5

**1. LIBERO-Para: VLAモデルにおける言い換え頑健性の診断ベンチマークと評価指標** | 70 upvotes | https://huggingface.co/papers/2603.28301
手法: Vision-Language-Action (VLA) モデルへの入力指示を言い換えた際のロボット動作の安定性を定量評価するベンチマークと指標群を設計
結果: 現状のVLAモデルが言い換えに脆弱であることを示し、ロボット制御の実用化に向けた重要な課題を提起

**2. Adam's Law: 大規模言語モデルにおけるテキスト頻度法則** | 45 upvotes | https://huggingface.co/papers/2604.02176
手法: LLMの出力とトレーニングデータのテキスト頻度分布の関係を実証的に分析し、「Adam's Law」と名付けた統計的法則を導出
結果: LLMが高頻度テキストパターンを過剰生成する傾向を定量化し、モデル評価・データキュレーションへの応用可能性を示す

**3. グループ相対的・自己蒸留型ポリシー最適化のサンプルルーティングによる統合** | 23 upvotes | https://huggingface.co/papers/2604.02288
手法: GRPOとDPO/自己蒸留法をサンプルルーティングの枠組みで統一的に理論化し、LLMの強化学習における安定化手法を提案
結果: 複数の最適化手法を単一フレームワークで扱え、LLM訓練の効率化・品質向上に貢献

**4. PLUME: 潜在的推論に基づく汎用マルチモーダル埋め込み** | 8 upvotes | https://huggingface.co/papers/2604.02073
手法: 潜在空間での推論を活用し、テキスト・画像・音声など複数モダリティを統一的に埋め込む新手法を提案
結果: 汎用的なマルチモーダル検索・分類タスクで既存手法を上回り、クロスモーダルAIシステムへの応用が期待される

**5. ONE-SHOT: 空間分離動作注入とハイブリッドコンテキスト統合による人間-環境映像合成** | 7 upvotes | https://huggingface.co/papers/2604.01043
手法: 人物と背景環境を空間的に分離してモーションを注入し、1枚の参照画像からリアルな合成動画を生成
結果: 単一ショットでの高品質映像合成を実現し、映像制作・VR/ARコンテンツ生成への応用が広がる

## AI ニュース

**1. 「I love you」「too」: LLMのアテンション機構を解説** | 4 pts | https://kaamvaam.com/machine-learning-ai/llm-attention-explanation/
内容: LLMにおけるアテンション機構の仕組みを、具体的な文例を通じてわかりやすく解説した記事
重要性: アテンション理解はLLM活用・デバッグの基礎であり、開発者・研究者向けの教育コンテンツとして注目を集めている

**2. 旧世代AIが新世代AIに勝つケース、その理由とは** | 4 pts | https://qz.com/ai-generative-chatbots-llm-machine-learning
内容: 最新の生成AIモデルが必ずしも旧世代より優れているわけではなく、特定タスクでは旧型が有利な場面を分析
重要性: 「新しさ=優秀さ」という思い込みに疑問を呈し、モデル選定の重要性と評価手法の課題を示唆

**3. LLM実験まとめ (1): ファインチューニング編** | 3 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/18/experiments-in-llms.html
内容: LLMのファインチューニングを実践した経験から得た知見を整理した技術ブログ記事
重要性: 実務での試行錯誤ベースのノウハウがまとめられており、LLM応用開発者のリファレンスとして価値が高い

**4. LLM実験まとめ (2): OpenAI Functions 活用** | 2 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/30/experiments-in-llms-3.html
内容: OpenAI Functionsを使ったLLMの構造化出力・ツール呼び出しの実験と実装例を紹介
重要性: Function Callingはエージェント開発の中核技術であり、実装例の共有が開発コミュニティの底上げに貢献

**5. LLM実験まとめ (3): ベクターDBと埋め込み** | 2 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/vector/embeddings/2023/06/23/experiments-in-llms-2.html
内容: ベクターデータベースと埋め込みベクトルを用いたLLMの検索拡張手法 (RAG) の実装実験を解説
重要性: RAGはLLMの知識拡張の主流アーキテクチャであり、実践的な知見の共有が業界全体の技術向上に寄与
