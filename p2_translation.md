## 1. Introduction (はじめに)

既存の拡散ベースのポーズ駆動型人間アニメーションシステムは数分〜数時間を要し、インタラクティブ応用に不向きでした。LiveAnimateは14Bパラメータの動画拡散トランスフォーマー（Video Diffusion Transformer: DiT）を基盤とし、リアルタイムストリーミングと安定した長形式生成を同時に実現する初のシステムです。2×H100 GPU上で約20FPSの生成を達成し、3分間にわたり知覚品質を維持します。

## 2. Related Work (関連研究)

Wan・Stable Video Diffusionなど14Bパラメータ大規模モデルへのスケーリング動向、Animate Anyone・MagicAnimate・UniAnimate-DiTなどのポーズ駆動アニメーション手法、Self Forcing・Causal Forcingなど自己回帰動画生成の曝露バイアス（Exposure Bias）低減手法を概観し、これらの知見をLiveAnimateの設計に統合しています。

## 3. Method (手法)

**段階1・Reference-Anchored Teacher-Forcing Adaptation（参照アンカー付き教師強制適応）**: 事前学習済みの双方向DiTをブロック因果的生成器（Block-Causal Generator）に適応。Ref Sinkが参照画像の潜在KV状態を全ブロックに可視化し、恒久的なコンテキストアンカーとして機能します。

**段階2・Block-wise Self-Forcing Distillation（ブロック単位の自己強制蒸留）**: 除去ステップを50から3に削減。2パス手法で全軌跡生成後にブロック単位で逆伝播し、メモリ効率を維持しながら分布マッチング信号を供給します。

**Pose-Retrieval Sink Attention（ポーズ検索シンクアテンション）**: Static Sink（最初のブロックを恒久固定）・Dynamic Sink（ポーズマッチ歴史ブロック）・3スロットRolling Windowを組み合わせ、有限KVキャッシュ内で関連コンテキストを復元します。

**システム最適化**: Ulysses型列並列化で注意計算をGPU間に分散、torch.compileによるカーネル融合を実装。

## 4. Experiments (実験)

3分間ベンチマーク（24参照画像・駆動動画ペア）で評価。短期品質でASE 2.823・IQA 4.047を達成。長期安定性では最初の30秒から最終分まで知覚品質とアイデンティティがほぼ一定を実証。既存手法が2〜5時間要する中、LiveAnimateは約4分で処理完了（19.63 FPS）。

## 5. Conclusion (結論)

LiveAnimateはリアルタイムストリーミング・安定した長形式生成・10億規模パラメータを同時達成する初のシステムとして定位されます。ライブストリーミング・テレプレゼンス・仮想アバターといったインタラクティブ応用への実用的な道を開きます。
