## 1. Introduction (はじめに)

インタラクティブビデオ生成モデル(Genie・YUME・HY-Worldなど)は急速進化しているが、各モデルが独自ベンチマークで評価されるため公平比較が不可能。統一されたシーン・行動シーケンスがなく、同評価指標でも数値比較不可能な問題がある。WorldMarkはこの問題を解決し、6つの主要モデルに対して統一環境を提供する。

## 2. Related Work (関連研究)

ビデオ生成技術はGAN・VAEから拡散モデル、Sora・HunyuanVideoへと進化。MineWorldやOpen-Oasisはマインクラフト領域での行動認識リアルタイム相互作用を実現し、Matrix-GameやHY-Worldは写真的現実世界への拡張を達成。各モデルは独自ベンチマークで報告されるため評価ギャップが存在し、VBench・WorldScore・MINDなどの公開ベンチマークは統一された試験条件が欠ける。

## 3. Method (手法)

WorldMarkは5構成要素：①Evaluation Dimension Suite(視覚品質・制御整合性・世界一貫性の8指標)、②Image Suite(50参照画像：1人称・3人称、現実的・様式化シーン)、③Action Suite(15段階複雑度軌跡)、④Unified Action Interface(WASD入力を各モデルのネイティブ形式に変換するアダプター)、⑤Evaluation Workflow(統合パイプライン)。VLMベースのシーン認識フィルタリングで約500標準化評価ケースを自動生成。

## 4. Experiments & Results (実験・結果)

YUME 1.5・Matrix-Game 2.0・HY-World 1.5・HY-GameCraft・Open-Oasis・Genie 3の6モデルを評価。YUMEが視覚品質で優秀(審美性56.94・画像品質74.36)、Genie 3が世界一貫性で優位。重要発見：「視覚品質と世界一貫性は概ね無相関」—審美的フレームが優秀なモデルが長期一貫性に欠ける傾向。人間選好度調査(20名・50セット)でSpearman相関ρ>0.9を達成し、自動評価指標の妥当性を検証。

## 5. Conclusion (結論)

WorldMarkは初の標準化インタラクティブI2Vベンチマークとして統一行動インターフェース・500ケーステストスイート・多層評価ツールキットを提供。全データ・コード・モデル出力を公開予定。新モデル追加には単一の行動マッピングアダプター実装のみ必要で、World Model Arena(warena.ai)でオンライン対戦も展開。
