# AI Daily Digest — 2026-05-06

## 今日のハイライト
- **SFT→RL の分布ドリフト問題**: 最多 upvote (25) の論文が、マルチモーダル LLM の標準ポストトレーニングである SFT→RL パイプラインの根本的問題を指摘。ブラックボックス蒸留による事前アライメントで解決策を提示。
- **Claude Code v2.1.129 リリース**: URL から直接プラグインを取得する `--plugin-url` フラグや自動アップデート機能を追加。`skillOverrides` 設定のバグも修正。
- **エージェント基盤研究の加速**: GUI エージェント (WindowsWorld)、Heavy Thinking (HeavySkill)、マルチエージェント RL (Orchestration Traces) と、エージェント系の論文が複数ランクイン。


## Claude Code アップデート

### v2.1.129 (2025-05-06)
- `--plugin-url <url>` フラグ追加：URLから `.zip` プラグインを取得してセッションに適用
- `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` 環境変数：Emacs `eat` など自動検出が失敗するターミナルで同期出力を強制有効化
- `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`：Homebrew/WinGet インストール時にバックグラウンドでアップグレードし再起動を促す
- Plugin manifests: `themes`/`monitors` は `"experimental": { ... }` 配下で宣言するよう変更（旧形式は警告）
- Gateway `/v1/models` モデル探索が `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` でオプトインに変更
- Ctrl+R 履歴ピッカーが全プロジェクト横断検索をデフォルトに戻した（Ctrl+S で現在プロジェクトに絞り込み）
- `skillOverrides` 設定が動作するように修正

### v2.1.128 (2025-05-04)
- `/color`（引数なし）でランダムセッションカラーを選択
- `/mcp` でサーバーのツール数を表示、0ツールのサーバーをフラグ表示
- `--plugin-dir` が `.zip` アーカイブを直接受け入れるように
- `EnterWorktree` がドキュメント通り `origin/<default-branch>` ではなくローカル HEAD から新しいブランチを作成するように修正

### v2.1.126 (2025-05-01)
- `/model` ピッカーがゲートウェイの `/v1/models` エンドポイントからモデルを一覧表示
- `claude project purge [path]` コマンド追加：プロジェクトの全 Claude Code 状態を削除
- `--dangerously-skip-permissions` が `.claude/`、`.git/`、`.vscode/` への書き込みプロンプトもバイパス
- `claude auth login` がブラウザコールバック未到達時（WSL2、SSH、コンテナ）に端末貼り付けで OAuth コードを受付

## 注目論文 TOP 10

**1. Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL**
- upvotes: 25 | arXiv: https://arxiv.org/abs/2604.28123
- SFT→RL という標準的なポストトレーニングレシピにおける分布ドリフト問題を指摘。SFT がモデルの元の能力を損ない、監督分布とも一致しないという課題に対し、ブラックボックスオンポリシー蒸留による「事前アライメント」手法を提案。マルチモーダル推論タスクでの性能を改善。

**2. WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments**
- upvotes: 9 | arXiv: https://arxiv.org/abs/2604.27776
- OSWorld 等の既存ベンチマークが単一アプリに限定されている問題を解決。複数アプリを横断する職業特化ワークフローを評価する「プロセス中心」ベンチマークを提案。実際のビジネス環境に近い複雑なタスク遂行能力を評価可能。

**3. HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness**
- upvotes: 6 | arXiv: https://arxiv.org/abs/2605.02396
- 複雑なエージェントフレームワーク内で実際に性能を駆動するメカニズムを解明。「Heavy Thinking（深い思考）」をエージェントのインナースキルとして位置づけ、複雑な推論タスクにおける性能向上の本質的要因を特定。

**4. PatRe: A Full-Stage Office Action and Rebuttal Generation Benchmark for Patent Examination**
- upvotes: 3 | arXiv: https://arxiv.org/abs/2605.03571
- 特許審査を分類・抽出タスクとしてのみ捉えていた既存研究を超え、審査意見書と意見書反論の生成を含む完全な反復プロセスをベンチマーク化。学術的なピアレビューと同様のインタラクティブな性質を評価。

**5. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces**
- upvotes: 2 | arXiv: https://arxiv.org/abs/2605.02801
- LLM エージェントが孤立したツール利用者から協調チームへ進化する中、タスクの生成・委任・通信・集約・停止を含むオーケストレーショントレース（時系列インタラクショングラフ）を通じた強化学習手法を研究。

**6. SVGS: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors**
- upvotes: 2 | arXiv: https://arxiv.org/abs/2411.18966
- 既存の Gaussian Splatting が単一の視点依存色と不透明度のみを持つ非コンパクト表現という限界を克服。空間的に変化する色を持つプリミティブを導入し、多視点再構成の品質と表現効率を改善。

**7. SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment**
- upvotes: 2 | arXiv: https://arxiv.org/abs/2605.04012
- 臨床専門家と同等以上の診断能力を示す言語モデルを、実際の患者が日常生活で症状を報告するシナリオに適用。複雑な症例ではなく日常的な症状報告における AI の実用性を検証した実証研究。

**8. Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies**
- upvotes: 2 | arXiv: https://arxiv.org/abs/2605.03596
- ワーカーのワークスペース内の異種ファイル間の明示的・暗示的な依存関係を AI エージェントが識別・推論・活用・更新する能力を評価。既存ベンチマークの合成ファイルの限界を超え、実世界の大規模ファイル依存関係を扱う。

**9. SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion**
- upvotes: 1 | arXiv: https://arxiv.org/abs/2605.01466
- 点群補完における 2D-3D マルチモーダル学習のメカニズムを解明。標準的なハード投影が疎な点群から視覚的事前情報の伝播を妨げることを特定し、Gaussian Soft Splatting とアテンションで解決。

**10. TCDA: Thread-Constrained Discourse-Aware Modeling for Conversational Sentiment Quadruple Analysis**
- upvotes: 1 | arXiv: https://arxiv.org/abs/2605.01717
- 会話型アスペクトベース感情4要素分析（DiaASQ）において、GCN の構造ノイズと標準 RoPE の平坦な相対距離捉え方という問題を解決。スレッド制約と談話認識モデリングで複数ラウンド対話の複雑な相互関係を効果的に捉える。

