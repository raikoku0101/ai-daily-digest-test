## 1. Introduction (はじめに)
タンパク質・分子・結晶などの科学的構造データは異なるドメインに分散しており、それぞれの構造-特性関係を統一的に理解する基盤モデルが存在しなかった。本研究では SciReasoner を提案し、構造を「推論の中心的な証拠」として位置付けることで、学際的かつ透明性の高い構造理解を実現する。

## 2. Method (手法)
座標 (coordinates)、トポロジー (topology)、周期的結合性 (periodic connectivity) を統一された構造認識語彙に離散化する。各構造トークン (structure token) を推論ステップ内でアドレス指定可能な証拠ユニット (addressable evidence unit) として扱い、マルチモーダル推論チェーンを構築。タンパク質・小分子・無機結晶の三ドメインに対応。

## 3. Experiments & Results (実験・結果)
86ベンチマーク中67タスクで最先端 (SOTA) 性能を達成。ホモロジー制御 GO 予測 (homology-controlled Gene Ontology prediction) では低相同性タンパク質およびオーファン型タンパク質の細胞成分注釈においてF値が 0.42 → 0.55 に向上。化学分野では単一ステップ逆合成精度 (single-step retrosynthesis accuracy) が 0.63 → 0.72 に上昇。

## 4. Conclusion (結論)
科学的推論において構造を検査可能な根拠 (inspectable basis) として位置付けることで、予測精度と解釈可能性を両立。創薬・材料科学・タンパク質工学の三分野を横断する汎用的な科学 AI 基盤を確立した。今後は更なるドメイン拡張と計算効率の改善が期待される。
