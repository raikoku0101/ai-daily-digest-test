## 1. はじめに (Introduction)
トーキングビデオのキャラクター置換は外観と音声を同時に移植しながら動き・シーン・言語・音声映像タイミングを保持する必要がある。既存手法は映像と音声変換を別々に実施するため音声と口唇動作の同期が困難だった。UniSwapは単一の拡散トランスフォーマー内で両モダリティを統合処理する初のフレームワーク。

## 2. 関連研究 (Related Work)
ビデオキャラクター置換（MoCha、Wan-Animate等）と音声変換（Seed-VC、CosyVoice）は個別に発展。LTX-2のような拡散トランスフォーマーが相互参照注意による同期生成を実現。DMD（Distribution Matching Distillation）等の蒸留手法で30ステップから3ステップへの削減が可能に。

## 3. 方法論 (Method)
①Swap-and-Reconstruct データ合成: 実ビデオを目標とし姿勢プロキシで人物置換した視覚アイデンティティと音声変換を組み合わせた訓練対を構築。②三段階学習: ステージ1(In-context事前学習)→ステージ2(Decoupled Streaming Conditioning Maskでブロック因果生成)→ステージ3(Efficient Multi-LoRA Switchingで3ステップ蒸留)。③Feature-RoPE Decomposition: 回転位置埋め込みをキャッシュ特徴から分離し長形式生成の安定性を確保。

## 4. 実験と結果 (Experiments & Results)
AVSpeechコーパスで学習、短編(~10秒)・長編(1分)ベンチマークで評価。音声映像同期性: Sync-C 3.633(最高)、Sync-D 10.304(最低)を達成。生成速度13.6 FPS（従来比10〜100倍高速）。消融実験で各コンポーネントの有効性を確認。

## 5. 結論 (Conclusion)
トーキングビデオにおける統合音声映像アイデンティティ置換の初実装。Swap-and-Reconstruct事前学習から効率的蒸留まで実用的なストリーミング生成を実現しながら、長時間生成でのアイデンティティ安定性を維持することに成功。
