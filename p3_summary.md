**3. To Add Is Machine, To Delete Is Human: Measuring and Mitigating Deletion Avoidance in LLM Code Editing**
**著者**: Deletion Avoidance Study Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2607.28887

**まとめ**:
LLMが生成するコードパッチにおける「削除回避 (deletion avoidance)」を初めて定量化した研究。SWE-bench Verifiedで解決済みとされたパッチでも開発者の削除の28〜35%が残存し、テスト合格が削除の正確性を保証しないことを示す。削除感応テストを追加すると合格率が63.2%→41.9%に急落。CanItDeleteベンチマークを新設し、後訓練で削除例を0.7%追加するだけでCanItDelete成功が倍増、SWE-bench全体も5.3pp改善することを実証。
