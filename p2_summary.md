**2. GlobalSplat: グローバルシーントークンによる効率的フィードフォワード3D Gaussian Splatting**
**著者**: GlobalSplat著者ら et al. (2025)
**arXiv**: https://arxiv.org/abs/2604.15284

**まとめ**:
3D Gaussian Splatting（3DGS）のフィードフォワード手法は入力ビュー数に比例してガウシアン数が増大する課題があった。GlobalSplatはグローバル潜在シーントークン（2048個固定）を先に構築してから幾何・外観を復号化する「整列第一」アーキテクチャにより、わずか16Kガウシアンで28.53 PSNR、推論時間77.88ms、GPU使用量1.79GBという高効率・高品質を同時に達成した。
