**3. Unsupervised Process Reward Models**
**著者**: (Anonymous et al.) (2025)
**arXiv**: https://arxiv.org/abs/2605.10158

**まとめ**:
ステップレベルのアノテーションも最終答の検証ラベルも不要な完全教師なし Process Reward Model (uPRM) の訓練手法を提案。LLM のトークン確率から導出したスコアリング関数で複数推論トレジェクトリを共同評価することで PRM を学習。ProcessBench で LLM-as-a-Judge より最大 15% 絶対精度改善、テスト時スケーリングでは教師あり PRM と同等性能を達成し、RL 訓練では報酬ハッキングへの耐性も向上。高コストなアノテーションを不要にしスケーラブルな推論改善への道を開く。
