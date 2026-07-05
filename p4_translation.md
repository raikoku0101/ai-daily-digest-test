## 1. Introduction (はじめに)
LLM エージェント（LLM agents）においてスキル（Skills）が再利用可能な操作層として機能するようになりましたが、スキルリポジトリ内の重複スキルが確実なスキル利用を困難にしています。最終検証成功のみを評価指標とすると試行錯誤による偽陽性が生じ、プロセス品質評価の必要性が本研究の動機となっています。

## 2. Method (手法)
SkillCoach フレームワークは自己進化型ルーブリック（Self-Evolving Rubrics）を採用。スキル選択（Skill Selection）・スキル追従（Skill Following）・スキル合成（Skill Composition）・スキル根拠反省（Skill-Grounded Reflection）の 4 次元で軌跡（trajectory）を評価。外部検証器（verifier）と独立した信号として機能し、結果の偶然成功とプロセス品質を区別します。ルーブリック自体も継続的に学習・改善されるセルフエボルビング設計を実装。

## 3. Experiments & Results (実験・結果)
進化したルーブリックが評価品質を大幅に向上させ、最終精度の背後に隠された失敗パターンを露出させることを実証。結果のみのフィルタリングよりも強力な教師信号（Supervision Signals）を提供し、エージェント的スキル利用（Agentic Skill-Use）の向上に貢献することを確認しました。

## 4. Conclusion (結論)
プロセス監督（Process Supervision）によるエージェント訓練の新しいアプローチを確立。スキルベース LLM システム開発における評価と改善の実践的フレームワークを提供し、AI エージェントの品質保証に新しい評価基準を提示します。
