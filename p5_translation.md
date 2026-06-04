## 1. Introduction (はじめに)

LLMエージェントが継続的に到着するタスクストリームに対応する際の課題を扱う。従来のauto-harnessシステム（A-Evolve、GEPA、Meta-Harness）は静的ベンチマークで評価されていたが、実運用環境では「タスク履歴が無制限に成長し、異なるタスク種が混在し、タスク分布が時間とともに変化する」という3つの重大な課題が発生する。単一のharness（プロンプト、スキル、ツール、メモリなどの集合）を繰り返し更新する従来手法は脆く、性能が早期にピークに達した後低下する問題があった。

## 2. Related Work (関連研究)

継続学習（continual learning）はタスクストリームからの学習と過去能力の保持を扱い、ドメイン適応・テスト時適応（test-time adaptation）は分布シフトに対応する。混合専門家（mixture-of-experts）は異種入力を特殊化コンポーネントへ振り分ける。LLMエージェントの自己改善関連では、A-Evolveは線形チェーン型evolver、GEPAは反射的Paretoプロンプト進化、Meta-Harnessはファイルシステムアーカイブを使用する。ただし既存手法はunbounded streams・タスク異質性・非定常性の組み合わせには対応していない。

## 3. Method (手法)

oracle harnessとのギャップを「進化損失（evolution loss, L_evo）」と「適応損失（adaptation loss, L_adapt）」に分解する分析的フレームワークを導入。これに基づき3つの主要成分を提案する。

**(1) 持続的auto-harness**: 4段階マルチエージェントevolver（分析→研究→実装→検証）、時間的フィードバック開示（temporal feedback disclosure）、循環間記憶（cross-cycle memory）によりunbounded streamに対応。

**(2) ソルブ時適応（solve-time adaptation）**: ハーネスツリー（harness tree）構造とエージェンティックルーティング（agentic routing）により、各タスクに最適な特化ブランチを選択。

**(3) Human-in-the-loop**: タスクボード操作と研究フェーズ支援で、履歴にない外部信号を補助。

## 4. Experiments (実験)

3つのストリーミングタスク（予測市場PolyBench、セキュリティ競争CTF-Dojo、イベント予測FutureX）で評価。PolyBenchでは280.9%から297.1%のカバレッジ・80.9%精度を達成し、A-Evolve（45.2%）やMeta-Harness（50.8%）を大幅上回る。CTF-Dojoでは50.2% pass rate、FutureXでは47.3%を記録。

Ablation研究から：マルチエージェントevolerはevaluation feedbackとcross-cycle memoryがある時に最強、ハーネスツリールーティングはCTF-DojoとPolyBenchで有意な適応利得を提供、human steeringは外部信号（API認証等）の注入時に最有効であることが示された。

## 5. Conclusion (結論)

オープンエンドタスクストリームはunbounded増加・異質性・非定常性という3つの展開課題を露出させる。Adaptive Auto-Harnessは持続的harness構築とsolve時タスク適応でこれらに対応し、5つの既存ベースラインとablationを上回った。進化損失と適応損失の分解により、単一の頻繁に更新されるdense harnessでは不十分な理由が明確化され、欠落機能の構築と各タスクへの特化ブランチ選択の必要性が証明された。
