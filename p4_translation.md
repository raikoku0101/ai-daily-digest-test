## 1. はじめに (Introduction)

本論文は、テキスト記述に基づいて物理的に正確かつ視覚的に忠実な 4D 人物-物体相互作用 (HOI: Human-Object Interaction) を生成する課題に取り組んでいます。静的な 3D 人物と対象物を 3D Gaussian Splats (3DGS) で表現し、人物が物体と相互作用する動的シーンの合成を目標としています。既存手法の課題として、純粋な生成的アプローチは物理モデルを欠き「ゴーストアーティファクト」が発生し、運動学的フレームワークは物体を静的な小道具として扱うため、現実的な運動量転移を捉えられないと指摘されています。

## 2. 関連研究 (Related Work)

テキスト-4D 生成、人物-物体相互作用生成、および生成的 3D アニメーション分野の既存研究が網羅されています。「DreamFusion」「4D-fy」などの手法が視覚的事前情報に依存し因果関係の一貫性に欠けること、「AvatarGO」「InterDreamer」が幾何学的制約に基づくが力学的モデリング（質量・弾性）を欠くことが強調されています。

## 3. 手法 (Method)

PhyGenHOI は 3 つの段階で動作します。**(1) Scene Representation**: 人物を SMPL 拘束付き 3DGS、物体を MPM (Material Point Method) シミュレーションで表現。**(2) Agent Motion Synthesis**: 人物は Motion Diffusion Model (MDM) で生成、物体は物理シミュレーションで駆動。**(3) Physically-Aware Interaction Synthesis**: Windowed Attraction Loss で接触フレーム t* と接触関節 j* を速度プロファイルから自動判定し、Contact Detection and Re-simulation で物理的運動量転移、Masked Video-SDS で接触領域の視覚品質向上を実現します。

## 4. 実験と結果 (Experiments & Results)

10 個の異なる人物-物体相互作用シナリオでベンチマーク評価を実施。VQA Physics (0.25 vs 0.19/0.15)、ViCLIP (0.30 vs 0.24/0.26) でベースライン (4D-fy、AnimateAnyMesh) を大幅に上回りました。ユーザー研究では物理的妥当性 (Q1: 4.33/5)、接触品質 (Q2: 4.29/5) で優位性を示し、アブレーション研究により各コンポーネントの必要性が実証されました。

## 5. 結論 (Conclusion)

生成的人物運動と明示的な物理シミュレーションを統合する PhyGenHOI により、テキスト整合性と物理的妥当性の両立が実現されました。ゴーストおよび貫通アーティファクトの排除と動的な接触後応答が同時に達成され、4D コンテンツ作成における新たな可能性が開かれています。
