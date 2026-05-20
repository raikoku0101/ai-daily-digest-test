## 1. Introduction (はじめに)
本研究は、RFT（Reinforcement Fine-Tuning）が視覚的継続学習タスクにおいて破滅的忘却（Catastrophic Forgetting）をどの程度軽減できるかを検証しています。先行研究では RFT が SFT より忘却耐性が高いことが示唆されていますが、クラス増分学習（CIL: Class-Incremental Learning）やドメイン増分学習（DIL: Domain-Incremental Learning）といった実課題での有効性は未解明でした。予備実験で GRPO が SFT を上回るものの依然として無視できない忘却が発生することを確認し、「軌跡レベルのドリフト無視性（Trajectory-level Drift Blindness）」という現象を特定しました。

## 2. Key Finding (主要発見)
「軌跡レベルのドリフト無視性」とは、同じタスク報酬を得た異なる応答が、先行タスクのポリシーからの KL ダイバージェンスで大きく異なることを意味します。標準的な GRPO はタスク報酬のみで応答を評価するため、知識保持に有利な軌跡を選択する機構がなく、これがタスク進行に伴う忘却の主因であることが明らかになりました。

## 3. Method: RaPO (手法)
RaPO（Retention-aware Policy Optimization）は 2 つの主要成分から構成されます。(1)保持報酬（Retention Reward）：先行タスクのポリシー π_{t-1} に近い応答ほど高い報酬を与え、トークンレベルの KL 差分に指数関数的減衰マッピングを適用。知識保持的な軌跡を優先的に強化できます。(2)タスク間利得正規化（CTAN: Cross-Task Advantage Normalization）：EMA（指数移動平均）でタスク間の報酬分布変動を平滑化し、最適化不安定性を緩和。

## 4. Experiments (実験)
5 つの視覚継続学習設定で検証：クラス増分画像分類（ImageNet-R/A、TinyImageNet、CUB-200）、クラス増分物体検出（COCO 2017）、クラス増分ビデオ分類（UCF-101、Kinetics-200）、ドメイン増分学習（DomainNet、OfficeHome）。ImageNet-R（10 タスク）で RaPO が精度 85.92%・忘却 4.69% を達成し、GRPO の 74.67%・20.02% から大幅改善。物体検出でもボックス AP 19.31%（GRPO: 14.64%）と顕著な向上。

## 5. Conclusion (結論)
視覚継続学習における RFT の可能性を初めて体系的に検証し、「軌跡レベルのドリフト無視性」に対応する RaPO を提案。多様な視覚タスクで一貫して良好な性能を示し、マルチモーダル AI の継続学習研究の新たな方向性を提示しました。
