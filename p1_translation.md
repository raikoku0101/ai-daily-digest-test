## 1. はじめに (Introduction)

従来の検索システム（辞書ベース・意味ベース）は、コーパスへのアクセスを「固定された類似度インターフェース（fixed similarity interface）」に圧縮しており、単一のtop-k検索ステップで結果を返します。しかしエージェント型検索（agentic search）タスクでは、正確な語彙制約（lexical constraints）、複数の弱い手がかりの組み合わせ、局所的コンテキスト確認、段階的な仮説改善などが必要となるため、従来型の検索APIはボトルネックになります。本研究はこれらの制限を克服する新しいアプローチを提案します。

## 2. 手法 (Method)

提案手法はDirect Corpus Interaction（DCI、直接コーパス相互作用）と呼ばれ、エージェントが「埋め込みモデル（embedding model）やベクトルインデックス（vector index）なしに、grep・ファイル読み込み・シェルコマンドなどの汎用ツールを用いて生のコーパスに直接アクセス」します。オフラインインデックスが不要で、進化する動的コーパスにも自然に適応できる利点があります。

## 3. 実験 (Experiments)

BRIGHT・BEIR・BrowseComp-Plusデータセット、および多段階QA（multi-hop QA）タスクで評価を実施しました。DCIは、スパース検索（sparse retrieval）・密集検索（dense retrieval）・リランキング型の強力なベースラインを大幅に上回る性能を示し、従来型意味検索器（semantic retriever）に依存せずに高い精度を達成しています。

## 4. 結論 (Conclusion)

言語エージェントの能力向上に伴い、検索品質は推論能力（reasoning capability）だけでなく「コーパスとの相互作用インターフェース（interaction interface）の解像度」に依存することが判明しました。DCIはエージェント型検索向けの新しいインターフェース設計空間を開拓する重要なアプローチです。
