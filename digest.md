# AI Daily Digest — 2026-04-07

## 今日のハイライト
- Self-Distilled RLVR が81 upvotes でHuggingFace 本日の最注目論文にランクイン — 追加データなしで自己強化学習を実現する新手法
- Claude Code v2.1.92 リリース — Bedrock インタラクティブセットアップウィザード、モデル別コスト内訳など実用機能を追加
- 「古いAIが新しいAIを上回る」理由を解説する記事がHackerNews で注目を集め、LLM の能力評価に再考を促す

## Claude Code / Anthropic アップデート

### v2.1.92（2026-04-04）
- `forceRemoteSettingsRefresh` ポリシー設定を追加
- AWS Bedrock のインタラクティブセットアップウィザードを実装
- モデルごとのコスト内訳表示機能を追加
- サブエージェント生成失敗・`prompt-type` Stop フックの不具合を修正

### v2.1.91（2026-04-02）
- アノテーションによる MCP ツール結果の永続化オーバーライドを追加
- `disableSkillShellExecution` 設定を追加
- ディープリンクでのマルチライン プロンプト対応
- `bin/` ディレクトリ配下のプラグイン実行ファイルサポートを追加

### v2.1.90（2026-04-01）
- インタラクティブな機能チュートリアル `/powerup` コマンドを導入
- プラグイン マーケットプレイスのオフラインサポートを追加
- 無限レート制限ダイアログループを修正
- `--resume` 時のプロンプトキャッシュミス回帰を修正

## 注目論文 TOP 5

**1. Self-Distilled RLVR（自己蒸留強化学習）| 81 upvotes | https://huggingface.co/papers/2604.03128**
外部アノテーションなしにモデル自身の出力を報酬信号として利用する強化学習フレームワークを提案。
数学・コード生成ベンチマークで既存 RLVR 手法を上回り、データ効率の大幅改善と小規模モデルへの適用可能性を示す。

**2. A Simple Baseline for Streaming Video Understanding（ストリーミング動画理解の簡潔なベースライン）| 55 upvotes | https://huggingface.co/papers/2604.02317**
複雑なアーキテクチャ不要で、軽量なフレームサンプリングと時系列アテンションで動画ストリームをリアルタイム処理する手法を提案。
主要ベンチマークで SOTA に匹敵しつつ推論コストを大幅削減、エッジデバイス上の動画 AI への応用に直結。

**3. Token Warping Helps MLLMs Look from Nearby Viewpoints（トークンワーピングで隣接視点からの観察を可能に）| 23 upvotes | https://huggingface.co/papers/2604.02870**
視点変換を token 空間でシミュレートするワーピング機構を MLLM に導入し、単一画像から複数視点の理解を実現。
3D 推論・ロボティクス・AR など多視点認識が必要なタスクでの精度向上が期待され、空間 AI の実用化を加速。

**4. Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?（エージェント能力はマルチモーダル知能に何をもたらすか？）| 22 upvotes | https://huggingface.co/papers/2604.03016**
エージェント的な計画・ツール使用・反復推論を組み込んだ場合のマルチモーダル評価ベンチマーク Agentic-MME を構築・公開。
エージェント能力が静的 VQA 性能と乖離する事実を明らかにし、次世代 MLLM 開発の評価軸を刷新する。

**5. Test-Time Scaling Makes Overtraining Compute-Optimal（テスト時スケーリングで過学習をコスト最適化）| 15 upvotes | https://huggingface.co/papers/2604.01411**
推論時の計算量を増やすことで、通常は過学習とみなされる訓練済みモデルのコスト効率が逆転して最適になることを理論・実験で示す。
既存モデルの有効活用戦略に変革をもたらし、推論時スケーリング（chain-of-thought, best-of-N）研究の理論的根拠を強化。

## AI ニュース

**1. "I love you" "too": LLM Attention Explained | 4 pts | https://kaamvaam.com/machine-learning-ai/llm-attention-explanation/**
LLM のアテンション機構を「I love you」という例文を使いながら直感的に解説した教育コンテンツ。
アテンションの仕組みをゼロから理解したい開発者・研究者入門層に刺さる内容で、LLM リテラシー向上需要の高さを示す。

**2. Old AI is beating new AI. Here's why | 4 pts | https://qz.com/ai-generative-ai-chatbots-llm-machine-learning**
最新の大規模モデルが旧世代モデルに特定タスクで劣後するケースを分析した記事。
「大きければ良い」という通説に疑問を呈し、ドメイン特化・ファインチューニング戦略の重要性を再認識させる内容として業界で議論を呼ぶ。

**3. Experiments in LLMs – Fine tuning（LLM 実験記録 — ファインチューニング編）| 3 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/18/experiments-in-llms.html**
実務者が OpenAI モデルのファインチューニングを試行錯誤した詳細な実験ログ。
再現性の高い手順とハマりどころが共有されており、独自モデル構築を検討する中小チームへの参考価値が高い。

**4. Experiments in LLMs – OpenAI Functions（LLM 実験記録 — Function Calling 編）| 2 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/30/experiments-in-llms-3.html**
OpenAI の Function Calling 機能を実装する際の実践知見をまとめた記事。
エージェント構築の基礎技術として今も参照されており、ツール呼び出しパターンの設計ベストプラクティスが学べる。

**5. Experiments in LLMs – Vector DBs and Embeddings（LLM 実験記録 — ベクター DB & 埋め込み編）| 2 pts | https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/vector/embeddings/2023/06/23/experiments-in-llms-2.html**
ベクターデータベースと埋め込みを組み合わせた RAG 構成の実験記録。
RAG 実装の定番アプローチが具体的なコードとともに解説されており、社内知識検索システム構築の入門資料として引き続き有用。
