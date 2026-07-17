## 1. Introduction (はじめに)
複数の参照画像と文字指示に基づいて一貫性のある音声映像コンテンツを生成する「多参照音声映像（MR2AV: Multi-Reference-to-Audio-Video）生成」という新興タスクを扱う。既存のベンチマークは単一参照の主体保持やテキスト駆動生成に焦点を当てているが、MR2AVが必要とする「複数参照の同時推論」と「音声映像の同期生成」という課題は未解決。

## 2. Method (手法)
MultiRef-Compass は350個の厳選サンプルで構成される統合ベンチマーク。

**資産合成パイプライン（Asset-Composition Pipeline）**: スケーラブルなパイプラインにより以下をカバー:
- 多視点主体保持（Multi-View Subject Preservation）
- 複数エンティティ結合（Multi-Entity Composition）
- 人物・物体・シーン構成

**評価プロトコル** - 4次元・14メトリクス:
1. 基本品質（Basic Quality）: 映像・音声の基本的な生成品質
2. 参照一貫性（Reference Consistency）: 参照画像との視覚的整合性
3. 音声映像同期性（Audio-Visual Consistency）: 音声と映像の同期
4. 指示追従性（Instruction Following）: テキスト指示への準拠

自動メトリクスと「再判定強化型MLLM評価器（Rejudging-Enhanced MLLM-as-a-Judge Framework）」を統合し、知覚忠実度と参照条件付き合成の両方を評価。

## 3. Experiments & Results (実験と結果)
8つの代表的なMR2AVシステムに対する実験では、複数の評価次元全体で改善の相当な余地が明らかになった。特に複数参照の同時推論と音声映像の同期生成において、既存モデルの性能が大きく低下することを確認。

## 4. Conclusion (結論)
MultiRef-Compass は MR2AV 生成の体系的な評価基盤を初めて提供する。8システムの評価から浮かび上がった課題（複数参照の同時推論・音声映像同期）が、将来の研究方向を示す重要な指針となる。
