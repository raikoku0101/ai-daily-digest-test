**2. RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM**
**著者**: Tikhomirov et al. (2026)
**arXiv**: https://arxiv.org/abs/2607.11683

**まとめ**:
GraphRAG の知識グラフ構築を単一パスから多段階に改善したオープンソースエンジン RAGU を提案。二段階エンティティ・リレーション抽出、DBSCAN+LLM による重複排除、Leiden クラスタリングによるコミュニティ検出を組み合わせる。コンパクトな 7B 特化モデル Meno-Lite-0.1 が Qwen2.5-32B を IE ベンチマークで +12.5% 上回り、単 GPU 環境での本番利用を実現した。広範な文脈合成が必要なタスクで特に強みを発揮する。
