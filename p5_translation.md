## 1. Introduction（はじめに）
ライブストリーミングeコマースのデジタルアバターは視聴者対話・製品質問回答・マーケティング戦略実行をリアルタイムで行う必要がある。頻繁な戦略更新と低遅延という相反する要件に対処するため進化可能な実行環境（Harness）を提案。固定設定で学習した小規模モデルはHarness変更に適応できず、大規模モデルは遅延が大きすぎるという課題を解決する。

## 2. Digital-Avatar Harness Agent Architecture（アーキテクチャ）
Harness Agentはスキル・ツール・プロンプト・検証ロジック（Hook）を独立して更新可能な4モジュールで構成。「モデル重みを固定したまま業務ロジックを進化させる」ことが可能。Harness Evolutionというサイクル（診断→確認→編集→評価→回帰チェック）を繰り返し、数時間単位での改善を実現する。

## 3. Harness-Aware Training（手法：HAT）
Harness-State Augmentation（HSA）によりスキル名・説明、ツール定義、プロンプト構造、Hook動作を「タスク保存的な変形」で多様化させる。3段階訓練：(1)HSA-SFT: 強力な教師モデルが複数Harness環境で生成した高品質軌跡から学習、(2)General OPD: 基盤モデルから一般性を回復、(3)HSA-RL: 強化学習により変化するHarness下での頑健性を向上させる。

## 4. Evaluation（評価設定）
Live-Stream QA（実運用品質）、Harness-Variant QA（Harness変更への耐性）、Tool/Prompt Robustness（合成シナリオ）、IFEval（汎用指示従性）の4セットで評価。HarnessベースのAgent-as-a-Judgeを人間ラベルで較正し信頼性を確保。

## 5. Experiments & Results（実験結果）
HAT訓練モデルはLive-Stream QAで平均94.8点を達成し最強の汎用LLM（93.0点）を上回った。固定Harness SFTはIFEvalで7.6点低下するがHATでは83.5点を維持。単一H20 GPU+MTP最適化でP50遅延3.4秒、P95遅延8.1秒を達成。Taobao LiveのオンラインA/BテストでGMV 4.33%上昇、商品ページビュー0.91%上昇を記録。

## 6. Conclusion（結論）
Harness-Aware Trainingは進化する実行環境と政策安定性の矛盾を解決する系統的アプローチ。小規模モデルの遅延メリットを保ちながらHarness変更への適応能力を獲得させることに成功。商用AIアバターの実運用での有効性を実証した。
