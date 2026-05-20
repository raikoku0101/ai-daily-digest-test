**5. TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization**
**著者**: Anonymous et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.20150

**まとめ**:
3DGS（3D Gaussian Splatting）のスケーリング問題を解決するアウトオブコア最適化システム。SSD-CPU-GPU の階層構造でパラメータ表を仮想化し、可視性スパース性と軌跡連続性を活用した差分ストリーミング（Tide）で I/O 転送を 4 倍削減。単一 24GB GPU で 11 億個以上の Gaussian プリミティブのトレーニングを世界初実現。都市規模シーン（MatrixCity）で PSNR 26.1dB を達成し、従来手法の 100 倍以上のスケールを実現。
