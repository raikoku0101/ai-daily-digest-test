## 1. Introduction (はじめに)
既存の自己回帰型リアルタイム音楽生成システム（例: Lyria RealTime）はチャンク境界でのみ制御更新が可能だが、拡散モデルベースのアプローチにより「フレーム単位での制御と応答性の両立」を目指したのがDEMON（Diffusion Engine for Musical Orchestrated Noise）である。RTX 5090上で60秒の楽曲を毎秒12.3回生成でき、ノイズ除去強度パラメータ（denoising parameter）がリアルタイム演奏コントローラとして機能する。

## 2. Architecture (システムアーキテクチャ)
DEMONは5段階パイプラインで構成される。StreamDiffusionのリングバッファに改良を加え、各スロットが独立したタイムステップスケジュール（Per-slot heterogeneous denoise scheduling）を保持することで、連続的なパラメータ変更時のキュー消失を回避する。「Shared mutable per-step state（共有可変ステップ状態）」により、SDE（確率微分方程式）ソース混合曲線などのパラメータが毎ステップ読み込まれ、次の81msティックで即座に効果が反映される。Windowed VAE decodeにより全潜在表現ではなく再生ウィンドウのみをデコードし8倍高速化。TensorRT mixed-precision（fp16+fp32）で加速。

## 3. Performance Results (性能評価)
デコーダTensorRT forward passは60秒生成でB=1時13.3ms・B=8時80.6ms。Windowed VAE decodeは56msから7msへ削減（8倍高速化）。RTX 5090/4090/3090で同一の伝播パターンを±0.02RMS以内で再現。Windowed VAE出力は16-bit PCM renditionでフルデコードとbit-identical（SNR=∞）を確認。

## 4. Control Parameters (制御パラメータ設計)
ODE/SDEソルバー統合で6種の「フレーム毎ノイズ除去ダイナミクス曲線（Per-frame denoising-dynamics curves）」を制御軸として公開する。「SDE source blending（SDE再ノイズステップにおけるソースブレンディング）」により、各フレーム独立にモデル予測とソース潜在へのアンカリング強度を操作できる。x0-target morphにより独立した事前計算ターゲット潜在への段階的ブレンドも可能。

## 5. Conclusion (結論)
StreamDiffusion型リングバッファを長形式音声領域に適用し、Per-slot scheduling・Shared mutable state・SDE source blending・Windowed VAEの4機構を組み合わせることで、消費者向けGPU上のリアルタイム音楽制御楽器を実現。提案する伝播クラス分類は画像拡散を含む一般的リングバッファ系に応用可能であり、「広範・応答性を両立した演奏可能な生成インターフェース」という新しい設計空間を開拓した。
