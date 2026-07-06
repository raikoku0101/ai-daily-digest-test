## 1. Introduction (はじめに)
拡散変圧器（DiT: Diffusion Transformer）は高品質な画像・動画生成を実現しているが、複数段階のサンプリングと増加するパラメータ数により推論コストが高い。既存のPost-Training Quantization (PTQ)手法は、DiTの活性化がタイムステップ・プロンプト・ガイダンス分岐間で変動するため、新しいチェックポイントやモダリティごとにキャリブレーションデータを再取得・再適合させる必要がある。本論文では、正規化・回転基底で量子化を行うデータ非依存量子化手法OrbitQuantを提案する。

## 2. Related Work (関連研究)
LLM量子化では、活性化外れ値をウェイトにスケーリングする（SmoothQuant）か回転で除去する（QuaRot, SpinQuant）アプローチが一般的である。DiT量子化では、ほとんどのメソッド（SVDQuant, PTQ4DiT, AdaTSQ, ViDiT-Q）がキャリブレーション依存であり、データフリーなDVD-Quantやconvrotも存在するが、モデル固有の調整が必要という課題がある。OrbitQuantは完全解析的コードブック設計により、画像・動画間で転移可能な点が独自性。

## 3. Methodology (手法: OrbitQuant)
OrbitQuantは重み・活性化を共有の回転・正規化基底で量子化する。**Randomized Permuted Block-Hadamard (RPBH)回転**により、正規化活性化の各座標がタイムステップに関わらず固定周辺分布 f_d ≈ N(0,1/d) に従う。このRPBH変換は「一様ランダム順列と小ブロックWalsh–Hadamard行列の組み合わせ」で、O(d log h)の高速実装が可能。重み行列を事前に回転させておくことで、推論時は活性化への単一前向き回転のみが必要となり、オーバーヘッドが最小限。

## 4. Experiments and Results (実験と結果)
GenEval指標でFLUX.1-schnell・FLUX.1-dev・Z-Image-Turboを評価すると、W4A4設定でOrbitQuantはすべてのベースライン（SVDQuant、AdaTSQ、ViDiT-Q）を上回り、W2A4ではほぼ唯一の機能的手法。VBench動画評価でもWan 2.1-1.3B・CogVideoX-2BにおいてOverall Consistency次元で最高性能を実現。推論遅延ではSmoothQuantより1.09倍、QuaRotより1.28倍高速化。

## 5. Conclusion (結論)
OrbitQuantは、タイムステップ毎のキャリブレーションをデータ非依存の分布ベースコードブックで置き換える。RPBH回転によりウェイト・活性化が共有基底量子化され、「画像・動画モダリティ間でチューニング不要」かつ「W2A4で実用的な生成品質を達成する唯一のPTQ手法」として、低ビット拡散変圧器量子化の新標準を示す。
