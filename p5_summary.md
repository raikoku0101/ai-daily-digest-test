**5. Where does output diversity collapse in post-training?**
**著者**: （OLMo 3 / AI2 チーム）et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.16027

**まとめ**:
LLMのポスト学習後に発生する出力多様性崩壊の原因を、OLMo 3 7Bの13チェックポイントを追跡して分析。Think-SFTがベースモデル比62%の多様性を喪失するのに対し、Instruct-SFTは38%に留まり、崩壊程度を決定するのはポスト学習手法ではなく訓練データの構成であることを証明。多様性崩壊はモデル重みに埋め込まれており推論時の修正は不可能で、SFTデータの多様化とKLペナルティなしのRLが有効な対策として推奨される。
