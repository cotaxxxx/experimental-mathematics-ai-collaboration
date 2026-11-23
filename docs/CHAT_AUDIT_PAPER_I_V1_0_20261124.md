# chat の監査：第一論文 v1.0（v0.5.7 の直し `2009fda` からの差分）

2026-11-24、Claude（通常監査。このセッションのモデルは Fable 5.2 に切り替わっている）。

**判定：PASS。** 数学の変更はない。公開の前に、表示の直しを一つ勧める（§3）。

## 1. 対象と同一性

- 置き場所：`bg-spheroid-family` の枝 `paper/paper-i-v1.0-author-review-20261124`、commit `b8bc379efedc7c0eca9a095fdc778ca806c36ac7`。
- 履歴：`2009fda`（v0.5.7 の直し、監査済み）→ `ed0991e`（v0.5.8 候補、C3 の数の訂正だけ）→ `b8bc379`（v1.0）。
- `ARTIFACT_SHA256SUMS.txt` の 6 件は、すべて一致した。PDF は 43 ページ。
- 監査のしかた：監査済みの v0.5.7 の PDF（`2009fda`）と、v1.0 の PDF の本文を全文で比べ、patch を読んだ。

## 2. 差分（本文の比較で、中身の違いは次の 3 点だけ）

| 箇所 | 変更 | 確認 |
|---|---|---|
| 版の表示 | 「Integrated research draft v0.5.7 — 23 November 2026」→「Paper I v1.0 — 24 November 2026」 | OK |
| C3 の照合の数（§8 の規模の表と §8.4 の表、`CURRENT_REPRODUCTION` の C3 の行） | 「35 selected vertical leaves」→「35 checked leaves (11 vertical: 8 E_z, 3 E_zz; 15 equatorial: 11 H, 4 E_xx; 9 boundary-equator H_b), independently re-enclosed in V51 audit (source c44ee45)」 | V51 の監査記録（`c44ee45`）の内訳（H 11、E_xx 4、H_b 9、E_z 8、E_zz 3、計 35）と一致する。OK |
| §10 の最後 | 「Author verification … is pending」を消し、段落「Author review and verification scope」を足した：著者は日本語の通読用の訳で本文全体を読み、本稿とこの開示を承認した。コード、計算の記録、補足は著者自身では確かめておらず、記録された監査に委ねる | Judge が決めた範囲のとおり。OK |

- ほかの違いは、改行とページ割りだけである。定理、表 1・表 2、C1〜C6、証明、数値は変わっていない。
- Zenodo のメタデータの下書き：版は v1.0。説明文の「pending」は、著者の確認の範囲の文に替わった。GeoEnclosure の DOI（references）と、紹介の一文は残っている。
- zip（184 ファイル）には、`LICENSE` と、直した `CURRENT_REPRODUCTION_v0_5_4.md` が入っている。

## 3. 公開の前に勧める直し（表示だけ）

- PDF の文書情報の Subject が「… independent audit pending」のままである。公開する PDF に残ると、監査前の版に見える。この監査で差分は確かめたので、「independent audit pending」を外すこと。
- 本文に「working draft」（§8 の冒頭）と「status of the draft」（§10 の題）が残っている。v1.0 としては「this paper」「status」でよい。変えるかどうかは Judge の判断でよい。条件つきであることは、別の文で明記されている。

## 4. 確かめていないこと

- 著者の承認の文は、Judge が本文を読み終えたという事実に基づく。chat は、その事実を Dig の報告でしか知らない。公開の前に、Judge 本人の確認が要る。
- v0.5.7 より前から変わっていない部分の数学は、この監査では見直していない。
