**4. MOSS-VL Technical Report**
**著者**: Pengyu Wang, Chenkun Tan, Shaojun Zhou et al. (2026)
**arXiv**: https://arxiv.org/abs/2608.15045

**まとめ**:
既存の視覚言語モデル（VLM）はオフライン処理を前提としており、「話しながら知覚する」リアルタイム対話能力を第一級機能として設計していない。MOSS-VLはゲート付きクロスアテンション（gated cross-attention）機構により言語デコーダが生成中に新規フレームを処理可能にし、合成インタラクションコーパスで発話タイミング制御を学習。4つのストリーミングベンチマークでオープンソース最高スコアを達成し、OmniMMI Proactive Alertingでは66.0 vs 37.5という大幅優位性を示しながら、時間遅延をQwen3-VL-8B比で2.8〜5.1倍短縮した。
