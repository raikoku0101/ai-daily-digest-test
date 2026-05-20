## 1. Introduction (はじめに)
3D Gaussian Splatting（3DGS）は高速でリアルな新規視点合成を実現する明示的な場面表現として注目されています。しかし各 Gaussian プリミティブは 59 個の浮動小数点値を保持し、100 万個で約 90GB のメモリが必要となるため、単一 GPU（24GB）での訓練は根本的にメモリ制約に直面。従来手法では約 1100 万個の Gaussian に限定されていました。TideGS は「GPU VRAM を作業セットキャッシュとして機能させ、SSD-CPU-GPU の階層構造でパラメータ表を仮想化」することで単一 24GB GPU で 11 億個以上のプリミティブ訓練を実現します。

## 2. Method: Block Virtualization & Async Pipeline (手法)
TideGS は 3 つの協調的技術で構成されます。(1)ブロック仮想化と 2 段階可視性フィルタリング：Gaussian を Morton 順でソートし SSD 整列ブロック（4096 プリミティブ/ブロック）に分割。CPU で粗い視錐台カリング、GPU で精密 Gaussian レベルフィルタリングを実行。(2)階層的非同期パイプライン：SSD 読み込み・CPU-GPU 転送・バックプロパゲーション・書き込みを重複実行し I/O 遅延を隠蔽。ログ構造化 SSD 保存で順序付き追記によるランダムアクセスを回避。

## 3. Method: Tide - Trajectory-adaptive Differential Streaming (差分ストリーミング)
カメラ軌跡に沿った連続フレーム間で重複するブロック集合を保持し、増分差分のみを転送する「軌跡適応型差分ストリーミング（Tide）」が核心技術です。LRU スコアリングと次ステップ有用性を組み合わせた容量制限住設セット選択でメモリ効率を最大化。Morton 順による空間局所性活用でキャッシュヒット率 95.2% を実現。

## 4. Experiments (実験)
スケーラビリティ：Native 3DGS が約 1150 万 Gaussian（VRAM 制約）、TideGS が 11 億 Gaussian 以上（単一 24GB GPU）。都市規模シーン MatrixCity での 102M Gaussian 訓練では PCIe 転送を 0.41GB/iter から 0.10GB/iter に削減（4 倍改善）。11 億 Gaussian 訓練で PSNR 26.1dB を達成し CLM の 25.0dB を上回る。Mip-NeRF 360 で軌跡順序付けにより Native 比 6.4% 性能改善。

## 5. Limitations & Conclusion (制限・結論)
弱い軌跡連続性を持つ非構造化画像集合では差分ストリーミングの効率が低下する可能性。遅い SSD 環境での性能低下も懸念されます。TideGS は「可視性スパース性と軌跡連続性を活用した実用的な単一 GPU 大規模訓練基盤」として、都市スケールのデジタルツインや超高精度3D再構成への道を開く根本的なブレークスルーです。
