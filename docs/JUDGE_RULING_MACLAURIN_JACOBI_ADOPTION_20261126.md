# Judge 裁定：GeoEnclosure 実例1（マクローリン→ヤコビ分かれ目）の結果の採用

- 裁定者：Judge（古田勝士）。AskUserQuestion ボタン「採用してノートに反映（推奨）」で決定。記録は chat（Claude）。時刻はこのコミットを正とする（裁定は 2026-11-26 18:4x JST、chat 監査 4e0a884 の直後）。
- 対象：cotaxxxx/GeoEnclosure `codex/macl-jacobi-interval-20261126` @ 53319d86cefbd6e9ef7c635db47790750f5777c2（結果登録）、束 4e52466bfd7be83c9af44f0add7907dee4cc36de
- chat 監査：docs/CHAT_AUDIT_MACLAURIN_JACOBI_RESULT_53319d8.md（4e0a884）PASS

## 裁定
計算記録の等級 DIAGNOSTIC_ONLY の結果を、Judge の裁定により **採用（ADOPTED）** とする。公表用の主張は次のとおり。
- 一意性：解析的証明（F′ ≥ 44e/105 と端点符号）。
- e* ∈ [117118091422919119/2^57, 234236182845838293/2^58] ⊂ [0.8126700106117429, 0.8126700106117432]
- Ω²/(πGρ) ∈ [0.3742296747861903, 0.3742296747862011]
- 前提：MPFR 4.2.2 の丸め保証（mpfr_asin, mpfr_sqrt 等）。符号は整数級数で独立に再包囲。

研究PCの原記録の等級表示（DIAGNOSTIC_ONLY）は書き換えない。採用はこの裁定記録で示す。
