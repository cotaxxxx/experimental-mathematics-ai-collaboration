# Judge裁定｜三軸研究再開の工程管理記録

**裁定日：2026年11月23日**  
**提案者・裁定者：Judge（古田勝士）**  
**記録担当：Dig（ChatGPT）**  
**位置づけ：数学研究の進退管理の裁定／証拠の採否・具体的な計算着手ではない**

## 1．裁定

Judgeは「次に３軸を再開します」と指示した。

**三軸研究（TR-01）はREOPENED、既存の個別計算・開発（TR-02）はHOLD。**

研究自体の再開は、2026年11月22日に裁定された旧中止状態に優先する。しかし、旧中止裁定・当時の未解決問題・監査記録・証拠は書き換えない。

**三軸リポジトリ内の再開裁定原本：** [`evidence/chat/2026-11-23/JUDGE_RESTART_TRIAXIAL_20261123.md`（commit `7ce6f1e7`）](https://github.com/cotaxxxx/bg-triaxial-family/blob/7ce6f1e7a4bbe6d599499eadff4de1e46327ef68/evidence/chat/2026-11-23/JUDGE_RESTART_TRIAXIAL_20261123.md)

**以前の中止裁定：** [`686343f`（2026年11月22日）](https://github.com/cotaxxxx/bg-triaxial-family/blob/686343fdf9349fd15cd5324457bd44aaa6af5dde/evidence/chat/2026-11-22/JUDGE_STOP_TRIAXIAL_20261122.md)

## 2．再開の範囲

| 工程 | 旧状態 | 新状態 |
|---|---|---|
| TR-01（三軸楕円体研究） | CANCELLED | **REOPENED／研究計画再構築中** |
| TR-02（E2/E4/Reader関連計算・開発） | CANCELLED | **HOLD／案件別承認待ち** |

当面の作業は既存証拠の読直し、未解決事項の明確化、目的と方法の再定式化、計画の事前宣言と通常監査である。短い確認以外の計算は研究PCでDigが行い、**新規投入にはJudgeの個別承認が必要**。

取り下げられたE2参照実行指示、AstraによるE2・E4関連作業、Claude CodeのReader 0.7・C移植は、研究再開だけでは実施・再投入・統合の権限を得ない。特別Dig・特別監査の利用はJudgeが別途決める。

## 3．変更しない事項

- E3の92組、V63-Aの9組予算切れ・完走0組、Reader既存試験等の診断と原本を保持する。
- 数学的な証明の認証、CLOSEDの新規裁定、`DIAGNOSTIC_ONLY / NOT_EVIDENCE`の昇格を行わない。
- 第一論文のZenodo公開方針とExperimental Mathematics誌への投稿HOLD、第三論文の保留は変更しない。
- 第二論文の管理期限2027年3月31日を自動変更しない。
- REDDS v1.0および旧版の工程表は変更しない。

## 4．最新の工程表

[数学研究工程管理表 v6（13件）](MATH_RESEARCH_SCHEDULE_2026-11-23_v6.md)に反映。前版v5を歴史として保持する。

**状態：JUDGE REOPENED / RESTART PLANNING / NEW COMPUTATION NOT AUTHORIZED**
