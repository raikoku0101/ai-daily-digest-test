**4. TTPO: Test-Time Policy Optimization**
**著者**: Anonymous et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.27448

**まとめ**:
正解ラベルなしのテスト時訓練（TTT）でLLMの数学推論を改善するTTPO（Test-Time Policy Optimization）を提案。多数決疑似ラベルを活用しながらその不正確さに耐性を持つ非対称目的関数（正サンプルにはOPSDで密な監督、負サンプルにはGrouped RLで選択的ペナルティ）を設計。Qwen3シリーズで評価し、完全TTT設定で1.7Bが+7.2点（TTRL比+5.4点）を達成、正解ラベルを使うOPSDと同等以上の性能をラベルなしで実現した。
