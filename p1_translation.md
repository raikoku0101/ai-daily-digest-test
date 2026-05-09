## 1. Introduction (はじめに)

現在の検索システム（字句的または意味的）は、固定された類似度インターフェースを通じて「単一の上位k検索ステップ」で結果を提供します。これは効率的ですが、エージェント型検索（Agentic Search）では瓶首（Bottleneck）となります。正確な字句制約（Exact Lexical Constraints）、疎な手がかりの組み合わせ（Sparse Clue Conjunctions）、局所文脈確認（Local Context Checks）、多段階の仮説改善（Multi-step Hypothesis Refinement）は従来型検索APIでは困難です。

## 2. Method (手法) — Direct Corpus Interaction (DCI)

提案手法は直接コーパス相互作用（Direct Corpus Interaction, DCI）です。エージェントが埋め込みモデル（Embedding Model）、ベクトルインデックス（Vector Index）、検索API（Retrieval API）なしに、grep、ファイル読み込み、シェルコマンド、軽量スクリプトといった汎用ターミナルツールでコーパスを直接検索します。

## 3. Experiments & Results (実験・結果)

BRIGHT、BEIR、BrowseComp-Plus、多段階質問応答（Multi-hop QA）ベンチマークで評価しました。DCI手法は疎（Sparse）、密（Dense）、再ランキング（Reranking）ベースラインを大幅に上回る性能を示しました。

## 4. Conclusion (結論)

言語エージェント（Language Agent）の能力向上に伴い、検索品質は推論能力だけでなく「コーパス相互作用インターフェースの解像度（Resolution of the Interface）」に依存することが示唆されます。
