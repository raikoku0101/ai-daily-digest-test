## 1. Introduction (はじめに)
複雑な質問に対してマルチステップの Web 検索で答える「深い検索 (Deep Search)」では、複数の有望な方向性の中でどの経路を追求するかの判断が重要。貪欲に現在最良の方向を追従すると弱い継続を延長してしまい、無規律に探索すると検索予算を浪費する。本論文は「制御された試行錯誤 (Controlled Trial-and-Error)」を実現する TreeSeeker フレームワークを提案。

## 2. Method (手法)
TreeSeeker は木構造状態 (Tree-Structured State) 上で分岐 (Branch)・復帰 (Return) 探索を組織化。各分岐は部分目標 (Sub-goal) の試験的方向を表現。テキストベースの UCB (Upper Confidence Bound) 信号で価値・不確実性・リスクを評価し「有望な分岐の活用 (Exploitation)」「不確実な選択肢の探索 (Exploration)」「非生産的な継続の剪定 (Pruning) と復帰」を動的に選択。TreeMem (ツリーメモリ) が証拠・不確実性・矛盾・進捗・失敗の手がかりを各分岐に付随させて管理する。

## 3. Results (実験結果)
XBench-DeepSearch・BrowseComp・BrowseComp-ZH ベンチマークで TreeSeeker はオープンソースの強力なベースラインを一貫して上回る性能を示した。「明示的な分岐・復帰制御」がより強力な推論と ツール実行 (Tool Execution) を補完することが実証された。

## 4. Conclusion (結論)
木構造化された試行錯誤フレームワークが深い検索タスクにおける効率的な意思決定を実現。探索予算の最適配分を通じて信頼性のある証拠への到達確率を向上させ、複雑な情報要求への対応能力を強化。MCTS (Monte Carlo Tree Search) の知見を LLM の推論時スケーリングに応用した有望なアプローチ。
