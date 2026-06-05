## 1. Introduction (はじめに)
VLA (Vision-Language-Action) モデルは VLM の豊富な知識を活用するが、VLM のセマンティック空間と具現化制御ポリシーの構造的不一致が正確な知覚-行動マッピングを阻害している。本研究はタスク指向の中間表現として「アフォーダンス (affordance)」を導入し、知覚と行動をより正確に橋渡けする枠組みを提案する。

## 2. Method (手法)
AffordanceVLA は Mixture-of-Transformer (MoT) アーキテクチャで3専門家モジュールを構成：(1) Understanding Expert: 視覚+言語のセマンティック表現を抽出、(2) Affordance Generation Expert: Which2Act（何をするか）・Where2Act（どこで）・How2Act（どのように）の3要素を予測、(3) Action Expert: 中間表現から実制御行動を生成。UAA (Understanding-Affordance-Action) プログレッシブアテンション機構でアクション情報がアフォーダンス予測段階に漏洩することを防止。

## 3. Training Strategy (訓練戦略)
3段階プログレッシブ訓練：Stage I は VQA データセット (AGD20K・RefSpatial・PRISM) でアフォーダンス基盤構築、Stage II は大規模合成ロボットデータ (InternData-A1) で共訓練（自動パイプラインで約 100,000 アフォーダンスラベル生成）、Stage III は目標タスク (LIBERO・CALVIN・実世界) への適応微調整。注釈パイプラインは Claude Opus 4.5 で長時間指示を分解し Qwen3-VL で視覚-言語アフォーダンス注釈を生成。

## 4. Experiments (実験)
シミュレーション：LIBERO ベンチマーク平均 95.8%、CALVIN ABC→D 平均チェーン長 4.33。実世界：基本タスク 88.3% 成功率、複雑タスク (引き出し・トースター操作) で Pi0 比約 2 倍の成功率。アブレーションで MoT アーキテクチャ・3アフォーダンス要素・UAA 機構それぞれの有効性を確認。

## 5. Key Findings & Conclusion (主要知見と結論)
アフォーダンス中間表現による監督で VLM のセマンティック理解を保ちながら物理的実行能力を強化できることが明らかに。データ量よりも表現品質が性能天井を決定することも示唆。構造化アフォーダンス予測は直接 E2E マッピングや映像予測より優れた知覚-行動マッピングを実現し、シミュレーション・実世界両領域で堅牢な性能と高い汎化性を達成した。
