## 1. Abstract（概要）

本研究は、画像安全フィルタリング（image guardrails）がポリシー変更に対応できない問題に取り組みます。"PolicyShiftBench"という2,000個のポリシー判別インスタンスを含むベンチマークを導入し、同一画像が異なるポリシー下で許可・制限される現実的シナリオを評価します。提案手法PolicyShiftGuardは、Randomized Policy SFT（RP-SFT）とBoundary-Pair Policy Adaptation（BP-Adapt）を組み合わせた二段階学習で、ポリシー適応性を大幅に改善し、既存VLMsより優れた性能を達成します。

## 2. Introduction（はじめに）

既存の画像安全フィルタリングモデルは固定ポリシー下で訓練・評価されており、安全性を画像固有の特性として扱っています。しかし実運用では同じ画像が製品・プラットフォームによって異なる許可状況に置かれます。本論文はこのポリシー適応性（policy adaptivity）の問題に焦点を当て、モデルが現在のポリシー定義に適応し、未見のポリシーにも一般化する能力が必要であることを主張します。

## 3. 提案手法（Method）

二段階訓練プロセスを採用します。第一段階のRP-SFT（Randomized Policy SFT）でポリシー条件付きプロンプトを用いた多様な訓練を実施。第二段階のBP-Adapt（Boundary-Pair Policy Adaptation）では、同一画像を「許可するポリシー」と「ブロックするポリシー」のマッチングペアで対比損失関数を使って学習。画像レベルの安全性バイアスに依存せずポリシー適応能力を強化します。

## 4. 実験結果（Results）

PolicyShiftBenchにおいて、7Bモデルは76.9 Avg. F1スコアと72.1 Avg. PSS（Policy Shift Score）を達成し、既存VLMsと専門的フィルタリング手法を上回りました。UnSafeBenchとSafeEditBenchへの転移性能も良好であり、アブレーション実験はマッチングペアがポリシー適応の安定性に不可欠であることを確認しています。
