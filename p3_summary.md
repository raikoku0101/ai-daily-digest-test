**3. Long Context Pre-Training with Lighthouse Attention**
**著者**: Lighthouse Attention Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.06554

**まとめ**:
因果トランスフォーマーの長文事前学習におけるSDPA（Scaled Dot-Product Attention）のΘ(N²)ボトルネックを解決するLighthouse Attentionを提案。訓練専用の対称的階層型注意機構でQ/K/Vを多層ピラミッドに圧縮・選択し、層単位の計算量をΘ(N·d)に線形化。512K文脈で順逆17.3倍高速化を達成し、訓練後の密集SDPA復帰で性能をフルに保持する。
