## 1. Introduction (はじめに)

拡散トランスフォーマー(Diffusion Transformer; DiT)はテキスト→画像生成の主流アーキテクチャとなっていますが、「学習解像度レンジ(training range)を超える解像度での生成性能が低下する」という課題があります。既存の訓練不要なアプローチは推論時の注意機構(attention mechanism)を修正していますが、回転位置エンコーディング(Rotary Position Embeddings; RoPE)の外挿と注意スケーリングを組み合わせた手法では、異なる周波数特性を持つRoPE成分に対して一様でコンテンツ非依存的なスケーリングを適用しており、グローバル構造保持と細部忠実度(detail fidelity)の間にトレードオフが生じていました。

## 2. Method (手法)

提案手法SEGAは、各ノイズ除去ステップ(denoising step)において潜在表現(latent representation)の空間周波数構造(spatial-frequency structure)に従い、RoPE成分間で注意を動的にスケーリングします。「Spectral-Energy Guided Attention」という名称の通り、スペクトルエネルギー情報を活用することで、適応的なスケーリングを実現し、構造的一貫性(structural coherence)と細部忠実度の両方を改善します。訓練不要(training-free)な手法として設計されており、既存のDiTへの後付け適用が可能です。

## 3. Experiments & Results (実験と結果)

複数のターゲット解像度にわたってSEGAが高解像度合成(high-resolution synthesis)を一貫して改善することが実験的に示されました。提案手法は最先端の訓練不要ベースライン(state-of-the-art training-free baselines)を上回る性能を達成しており、既存手法との比較において優位性が確認されています。

## 4. Conclusion (結論)

本研究は訓練不要なアプローチとして解像度外挿(resolution extrapolation)の問題に対する実用的なソリューションを提供し、拡散トランスフォーマーの汎用性向上に貢献するものとなっています。既存モデルの追加学習なしに高解像度出力を得られることは、実用上の価値が高いです。
