## 1. Introduction (はじめに)

プロセス報酬モデル(Process Reward Model; PRM)は大規模言語モデル(LLM)の推論を段階ごとに評価し、精密な監督を提供する強力なメカニズムです。しかし、その有効性には専門家による各推論ステップへのアノテーション(annotation)が必要という課題があり、スケーラビリティ(scalability)が制限されています。本研究は人間の監督を一切必要としない教師なしPRM(uPRM; unsupervised PRM)の訓練方法を提案し、この課題の解決を目指しています。

## 2. Method (手法)

提案手法の核は、LLMのトークン確率(token-level probability)から導出されるスコアリング関数にあります。この関数は推論軌跡(reasoning trajectory)のバッチ全体における「最初のエラーが発生したステップ(first erroneous step)」の候補位置を統合的に評価します。人間による最終答の検証も不要な点が革新的であり、完全に自律的なPRMの構築を可能にします。

## 3. Experiments and Results (実験と結果)

uPRMはProcessBenchデータセットでLLM-as-a-Judgeを最大15%上回る精度を実現しました。テスト時スケーリング検証器(test-time scaling verifier)として教師ありPRM(supervised PRM)と同等の性能を示し、多数決投票法(majority voting)を6.9%上回ります。強化学習(RL)の報酬信号として使用した際、教師ありPRMより堅牢な方針最適化(policy optimization)を実現します。

## 4. Conclusion (結論)

本研究は複雑な推論タスクの拡張可能な報酬モデリング(scalable reward modeling)への道を開きます。人間のアノテーションコストを排除しながら高性能を維持する手法として実用的な価値が高く、あらゆるドメインへのPRM適用を現実的なものにします。
