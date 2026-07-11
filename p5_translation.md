## 1. Introduction (はじめに)
イベントカメラ（Event Camera / 神経形態カメラ）は、ピクセルごとの輝度変化を非同期かつマイクロ秒精度で検出するセンサーで、従来のフレームカメラと比較して動体ブラーがなく高ダイナミックレンジを実現する。しかし、イベントデータから長時間・高品質な動画を再構成・予測することは、時間的ドリフト（Temporal Drift）と双方向一貫性（Bidirectional Consistency）の確保が困難であり、未解決の課題となっていた。本研究は事前学習済み動画拡散モデル（Video Diffusion Models）の事前知識を活用してこれらの課題を解決する。

## 2. Related Work (関連研究)
E2VID・FireNet・SPADE-E2VID など既存のイベントベース動画再構成手法は短時間系列での性能は高いが、長時間になると累積誤差が増大する問題を抱えていた。拡散モデルを動画生成に応用した研究（VideoLDM・Stable Video Diffusion 等）の知識を、イベントデータという特殊な条件付き入力に適用する試みは本研究が先駆的。

## 3. Method (手法)
LongE2V の主要コンポーネント：
(1) **Autoregressive Unrolling（自己回帰的展開）**: イベント系列を段階的に処理し、長時間の時間的整合性を維持
(2) **Adaptive Context Switching（適応的文脈切り替え）**: 局所的・大域的文脈を動的に切り替え、時間的ドリフトを軽減
(3) **Reencoding Alignment with Cross Residual Correction（再エンコーディング整合 + 交差残差補正）**: フレーム補間時の前後フレームとの双方向一貫性を確保
(4) **Event Voxel Density Augmentation（イベントボクセル密度拡張）**: センサー解像度変動に対するロバスト性を向上

## 4. Experiments (実験)
MVSEC・HQF・BS-ERGB などの標準イベントカメラデータセットで評価。動画再構成（Video Reconstruction）・動画予測（Video Prediction）・フレーム補間（Frame Interpolation）の 3 タスクで包括的な実験を実施。PSNR・SSIM・LPIPS の定量指標を使用。

## 5. Results (結果)
全 3 タスクにおいて既存手法を上回る最先端性能（State-of-the-Art）を達成。特に長時間系列（100 フレーム以上）での時間的一貫性が従来手法を大幅に上回り、時間的ドリフトの抑制効果が定量的に実証された。

## 6. Conclusion (結論)
LongE2V は動画拡散モデルの事前知識をイベントカメラ処理に応用する有効性を示し、長時間イベントベース動画処理の実用的パイプラインを提供した。自動運転・スポーツ解析・高速ロボット制御など高速動体追跡が必要な実世界応用に対して、信頼性の高い動画処理基盤を実現する。
