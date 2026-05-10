## 1. はじめに (Introduction)

ロボット操作タスクにおいて、World Action Models（WAM/世界行動モデル）は視覚観測と行動を同時に予測する有望なパラダイムです。しかし既存のWAMは固定長の予測行動を実行するため、「想像した未来（imagined future）が実際の物理的展開と一致するか」という問題に対応できません。本研究では、予測未来が信頼できる場合は長く実行し、現実が想像と乖離した場合は早期に再計画（re-planning）するアプローチを提案します。

## 2. 手法 (Method)

Future Forward Dynamics Causal Attention（FFDC/未来順序動力学因果注意）という軽量な検証器（verifier）を開発しました。FFDCは予測された将来行動・視覚ダイナミクス（visual dynamics）・実際の観測・言語指示を統合し、「残りの行動実行がまだ信頼できるか」を推定します。さらに「Mixture-of-Horizon Training（多地平線混合訓練）」により適応的実行向けの長時間軌跡カバレッジを改善しています。

## 3. 実験・結果 (Experiments/Results)

RoboTwinベンチマークでは、WAMの前向きパス（forward pass）を69.10%削減し、実行時間を34.02%短縮しながら成功率を2.54%向上させました。実世界実験では成功率が35%改善され、強力な堅牢性-効率トレードオフ（robustness-efficiency trade-off）を実現しています。

## 4. 結論 (Conclusion)

提案手法は予測と観測の一貫性（prediction-observation consistency）から適応的行動チャンク長（adaptive action chunk length）を自動決定し、長時間実行の効率性と接触豊富な局面での応答性を両立させます。ロボット操作の実用化に向けた重要な進展を示しています。
