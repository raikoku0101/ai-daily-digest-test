## 1. Introduction (はじめに)

Claude Code（v2.1.88）の公開TypeScriptソースコードを分析し、包括的なアーキテクチャを記述。シェルコマンド実行・ファイル編集・外部サービス呼び出しを自動化するエージェント型コーディングツールの内部構造を体系化。独立OSSシステム「OpenClaw」との比較で設計選択肢を明確化。

## 2. Design Philosophies (設計哲学)

5つの人間中心価値観：Human Decision Authority（人間の決定権）、Safety/Security/Privacy（安全性・プライバシー）、Reliable Execution（信頼できる実行）、Capability Amplification（能力増幅：内部調査で27%のタスクがツールなしでは試みられなかった）、Contextual Adaptability（文脈適応性：CLAUDE.md・スキル・MCP・フック・プラグインによる多層構成）。

## 3. Architecture Overview (アーキテクチャ概要)

7機能コンポーネント：UI層・コアエージェントループ（QueryEngineクラス）・権限管理（7権限モード：plan/default/acceptEdits/auto/dontAsk/bypassPermissions/bubble）・ツールプール（最大54個の組み込みツール）・状態・永続性層・実行環境。5層階層：Surface→Core→Safety/Action→State→Backend。

## 4. Permission and Safety Layers (権限と安全性)

7つの独立安全性層：ツール事前フィルタリング・Deny-first規則評価・権限モード制約・ML基盤自動分類器・シェルサンドボックス・再開時権限非復元・フックベース仲介。重要発見：ユーザーが権限プロンプトの93%を承認するため、対話型確認だけでは安全性が不十分と判断。多層独立安全機構を設計。

## 5. Context Management (コンテキスト管理)

5段階圧縮パイプライン（Budget reduction→Snip→Microcompact→Context collapse→Auto-compact）。各層は異なるコスト・ベネフィット比を持ち、安い層が先に実行。4拡張メカニズム（MCPサーバー・プラグイン・スキル・フック）をコンテキストコスト別に階層化。27イベント型フック（うち5個が安全性関連）。

## 6. Subagent Delegation & Session Persistence (サブエージェント委任・セッション永続性)

サブエージェントは独立コンテキストで実行し概要のみ親に返却。Sidechain転写で親コンテキストを肥大化させない。append-only JSONLセッション転写でResume/Fork/Rewind操作をサポート。権限状態は復元されない（セキュリティのため）。

## 7. Comparative Analysis & Future Directions (比較・将来方向)

OpenClawとの比較：Claude Codeはシングルターン反応型ループ、OpenClawはマルチチャネルゲートウェイ。同じ設計問題が異なるデプロイメント文脈では異なる回答を生む。将来課題：静かな失敗の検出・セッション横断的永続性・監視機構のスケーリング・長期的な人間能力保持とのバランス。
