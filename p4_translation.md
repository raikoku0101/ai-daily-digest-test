## 1. Introduction (はじめに)

多言語自動音声認識（Multilingual ASR：Automatic Speech Recognition）の性能は言語間で著しく不均等であり、長尾言語（Long-tail Languages）はデータ不足による深刻な性能低下に苦しんでいる。特にカザフ語（Kazakh）、キルギス語（Kyrgyz）、ウズベク語（Uzbek）などの中央アジア言語は既存の多言語モデルで十分にカバーされていない。本研究はこれらの過小評価言語向けのロバストな基盤モデル（Foundation Model）構築を目指す。

## 2. Method (手法)

GigaAM Multilingual は200万時間の多言語音声データを用いてConformerエンコーダーをHuBERTスタイルの目的関数で事前学習（Pre-training）させた基盤モデルである。重要な技術革新として2つのバランシング手法を導入：(1) 事前学習時の「クラスタレベルのデータバランシング戦略（Cluster-level Data Balancing）」により言語偏重を軽減、(2) 微調整時の「ドメイン認識サンプリング（Domain-aware Sampling）」により自然発話音声への適応を向上させる。

## 3. Training Setup (学習設定)

200万時間という大規模な多言語音声コーパスを活用し、特に低リソース言語のデータが優位言語（英語・中国語など）に埋もれないよう、データバランシング戦略を事前学習フェーズから適用。HuBERT（Hidden-Unit BERT）スタイルの自己教師あり学習目的関数を採用することで、ラベルなしデータからも豊かな音声表現を学習する。

## 4. Results (結果)

Whisper Large v3やOmnilingual-1Bなどの強力なオープン事前学習エンコーダーを上回る性能を達成。特に自然発話音声（Spontaneous Speech）での改善が顕著で、低リソース言語での認識精度が大幅に向上。効率性も維持されており、実用的なデプロイが可能なサイズを実現している。

## 5. Conclusion (結論)

現実的なデータ不均衡（Realistic Data Imbalance）状況下での効果的な多言語適応のための実証済みレシピを提供した。基盤エンコーダーとASRモデルを公開することで、低リソース言語コミュニティの音声AI研究を支援する。Interspeech 2026への採択は音声処理分野での高い評価を示しており、他の低リソース言語への拡張が今後の課題となる。
