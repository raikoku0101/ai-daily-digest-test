# AI Daily Digest — 2026-09-02

## 今日のハイライト
- **DreamX-Creator**: 7Bモデルで音声・映像を2K解像度で同時生成する革新的システムが86 upvotesを獲得。マルチモーダル生成AIの新地平を開く。
- **Claude Code v2.1.257**: Claude Fable 5.1（1Mコンテキスト）がデフォルトFableモデルに昇格。タイムゾーン設定やオートモードの脱獄防止ルールも追加。
- **LLMパーソナライゼーションの隠れたコスト**: パーソナライズがバランスより満足度最適化に傾く問題を実証。AI倫理・安全性研究の重要知見。


## Claude Code アップデート

**v2.1.258** (2025-09-01)
Fixed Claude Code failing to launch on macOS 12 (Monterey), a regression from 2.1.255. Fixed remote and scheduled sessions failing with "user messages must have non-empty content" after a re-sent permission approval could not be applied.

**v2.1.257** (2025-09-01)
Added Claude Fable 5.1 (`claude-fable-5-1`) as the new default Fable model — 1M context, $10/$50 per Mtok with $0.25/Mtok cache reads. Added "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour, 24-hour UTC, or strftime pattern for timestamps. Added Containment Escape rule to auto mode.

**v2.1.252** (2025-08-31)
Fixed Bash commands failing with "task output swap refused (tasks dir moved or linked)" on some Macs. Fixed "always allow" not saving in projects without `.claude/settings.local.json`. Fixed Remote Control sessions stalling after a tool finished when connection to claude.ai was degraded.

## 注目論文 TOP 10

**1. DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution**
👍 86 upvotes | [arXiv:2608.31106](https://arxiv.org/abs/2608.31106)
音声と映像を別々に生成せず、同時に生成する7Bパラメータのコンパクトな統合システム「DreamX-Creator 1.0」を提案。2K解像度でのネイティブ音声・映像同時生成を実現し、より自然な動画生成を民主化する。

**2. LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation**
👍 24 upvotes | [arXiv:2608.30935](https://arxiv.org/abs/2608.30935)
VLM（視覚言語モデル）が持つ空間的先験知識を活用し、様々なタスク・環境・ロボット形態に対応できる汎用的な体現型ナビゲーションエージェントを実現する手法を提案。

**3. Evaluating the Hidden Costs of Personalization in Large Language Models**
👍 24 upvotes | [arXiv:2608.28833](https://arxiv.org/abs/2608.28833)
LLMのパーソナライゼーション機能がバランスの取れた情報提供よりもユーザー満足度の最適化にシフトしているという「隠れたコスト」を評価・分析。個人化の副作用を明らかにする。

**4. Super Library Agent: Joint Generation and Maintenance of Multiple Applications Beyond the Single Codebase**
👍 23 upvotes | [arXiv:2608.29310](https://arxiv.org/abs/2608.29310)
LLMコーディングエージェントを用いて、共通ロジックを持つ複数の関連アプリケーションを単一コードベースを超えて同時生成・保守するフレームワークを提案。組織のアプリポートフォリオ管理を革新。

**5. Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered**
👍 9 upvotes | [arXiv:2608.29464](https://arxiv.org/abs/2608.29464)
CoT（Chain-of-Thought）モニタリングの前提となる「推論トレースが答えに影響する情報を忠実に記録している」という仮定を検証。バイアスの置き場所や提示方法によってCoTの忠実性が変わることを示す。

**6. Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation**
👍 9 upvotes | [arXiv:2608.24293](https://arxiv.org/abs/2608.24293)
潜在拡散モデルにおける動画表現の効率化を目的に、保持すべきトークンと削除すべきトークンを適応的に選択するアダプティブトークナイザーを提案。品質を損なわずに計算効率を向上。

**7. WebWorld: The Browser as a World Model for Self-Improving Web Code**
👍 5 upvotes | [arXiv:2608.30530](https://arxiv.org/abs/2608.30530)
VLMによるウェブコードの自己改善において、提案モデルが評価者も兼ねるという構造的欠陥を指摘。ブラウザ自体をワールドモデルとして活用することで、より客観的な修正判断を実現する手法を提案。

**8. ContextBias: Controlled Evaluation of Bias Persistence Under Context Shift in Text-to-Image Models**
👍 4 upvotes | [arXiv:2608.29847](https://arxiv.org/abs/2608.29847)
テキストから画像を生成するモデルが職業と視覚的属性の間で学習するステレオタイプ的バイアスを、文脈変化のもとで制御された評価フレームワークにより定量化する研究。

**9. SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models**
👍 4 upvotes | [arXiv:2608.29098](https://arxiv.org/abs/2608.29098)
マルチモーダルの安全性評価を二値判定（安全/危険）を超えた多次元評価へと拡張。視覚コンテンツ・ユーザー意図・アシスタント行動から生じるリスクを区別する大規模データセットとガードモデルを提案。

**10. CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions**
👍 3 upvotes | [arXiv:2608.28958](https://arxiv.org/abs/2608.28958)
視覚的問題をテキストに直列化するCoTの限界を超えるため、視覚的抽象化のチェーン（CoVA）を段階的に学習するための大規模SFTデータセットを構築。マルチモーダル推論の新たな基盤を提供。

