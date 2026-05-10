## 1. はじめに (Introduction)

本論文はSemEval-2026 Task 8「MTRAGEval」タスクBの優勝システムを報告します。タスクは参照文献を用いた忠実な多ターン応答生成（faithful multi-turn response generation）を目指しており、研究チームは異種LLMアンサンブル（heterogeneous ensemble）により単一モデルを大幅に上回る性能を目指しました。

## 2. 手法 (Method)

提案手法は「judge-orchestrated LLM ensemble（ジャッジ統合LLMアンサンブル）」と呼ばれます。7つの異なるLLMと2種のプロンプティング（prompt engineering）バリアントで構成され、GPT-4o-miniがジャッジとして各インスタンスの最適候補を選定します。さらに7B規模のドメイン適応モデル（domain-adapted model）「Meno-Lite-0.1」も開発し、コスト・パフォーマンスの優れたトレードオフを実現しています。

## 3. 実験・結果 (Experiments/Results)

26チーム中1位を達成し、条件付き調和平均（conditioned harmonic mean）0.7827を記録。最強ベースライン「gpt-oss-120b」（0.6390）を大きく上回りました。アブレーション研究により、モデルファミリーの多様性・スケールの異なるモデル・異なるプロンプト戦略の組み合わせが性能向上に本質的であることが実証されました。

## 4. 結論 (Conclusion)

異種アンサンブル（heterogeneous ensemble）アプローチが単一モデルより一貫して優れた性能を発揮することを示しました。MTRAGEvalの注釈上の制限も分析し、将来の改善方向を提示。コードは公開されており、再現性と実用性を確保しています。
