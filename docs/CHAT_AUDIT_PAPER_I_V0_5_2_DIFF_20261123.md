# chat の監査：第一論文 v0.5.1 → v0.5.2（公開前の三点）

2026-11-23、Claude（通常監査）。**判定：PASS。** v0.5.1 の監査（`ea7c2c9`）§3 の三点が、指示どおりに入っている。ほかの変更はない。

## 1. 対象

- `Paper_I_v0_5_2_Integrated_EN.pdf`（36 ページ）
  - SHA-256 `091019a9e4ed4033901c8058807a5839d40f63d39012113a8635b893bb2db144`
  - 添付の `Paper_I_v0_5_2_ARTIFACT_SHA256SUMS.txt` と一致した。
- `Paper_I_v0_5_2_Revision_Notes_JA.md`
  - SHA-256 `187122a43949dd72d83df2b40f0b76ffa093688e18c0b4794bbf1f80a7214dd0`
  - 一致した。
- ソースの zip と patch は受け取っていない。この監査は、v0.5.1 の PDF と v0.5.2 の PDF の本文を全文で比べ、PDF のリンクの注記を確かめたものである。

## 2. 差分（本文の全文の比較）

| 箇所 | 変更 | 確認 |
|---|---|---|
| 日付の行 | v0.5.1 → v0.5.2 | OK |
| 1 ページ目「Main result and status」 | 一文を足した。「The approximate thresholds are c_o ≈ 0.408, b_o ≈ 0.644, b_p ≈ 2.065 and c_p ≈ 4.724 (Table 1).」 | 表 1 の参考値（0.40795886030、0.64354577、2.06538229、4.72438340）を丸めた値と一致する。OK |
| 第 10 節 | 一文を足した。「Record V24 (16 November 2026): cotaxxxx/bg-spheroid-family, commit 127be52046e9498d1306fe3d35c3e02e91c636de, file JUDGE_RULING_D_OB_GLOBAL_CLOSED_20261116.md (with the accompanying independent audit).」 | 印刷しても読める形になった。「see Section 10」の行き先ができた。OK |
| リンクの注記（1、7、33 ページ） | STATE.md（`c41ab3b`）から、一次の記録に替えた | リンク先 `runs/2026-11-16/D_OB_GLOBAL_CLOSED_V24/JUDGE_RULING_D_OB_GLOBAL_CLOSED_20261116.md` は、commit `127be52` に実在する。この commit には chat の V24 の監査も入っている。OK |
| 33〜36 ページ | 参考文献の改ページの位置が変わった | 文の中身は同じ |

定理 3.1、表 1、表 2、C1〜C6、数値、球の節の証明、要旨は変わっていない。

## 3. 注意（直しは求めない）

第 10 節に出てくるファイル名には「JUDGE_RULING」が含まれる。これは一次の記録の実際のファイル名なので、そのまま示すのが正しい。本文の説明の文には、内部の用語は使われていない。

## 4. 次

Zenodo に出す束（PDF、補足、ソースの zip、説明文、メタデータ）の監査に進める。
