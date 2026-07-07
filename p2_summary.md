**2. KVpop: Key-Value Cache Compression with Predictive Online Pruning**
**著者**: KVpop チーム (2025)
**arXiv**: https://arxiv.org/abs/2607.05061

**まとめ**:
LLM長文脈推論のボトルネックであるKVキャッシュを学習型オンライン枝刈りで圧縮するKVpopを提案。将来のアテンション重みを教師信号として「保持/削除」を学習し、遅延メモリ型スコアリングで保護ウィンドウ内の文脈を活用。Qwen3-4Bで圧縮率75%時に密注意性能の95%を維持し、数学推論・コード生成タスクへの転移性も示した。
