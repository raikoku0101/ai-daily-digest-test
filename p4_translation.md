# Generative World Renderer at the Speed of Play (AlayaRenderer-Flash)

## 1. Introduction (はじめに)
テキストプロンプトのみから画像を生成する従来アプローチと異なり、本研究はゲームエンジンが出力するG-buffer（幾何・材質情報）を条件とした生成型レンダラーを提案する。AlayaRendererは高品質なレンダリングを実現するが、50ステップの拡散プロセスにより「0.56 FPS」という低速だった。AlayaRenderer-Flashは自己回帰ストリーミング・4ステップ蒸留・軽量コーデックにより「31.54 FPS」の実時間レンダリングを実現し、ゲームプレイ中の即時スタイル変更を可能にする。

## 2. Method (手法)
4つの核技術で構成:
- **(1) G-buffer条件付き潜在空間レンダリング**: Wan VAEを用いたマルチモーダル条件付けにより、シーン構造を保持
- **(2) 自己回帰ストリーミング（Autoregressive Streaming）**: 固定長チャンク単位での逐次生成で無制限長シーケンスに対応、テキストプロンプトの動的変更を支援
- **(3) 段階的蒸留（Progressive Distillation）**: ガイダンス蒸留→段階的ステップ削減→Mean Flow Distillation の3段階で50ステップから4ステップへ安定的に圧縮
- **(4) 軽量コーデック（Lightweight Codec）**: G-buffer encoder・VAE decoderを蒸留で小型化し推論レイテンシを削減

## 3. Experiments (実験)
Black Myth: Wukongデータセット（訓練1,352クリップ、テスト131クリップ）で評価。測定指標: CLIP画像類似度（内容保持）・時間的LPIPS（フリッカー抑制）・境界一貫性（ウィンドウ間滑らかさ）・CLIPマージン（プロンプト制御性）・FPS・メモリ使用量。段階的設計分析で各コンポーネントの寄与度を定量化。

## 4. Results (結果)
AlayaRenderer-Flashは「SCLIP-IS: 0.847」の高い内容保持と「FPS: 31.54」の実時間性能を両立。RGB↔XやFrameDiffuserを上回る時間的安定性を達成し、プロンプト切り替えでも自然な遷移を実現。SuperTuxKartへの統合実験で単一H200 GPU上で「30 FPS」の実運用を確認し、ゲーム内リアルタイム視覚スタイル変更が実用化された。

## 5. Conclusion (結論)
自己回帰ストリーミング・段階的4ステップ蒸留・軽量コーデックの統合により、オフライン拡散レンダラーをインタラクティブなストリーミング生成レンダラーへ変換することに成功。レンダリング品質とプロンプト制御性を保持しながら実時間性能を達成し、「AI-nativeなインタラクティブ環境（AI-native interactive environment）」構築への実用的な道筋を示す。
