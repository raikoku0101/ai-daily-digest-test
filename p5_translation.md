## 1. Introduction (はじめに)
自律 GUI エージェント（Autonomous GUI Agents）は2つの根本的課題に直面している。早期停止（Early Stopping）では、エージェントが検証可能な証拠なしに成功を宣言してしまう。反復ループ（Repetitive Loops）では、同じ失敗行動を回復せずに繰り返し続ける。これらの問題は現実の GUI 自動化での信頼性を著しく損ない、実用展開の障壁となっていた。VLAA-GUI はこの2問題を一元的に解決するモジュラーフレームワークとして提案される。

## 2. Related Work (関連研究)
GUI 自動化エージェントの研究は WebAgent・Mind2Web・AppAgent 等により急速に発展している。VLM（Vision-Language Model）ベースのアプローチが主流となりつつあるが、タスク完了の検証と失敗回復のメカニズムは十分に研究されていなかった。RL ベースの手法は学習コストが高く、LLM ベースの手法は完了判断の信頼性に課題があった。

## 3. Framework Components (フレームワークコンポーネント)
VLAA-GUI の3つの統合コンポーネント：(1) 完全性検証器（Completeness Verifier）：各終了ステップで UI 観察可能な成功基準を強制適用。エージェントレベル検証器が completion claim を decision rule と照合し、直接的な視覚的証拠がない主張を拒否する、(2) 回復メカニズム（Recovery Mechanism）：反復ループを検出した際に代替行動シーケンスを生成・実行する、(3) 探索コンポーネント（Search Component）：従来手法が失敗するシナリオで新たなアプローチを体系的に探索する。

## 4. Completeness Verification (完全性検証)
完全性検証は2段階で実施：スクリーンショット解析（Screenshot Analysis）でタスク完了の視覚的証拠を確認、ルールベース検証（Rule-based Verification）でタスク固有の完了条件を評価。視覚的証拠なしの「成功」主張を系統的に拒否することで、早期停止問題を根本から解決する。

## 5. Experiments (実験)
AndroidWorld・GUI Odyssey・Mind2Web 等の標準ベンチマークで評価。比較対象：GPT-4V・Claude Vision・既存 GUI エージェント。タスク完了率・誤検知率・回復成功率・ループ検出率を測定。タスクカテゴリ（情報検索・フォーム入力・ナビゲーション等）別の詳細分析も実施。

## 6. Results & Conclusion (結果と結論)
VLAA-GUI は全ベンチマークで既存手法を上回るタスク完了率を達成。早期停止の誤検知率を大幅低減し、反復ループからの回復成功率も高水準を記録。モジュラー設計により、各コンポーネントの効果を独立して検証（アブレーション研究）できることも実証。GUI 自動化エージェントの実用展開に向けた信頼性向上に大きく貢献する成果である。
