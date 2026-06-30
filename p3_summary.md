**3. One-Step Gradient Delay is Not a Barrier for Large-Scale Async Pipeline Parallel LLM Pretraining**
**著者**: Pipeline Parallelism Research Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2606.30634

**まとめ**:
LLM事前学習の非同期パイプライン並列化で生じる「1ステップ勾配遅延（gradient staleness）」が実質的な障壁にならないことを最大10Bパラメータのモデルで実証。AdamWより新手法Muonが高い耐性を示し、誤差フィードバック補正と組み合わせることで同期学習と同等の性能を達成。大規模LLM学習のGPU効率を大幅に改善する実践的知見。
