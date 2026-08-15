## 1. はじめに (Introduction)
ポーズ駆動型人間アニメーションは参照画像とポーズシーケンスから対象者のビデオを合成するタスクで、ライブストリーミング・テレプレゼンス・バーチャルアバターへの応用が期待されている。従来のビデオ拡散モデル（Diffusion Transformer, DiT）は高品質だがリアルタイム生成不可。本研究は144億パラメータDiTでリアルタイムストリーミングと安定長時間生成を両立させる初のシステムを提案。

## 2. 関連研究 (Related Work)
ビデオ拡散モデルはU-NetからDiTへ進化し、Stable Video DiffusionやWanなど144億パラメータスケールが登場。ポーズ駆動ではAnimateAnyone・MagicAnimateが基準だが全てオフライン処理。自己回帰的生成ではDiffusion Forcing・Self Forcingが訓練・推論ギャップを軽減している。

## 3. 手法 (Method)
3つの主要コンポーネントで構成。①Reference-Anchored Teacher-Forcing Adaptation: 事前学習済み双方向DiTを参照画像を常に可視化するRef Sinkと共にブロック因果的生成器に適応。②Block-wise Self-Forcing Distillation (BS-DMD): 50ステップから3ステップへ推論ステップを削減し、単一8×80GB GPUノードで訓練可能。③Pose-Retrieval Sink Attention (PR-Sink): Static Sink + Dynamic Sink（ポーズ類似度で選択）+ Rolling Windowの組み合わせで、メモリと遅延をストリーム長に非依存化。

## 4. 実験 (Experiments)
3分間ベンチマーク（24クリップペア）でASE・IQA・DINO-S・FID・V-MAEを計測。UniAnimate-DiT・SCAIL・Wan-Animate・EverAnimate・One-to-Allと比較。ポーズ繰り返し場面での外観維持を特に評価。

## 5. 結果 (Results)
LiveAnimateは初段30秒でIQA 4.047を達成し最終段でIQA 4.026と安定。比較手法は出現ドリフト（One-to-AllはIQA 3.402→1.786に低下）やちらつきを示した。2×H100 GPUで19.63 FPS（ブロック時間0.611秒）を実現。Ulysses配列並列化で単一GPUの12.41 FPSから1.58倍加速。

## 6. 結論 (Conclusion)
リアルタイムストリーミングと安定長時間生成を同時に実現する初の144億パラメータアニメーションシステム。今後は高解像度・複数人対応・大規模カメラ動作への拡張が課題。
