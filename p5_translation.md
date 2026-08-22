## 1. はじめに（Introduction）
低リソース言語（ギリシャ語）での推論能力を持つようLLMを調整することに焦点。従来の精度ベンチマークでは改善が見えない一方、モデルの内部的推論プロセスに大きな変化が生じることを報告。基盤モデルはギリシャ語の質問に対しても英語で推論（reasoning in English）するため、ユーザーは推論過程を理解・監査・修正できない問題があった。

## 2. 手法（Method）
3つのMoE（Mixture-of-Experts）モデル（Alibaba・OpenAI・NVIDIA製、3.6-4.0B活性パラメータ）を対象に実験。SFT（Supervised Fine-Tuning：教師あり微調整）とRL（Reinforcement Learning：強化学習）による段階的調整で推論言語の制御性を向上。「6つの行動次元（six behavioral dimensions）」という独自評価指標を開発し、出力長との相関を排除する厳密な測定手法を採用。

## 3. 実験と結果（Results）
SFT後、約98%の項目でモデルは質問言語（ギリシャ語）での推論を実行。一方、RLにより「形式スキップ（format skipping）」（24%→2.5%）と「推論チャネルへの流出（reasoning channel leakage）」（3.5%→0.0%）という具体的欠陥を解決。精度のみを最適化しても言語習慣は変わらないことが判明。

## 4. 結論（Conclusion）
検証可能な報酬（verifiable rewards）を備えたRL手法により、SFTが解決できない問題を段階的に改善できることを実証。開発された評価ツールと制御手法は他の低リソース言語にも転用可能で、多言語LLM開発に新たな知見を提供する。
