## 1. Introduction (はじめに)
長期的なロボット操作（Long-Horizon Manipulation）には、個別スキルの確実な実行と、それらの連貫した配列が必要とされます。「階層的VLA（Vision-Language-Action）モデルの多くは単一の前向き伝播（Single Forward Pass）で決定を下すため、困難または重要な選択肢に追加計算を割り当てるメカニズムが欠けている」という課題が指摘されています。

## 2. Method (手法)
τ₀-VLAは、世界モデル誘導テスト時間計算（World-Model-Guided Test-Time Computation）を通じて、高レベルのサブタスク生成を計算スケーラブルな推論問題として定式化します。実行メモリ（Execution Memory）を使用し、必要に応じて代替案を探索してから出力にコミット。低レベルポリシー（Low-Level Policy）は、複数のロボット具体化（Embodiments）にわたってサブタスクを実行します。

## 3. Experiments & Results (実験と結果)
40,115時間のマルチモーダル実世界データを用いて訓練されました。テスト時間計算（Test-Time Computation）を追加割り当てすることで、次のサブタスク予測精度が大幅に向上し、長期操作タスクでの閉ループ（Closed-Loop）成功率の向上につながることが実証されています。階層的アーキテクチャにより、複数のロボット具体化での汎化性能も確認されました。
