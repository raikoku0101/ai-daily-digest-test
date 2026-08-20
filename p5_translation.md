## 1. Introduction (はじめに)
単一段階逆合成（SSRS: Single-Step Retrosynthesis）はコンピュータ支援合成計画（CASP: Computer-Aided Synthesis Planning）の中心課題。従来モデルとLLMの間に性能差が存在し、「一つの目標分子から複数の妥当な反応経路が存在する」逆合成の一対多性が未解決。Top-KKプロンプティング手法で多様性を捉える新枠組みを構築した。

## 2. Method (手法)
二つのプロンプティングパラダイムを採用:
Top-1モード: 15個の異なるテンプレートで個別にプロンプトして回答生成。
Top-KKモード: 各テンプレートに「15個の異なる回答を提示せよ」という指示を追加し、反応空間の多様性をより広く探索。
訓練データ: 新規作成CREED-CCV-2+USPTO-XLデータセット（約4,560万個の検証済み反応）を使用。

## 3. Training (訓練)
C3LM（Chemistry Constraint-Consistent Language Model）を二段階で訓練:
第一段階 - 教師あり微調整（SFT: Supervised Fine-Tuning）: 異なるデータセットサイズと訓練モード（Top-1 vs Top-K）を比較。
第二段階 - 強化学習微調整（RFT: Reinforcement Fine-Tuning）: ChemCensorスコア（化学妥当性プロキシ）と新規性報酬を組み合わせた報酬関数を設計。

## 4. Experiments & Results (実験と結果)
評価: URSA-expert-2026（OODベンチマーク）とUSPTO-50K-test-mini、ChemCensorメトリクスで測定。
Top-KKへの移行: ほぼ全LLMで性能向上。Av.PT-Top-10（多様性指標）が2.5倍以上改善。
最終モデルC3LM-LFM2-RFT-CC-NR: URSA-expert-2026で従来型SSRSモデル（LocalRetro・MHNreact）を上回りSOTA達成。反応空間の補完的探索特性を実証。

## 5. Limitations & Ethics (制限と倫理)
制限: ChemCensorの化学妥当性代理指標としての不完全性、実験条件・溶媒・精製法を未考慮、テンプレートベース生成による化学空間の偏り、SMILES完全一致のみの多様性評価。
倫理: CASPのデュアルユース可能性の懸念から医薬品発見の正当目的に限定評価。制度的バイオセーフティ枠組み内での使用を前提。

## 6. Conclusion (結論)
Top-KKプロンプティングとChemCensor強化学習の組み合わせにより、化学的妥当性を認識したLLMが逆合成タスクでSOTA達成。4560万件の検証済み反応データと二段階訓練戦略が創薬AIの実用化を後押しし、化学空間の多様な探索能力を実証した。
