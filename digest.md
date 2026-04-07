# AI Daily Digest — 2026-04-07

## 今日のハイライト
- **Self-Distilled RLVR**（81 upvotes）: 外部報酬モデル不要の自己蒸留型強化学習でLLM推論能力を大幅向上。
- **Claude Code v2.1.92**: Bedrock設定ウィザード・モデル別コスト内訳・リモートセッション名改善など実用機能を多数追加。
- **ストリーミング動画理解のシンプルベースライン**（54 upvotes）: 複雑な専用アーキテクチャ不要で高精度なリアルタイム動画理解を実現。

## Claude Code / Anthropic アップデート

### v2.1.92（2026-04-04）
- `forceRemoteSettingsRefresh` ポリシー設定を追加
- インタラクティブな Bedrock セットアップウィザードを追加
- モデル別コスト内訳表示を追加
- サブエージェント生成に関するバグを修正
- Remote Control セッション名のデフォルトプレフィックスにホスト名を使用するよう変更

### v2.1.91（2026-04-02）
- アノテーション経由の MCP ツール結果永続化オーバーライドを追加
- `disableSkillShellExecution` 設定を追加
- ディープリンクで複数行プロンプトをサポート
- `bin/` ディレクトリ下のプラグイン実行ファイルをサポート

### v2.1.90（2026-04-01）
- `/powerup` インタラクティブレッスン機能を追加
- `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` 環境変数を追加
- `.husky` を保護ディレクトリに追加
- レート制限ダイアログの無限ループを修正
- プロンプトキャッシュミスのリグレッションを修正

## 注目論文 TOP 5

1. **自己蒸留型 RLVR（Self-Distilled RLVR）** ★81 upvotes — https://huggingface.co/papers/2604.03128
   外部報酬モデルや人手ラベルなしに、LLM自身の出力を教師信号として強化学習する自己蒸留フレームワークを提案。
   数学・コード・論理推論ベンチマークで既存 RLVR 手法を上回り、低コスト・高スケーラブルな推論強化の新基準を示す。

2. **ストリーミング動画理解のシンプルベースライン（A Simple Baseline for Streaming Video Understanding）** ★54 upvotes — https://huggingface.co/papers/2604.02317
   既存のマルチモーダル LLM にシンプルなフレームサンプリングと時系列埋め込みを組み合わせるだけでストリーミング動画を理解。
   専用アーキテクチャ不要で SOTA に匹敵する性能を達成し、リアルタイム監視・動画QA・ロボティクスへの応用に期待。

3. **Token Warping による近傍視点対応 MLLM（Token Warping Helps MLLMs Look from Nearby Viewpoints）** ★23 upvotes — https://huggingface.co/papers/2604.02870
   視点変換を「トークンのワーピング」として定式化し、マルチモーダル LLM が近傍視点の画像を効率的に処理できるよう改善。
   3D シーン理解・ロボット操作・自動運転など視点変化が伴うタスクでの精度向上に寄与。

4. **エージェント型マルチモーダル評価（Agentic-MME）** ★22 upvotes — https://huggingface.co/papers/2604.03016
   「エージェント能力」がマルチモーダル知能にどう貢献するかを系統的に評価する新ベンチマーク Agentic-MME を提案。
   ツール使用・計画・自己修正など能力ごとに分析し、現行モデルのボトルネックを明確化して次世代エージェント開発の指針を提供。

5. **テスト時スケーリングで過学習を計算最適化（Test-Time Scaling Makes Overtraining Compute-Optimal）** ★15 upvotes — https://huggingface.co/papers/2604.01411
   モデルを過学習させた後にテスト時スケーリング（推論時計算増大）を組み合わせることで全体的な計算効率が最適化されることを示す。
   学習コストと推論コストのトレードオフを再定義し、小規模モデルでも大規模モデルに匹敵する性能を引き出す可能性を示唆。

## AI ニュース

1. **古いAIが新しいAIに勝っている — その理由（Old AI is beating new AI. Here's why）** ★4pts — https://qz.com/ai-generative-chatbots-llm-machine-learning
   最新の大規模モデルが特定タスクで旧世代モデルに性能で劣るケースが増加していることを報告。
   パラメータ数・コスト増大にも関わらず実用性能が伸び悩む「AIの収穫逓減」問題を浮き彫りにし、効率重視の研究へのシフトを促す。

2. **LLM アテンション機構を直感的に解説（"I love you" "too": LLM Attention Explained）** ★4pts — https://kaamvaam.com/machine-learning-ai/llm-attention-explanation/
   Transformer のアテンション機構を「"I love you" に対して "too" を予測する」具体例でわかりやすく図解した解説記事。
   LLM の仕組みへの関心が高まる中、開発者・非専門家双方に向けた教育コンテンツとして注目を集めている。

3. **LLM 実験記録 Part 1 — ファインチューニング編（Experiments in LLMs – Fine Tuning）** ★3pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/18/experiments-in-llms.html
   実際のファインチューニング実験を通じて学んだ知見・ハマりどころ・ベストプラクティスを詳細にまとめた実践記録。
   再現性の高いノウハウが豊富で、独自モデルを構築したい開発者にとって実用的なリファレンスとして根強い人気を持つ。

4. **LLM 実験記録 Part 3 — OpenAI Functions 編（Experiments in LLMs – OpenAI Functions）** ★2pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/2023/06/30/experiments-in-llms-3.html
   OpenAI の Function Calling 機能を使ったツール統合の実装方法と落とし穴を実験ベースで解説。
   LLM をアプリに組み込む際の Function Calling 活用事例として、エージェント開発の基礎理解に役立つ。

5. **LLM 実験記録 Part 2 — ベクトル DB と埋め込み（Experiments in LLMs – Vector DBs and Embeddings）** ★2pts — https://adamfallon.com/ai/llms/deep-learning/machine-learning/artificial-intelligence/openai/vector/embeddings/2023/06/23/experiments-in-llms-2.html
   ベクトルデータベースと埋め込みを使った RAG（検索拡張生成）の構築実験をステップバイステップで記録。
   RAG システム構築に必要な基礎知識を実践的に学べる内容で、LLM アプリ開発入門として継続的に参照されている。
