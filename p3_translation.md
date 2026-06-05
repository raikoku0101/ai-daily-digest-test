## 1. Introduction (はじめに)
KITTI・nuScenes・Waymo など既存データセットは進展を可能にしたが、センサー性能・地図完全性・地理的多様性で限界がある。本論文は高分解能カメラ・400m超 LiDAR・4D Imaging Radar・完全 HD マップを統合した欧州データセットを開発し、4 つのベンチマークで現 SoTA 手法の空間学習の系統的ギャップを露出させることを目指す。

## 2. Dataset Construction (データセット構築)
センサー構成：72.5Mpx 同期カメラ群（6 周囲＋1 長焦点＋ステレオ対）、7 台 LiDAR（平均 900k 点/フレーム・有効距離 400m 超）、3 台 Continental ARS548 4D Imaging Radar、RTK 精度 0.6cm の GNSS/INS。全センサーはハードウェア同期、サブピクセル内部・1cm/0.1° 外部較正を達成。HD マップは Lanelet2 形式で 62km²、29 道路特徴クラス・120 交通標識クラス・3D 信号を含む。

## 3. Benchmarks (ベンチマーク)
**(1) Online HD Map Construction**: MapTRv2・SDTagNet ともに従来ベンチマーク比で性能低下を示し、単純幾何要素のみ評価では隠れていたギャップを露出。
**(2) Long-range Monocular Depth Estimation**: 75m 超で全手法が性能低下、200m 超では著しく信頼性欠如。総合スコア最上位の MapAnything が長距離では最低に逆転するという驚くべき発見。
**(3) Novel View Synthesis**: 駆動軌跡上でも 27.8% 低下、横方向 ±3m シフトで 80% 超の低下。photometric 指標では検出されない幾何不整合を顕在化。
**(4) End-to-End Driving**: nuPlan 訓練の Epona で最小ドメインギャップだが依然顕著。

## 4. Related Work (関連研究)
KITScenes は既存比で最も完全な HD マップ・最高点群密度（3 倍）・最長有効 LiDAR 距離を実現。Lanelet2 による規制構造の完全性は nuScenes・Argoverse 2 が提供できていない機能。

## 5. Limitations & Conclusion (制限と結論)
動的オブジェクトの 3D アノテーション未実装、データ量は nuPlan の約 1/20。しかし高忠実度センサー・完全 HD マップ・4 ベンチマークの組み合わせにより、Level 4 自動運転に向けた空間推論能力のギャップを初めて系統的に露出させることに成功した。
