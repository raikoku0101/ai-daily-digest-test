## 1. Introduction (はじめに)

ロボット操作において、World Action Models (WAMs) は視覚的観測（Visual Observations）と行動（Actions）を同時に予測する有望なパラダイムとして注目されています。しかし従来の WAMs は固定数の予測行動を実行するため、「予測された未来（Imagined Future）が実際の物理的展開と一致しているかどうか」をロボットが認識できないという課題があります。本研究では、適応的実行（Adaptive Execution）を「未来-現実検証問題（Future-Reality Verification Problem）」として定式化します。

## 2. Method (手法) — FFDC + Mixture-of-Horizon Training

提案手法の核は **Future Forward Dynamics Causal Attention (FFDC)** と呼ばれる軽量検証器（Lightweight Verifier）です。FFDC は予測された未来行動（Predicted Future Actions）、予測視覚ダイナミクス（Predicted Visual Dynamics）、実際の観測（Real Observations）、言語指示（Language Instructions）を統合的に因果注意（Causal Attention）で推論します。さらに **Mixture-of-Horizon Training** を導入し、長期軌跡カバレッジを改善しています。

## 3. Experiments & Results (実験・結果)

RoboTwin ベンチマークの実験では、提案手法は WAM 前方パス（Forward Pass）を 69.10% 削減、実行時間を 34.02% 削減しながら、短チャンクベースライン比で成功率を 2.54% 向上させました。実世界実験では成功率が 35% 改善されました。

## 4. Conclusion (結論)

FFDC による適応的実行は長期実行の効率性と接触豊富な局面での応答性を両立させます。予測-観測一貫性を動的チャンクサイズとして自然に導出する設計は直感的かつ効果的です。
