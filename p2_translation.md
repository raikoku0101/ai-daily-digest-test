## 1. Introduction (はじめに)

本研究は音楽に基づいてダンス動画を自動生成するタスクに取り組んでいます。オンラインダンス動画プラットフォームの普及とAIGC技術の進展により、このタスクが重要な研究課題として浮上しています。既存の3Dダンス生成やポーズ駆動型画像アニメーション技術は、ダンス動画生成にはそのまま適用できません。主な課題は「運動学的に妙当で芸術的に表現豊かなダンス動作の生成」と「高忠実度の視覚的外見と時空間的一貫性の実現」です。

## 2. Related Work (関連研究)

音楽駆動3Dダンス生成の研究は、GAN、自己回帰モデル、拡散モデルの3つのカテゴリに分類されます。一方、ポーズ駆動型画像アニメーション技術も進展していますが、"pose design remains manual"という課題があります。既存のダンス動画生成研究は限定的で、"compromised motion quality and visual appearance"という問題を抱えています。

## 3. Methodology (手法)

MACE-Danceは「Motion Expert（モーション専門家）」と「Appearance Expert（外見専門家）」の2つの専門家モジュールで構成されています。

Motion Expertは拡散モデル（Diffusion Model）のBiMamba-Transformerハイブリッドアーキテクチャを採用します。BiMamba（双方向Mamba）は音楽やダンスの局所的依存性をモデル化し、Transformerは交差モーダルの大域文脈をキャプチャします。Guidance-Free Training（GFT）戦略を使用して、従来の分類器なし案内（CFG）より効率的で安定した生成を実現します。

Appearance Expertは Wan-Animateベースのアーキテクチャに「運動学的段階」と「美的段階」の2段階ファインチューニング戦略を採用。運動学的段階ではBody Adapterを強化し、美的段階ではLoRA（Low-Rank Adaptation）パラメータを最適化します。3D SMPL表現を中間表現として採用することで"3D provides view-invariant and physically consistent supervision"を実現しています。

## 4. Experiment (実験)

70,000クリップ（5【10秒）、記16時間のダンス動画データセット「MA-Data」を構築　3Dレンダリング（20,000クリップ）とインターネット動画（50,000クリップ）の2つのソースから構成。評価メトリクスは運動次元（FID、DIV、BAS）と外見次元（IQ、AQ、SC、BC、MS、TF）から多角的に評価。MACE-Danceは音楽駆動ダンス動画生成タスクで最先端性能を達成。Motion ExpertはSOTA、Appearance Expertはポーズ駆動アニメーションでもSOTA達成。

## 5. Conclusion (結論)

MACE-Danceは運動生成と視覚合成を効果的に分離することで、"kinematically plausible and artistically expressive"なダンス動画生成を実現しました。今後は、テキスト説明による条件付け機能の拡張と、リアルタイム処理対応を計画しています。
