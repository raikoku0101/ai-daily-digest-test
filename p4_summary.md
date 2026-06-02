**4. Policy and World Modeling Co-Training for Language Agents**
**著者**: Ning Lu et al. (2026)
**arXiv**: https://arxiv.org/abs/2606.02388

**まとめ**:
RLでLLMエージェントを訓練する際、ポリシー学習だけでは「行動が環境にどう影響するか」の知識が不足する。提案手法PaWは既存のRLロールアウトを再利用して補助的な世界モデリング（World Modeling）監督信号を生成し、ポリシーと世界モデルを同時訓練。追加シミュレーターや訓練段階を一切必要とせず、3つのエージェントタスクで複数の強力なRLベースラインを一貫して上回る改善を達成。
