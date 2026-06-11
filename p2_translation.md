## 1. Introduction (はじめに)
文法制約付きデコーディング（GCD: Grammar-Constrained Decoding）はコード生成の構文的妥当性を保証する技術だが、著者らはこれが安全性リスクになることを指摘。「CodeSpear」攻撃により、良性の文法制約がモデルを強制的にコード生成モードに入れ、自然言語での拒否応答を無効化できることを実証した。既存の安全アライメントが自然言語モダリティに依存していることが根本的な問題。

## 2. Background and Related Work (背景と関連研究)
文法制約付きデコーディングは LLM が構文的に妥当なコードを生成することを保証する技術。一方、既存の安全性アライメント手法は自然言語での拒否応答に依存（Safety alignment is almost exclusively grounded in the natural-language modality）。コードモダリティにおける安全アライメントの欠如がこの攻撃を可能にしている。

## 3. Threat Model (脅威モデル)
攻撃者は標準的な Python 等のコード文法を用いて GCD インターフェースを活用可能。ローカルデプロイメント（vLLM、SGLang 等）と API ベースデプロイメント（OpenAI、Fireworks AI 等）の両方で現実的な脅威。攻撃目標は安全アライメントをバイパスして悪意あるコードを生成させること。

## 4. Methodology - CodeSpear (攻撃手法)
GCD を適用すると悪意プロンプトへの自然言語拒否応答がコード文法の有効空間外となり、モデルはコード生成を継続するしかなくなる。既存アライメントはコードモダリティでの安全性を明示的に教示していないため攻撃が成功する。実装はシンプルな文法制約の適用だけで完結する。

## 5. Methodology - CodeShield (防御手法)
DPO（Direct Preference Optimization）を使い「自然言語拒否 ≻ ハニーポットコード ≻ 悪意コード」の優先度階層を学習。セマンティックに無害で構造的に多様なハニーポットコードを GCD 下で生成するよう訓練。文法が厳格化されても多様なハニーポット戦略により堅牢性を確保。

## 6. Experimental Results (実験結果)
CodeSpear: ローカル LLM（Qwen2.5-Coder、LLaMA3 等 10 モデル）で平均 ASR 81.82%、API ベース LLM で 67.39% を達成。CodeShield: 攻撃成功率（ASR）を 77.39%（SafeDPO ベースライン）から 5.57% に劇的低減。HumanEval pass@1 は 66.94% を維持し、コード生成性能への影響を最小化。

## 7. Conclusion (結論)
GCD という一見無害な技術が攻撃面になりうることを実証し、コードモダリティにおける安全アライメントの重要性を示した。CodeSpear と CodeShield の両面アプローチにより、コード LLM の信頼性と安全性を両立できることを実証。業界標準への統合を推奨。
