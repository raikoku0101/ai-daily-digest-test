**4. How can embedding models bind concepts?**
**著者**: Research Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.31503

**まとめ**:
CLIPなどのVision-Language埋め込みモデルが「概念バインディング（赤い四角と青い四角を区別する能力）」に失敗する原因を内部表現レベルで解明した研究。CLIP埋め込みは階層的加法構造（R²=0.90）を示し単一モダリティ内では物体情報を復元できるが、バインディング関数が高複雑度のためクロスモーダル対応が失敗することを実証。汎化に成功するモデルは低複雑度で乗法的相互作用（multiplicative structure）を持つバインディング関数を学習しており、これが設計指針として重要な知見となる。
