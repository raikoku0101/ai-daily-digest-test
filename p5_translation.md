## 1. 背景・動機 (Background & Motivation)
イベントカメラ（event camera）は従来カメラと異なり、各ピクセルが独立して輝度変化を検出する非同期センサです。高速動作・低消費電力・高ダイナミックレンジという特性を持ちますが、出力は疎な非同期イベントストリームであり、連続動画への変換が困難でした。特に長時間シーケンスでは時間的ドリフト（temporal drift）が深刻な問題となります。

## 2. 提案フレームワーク: LongE2V (Proposed Framework)
事前学習済みビデオ拡散モデル（video diffusion model）のプリオルを活用して、イベントベースの動画再構成・予測・フレーム補間を統合的に処理します。回帰手法がテクスチャをぼかしてしまう問題に対し、生成的アプローチで高品質な動画生成を実現します。

## 3. 主要技術革新 (Key Technical Innovations)
- **Autoregressive Unrolling（自己回帰展開）**: 長時間シーケンスを自己回帰的に処理し、時間的ドリフトを累積させない機構
- **Adaptive Context Switching（適応的文脈切り替え）**: コンテキストウィンドウを動的に管理し、長期的な時間的一貫性を確保
- **Reencoding Alignment with Cross Residual Correction**: フレーム補間における双方向時間的一貫性を保証
- **Event Voxel Density Augmentation**: 異なるセンサ解像度・密度への頑健性を実現

## 4. 実験・成果 (Experiments & Results)
動画再構成（reconstruction）・予測（prediction）・フレーム補間（frame interpolation）の3タスク全てで既存手法を上回る性能を達成。特に例外的な時間的一貫性とゼロショット汎化能力を実証。SIGGRAPH 2026に採択された高水準の研究成果です。

## 5. 応用と展望 (Applications & Future Work)
自律走行車のカメラシステム・産業ロボットの高速物体追跡・スポーツ映像の高速動作解析・天文観測等への応用が期待されます。今後はリアルタイム推論の最適化と、より多様なシーン条件への対応が課題です。
