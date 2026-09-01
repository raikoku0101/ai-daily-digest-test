## 1. Abstract（概要）

LightNav-0は、事前学習済みVLM（Vision Language Model）の空間的知能を引き出し、ロボット制御に統合する汎用embodied navigationモデルです。「dual-channel pointing」により、タスク・環境・ロボット体型に依存しない空間意図を表現し、残差ベクトル量子化（RVQ）アクショントークナイザーが具体的な軌跡に変換されます。2K+シーン、4K+時間のナビゲーションデータを用いた教師付き学習と強化学習を通じて、指示追従、物体ナビゲーション、視覚追跡を単一モデルで実現します。

## 2. Introduction（はじめに）

既存のembodied navigationシステムは、タスクや体型ごとに特化した設計を採用しており、異なる環境や条件への転移が困難です。「現代的なVLMは既に視覚的接地、空間推論、指示理解を備えており、これらを直接ロボット制御に活用すべき」という原則のもと、Qwen3-VL-4B-Instructを基盤として、タスク固有の予測ヘッドを導入せずに、語彙拡張と統一的教師付けにより一般的なnavigation能力を獲得させます。

## 3. Method（手法）

モデルアーキテクチャは、時間的に圧縮された視覚履歴と自然言語目標を入力として、まず「affordance point」（実行可能な方向）と「object point」（タスク目標の位置）のdual-channel pointing prefixを出力し、その後3層のRVQアクショントークンで10ステップのSE(2)軌跡を生成します。「temporally aware visual history compression」により、最近の観測は高解像度で、古い観測は低解像度でトークン予算を配分します。統一的な自己回帰的目的関数により、全タスクが同じトークン空間で学習されます。

## 4. Experiments（実験）

評価は三段階で実施されます。まずLightNav-ERチェックポイントが8つのembodied-reasoningベンチマーク（Point-Bench、RefSpatial等）でマクロ平均67.4%の最高スコアを達成。次にLightNav-0が10の公開シミュレーション設定で評価され、VLN-CE（R2R/RxR）では単眼条件で最高の成功率を、ObjectNav（MP3D/HM3D）では先行手法を上回る結果を示します。INSIGHT-Benchでは43.7%のSRで他の手法を大きく上回り、実世界デモでもゼロショット転移を実証。

## 5. Conclusion（結論）

本研究は、「コンパクトなVLMバックボーンが、タスク・環境・ロボット体型を横断する統一的で転移可能な基盤として機能し得る」という中心的仮説を実証しました。タスク固有コンポーネント排除による簡潔性、dual-channel pointingによる明示的な空間推論ステップ、RVQトークナイザーによる効率的な軌跡表現、および段階的な学習カリキュラム（ER mid-training→SFT→online RL）を組み合わせることで、単一モデルでの多様なnavigationタスク実行を実現し、embodied navigationの新しい設計原則を確立しています。
