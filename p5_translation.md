## 1. Introduction (はじめに)
小児の歩行パターン分析は脳性麻痺などの発達障害や神経筋疾患（Neuromuscular Disorders）の診断に重要ですが、従来の3Dモーションキャプチャシステムは高額で小児に負担が大きい問題がありました。本研究ではRGBカメラを用いた「小児歩行の細粒度ビデオ分析（Fine-Grained Children's Gait Analysis from Video）」という新たな課題を定義し、臨床的に意味のある歩行品質評価を実現します。

## 2. Dataset: CGV (Children Gait Video)
CGVは110名の小児患者から収集した1,185本のビデオ（339,236フレーム）を含む臨床グレードのデータセットです。各ビデオはEdinburgh Visual Gait Score（EVGS）の17項目で注釈付けされています。SAM 3とSapiens-2Bによる自動抽出後に臨床医が手動調整した姿勢情報・セグメンテーションマスク・バウンディングボックスを含みます。専門家間一致度はICC=0.93と高い精度を示します。

## 3. Challenges (小児歩行分析の課題)
3つの主要課題があります：(1)成人データで学習した基盤モデルが小児の異なる骨格比率に対応できない問題、(2)臨床評価が位相依存的（Phase-Dependent）で細粒度の評価が必要な点、(3)療法士や保護者による遮蔽（Occlusion）や複雑な視覚的混乱が生じる点です。

## 4. Experiments & Results (実験と結果)
Gemini 3 Pro・GPT-5.2・Qwen3-VL等の最新マルチモーダルLLMを評価すると平均精度は50〜60%で、視覚的に明らかな異常は検出できますが微細な運動学的偏差（Kinematic Deviations）の捕捉に失敗します。VideoMAE v2を微調整すると69〜72%を達成。提案するChildGait-Videoは、Token-Level Kinematic Prompting（骨格キーポイントのレンダリング）とMask-Guided Patch Pruning（背景除去による重要領域集中）を組み合わせ、70〜93%の精度を達成（McNemar検定：p=2.3×10⁻⁴で統計的に有意）。16フレーム（0.53秒）が最適なバランスを提供します。

## 5. Conclusion (結論)
CGVデータセットとChildGait-Videoフレームワークを提示した研究です。現在のMLLMおよび微調整VLMは臨床的歩行スコア推定に信頼性が低く、専門的な適応パラダイムの必要性が実証されました。標準的なRGBカメラで動作し高額な専門インフラを不要とするため、資源制限環境での臨床展開が可能です。AI小児医療の民主化（Democratization of Pediatric Healthcare）に向けた重要な基盤研究として、今後の在宅・地域環境での応用が期待されます。
