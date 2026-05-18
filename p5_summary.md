**5. Efficient Image Synthesis with Sphere Latent Encoder（球面潜在エンコーダによる効率的画像生成）**
**著者**: Sphere Latent Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.15592

**まとめ**:
従来の Sphere Encoder が推論時にピクセル空間と潜在空間を繰り返し往来する問題を解決し、生成全体を球面潜在空間で完結させる新フレームワークを提案。再構成損失と一貫性損失を潜在空間に移行し、Logit 正規分布ノイズスケジュールを採用することで、計算コストを約 85%（FLOP 6.5 倍削減）削減。ImageNet-1K で 4 ステップ生成 FID 2.25 を達成し、多段階拡散モデルと競合する品質を実現した。
