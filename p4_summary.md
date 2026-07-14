**4. 4D Human-Scene Reconstruction from Low-Overlap Captures**
**著者**: StudioRecon Team et al. (2026)
**arXiv**: https://arxiv.org/abs/2607.09125

**まとめ**:
4台の低オーバーラップカメラだけで動的人物シーン（4D）を高品質再構成する StudioRecon を提案。背景はビデオ拡散モデル(GEN3C)で仮想視点を大量生成して密な教師信号を合成し、人物はSMPL骨格プライオリと Linear Blend Skinning で幾何制約。運動適応的一貫性注入（光学フロー+EMA）でちらつきを抑制。既存手法対比 LPIPS で36%改善を達成した。
