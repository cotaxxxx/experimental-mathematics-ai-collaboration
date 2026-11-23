# chat の監査：第一論文 v1.0 の最終の公開用の束（`50a2ad1`）

2026-11-24、Claude（通常監査）。

- 対象：`bg-spheroid-family` の commit `50a2ad1882ea95a38f7b6120c0f2a90483c1bd9f`（親 `124d31b`、その親 `b8bc379`＝監査済みの v1.0）。`manuscripts/2026-11-24/Paper_I_v1_0_Final_GeoEnclosure/`。
- 基準：v1.0 の監査 `b22c32d`、Judge の承認 `d9abd1e`、追記の承認 `9a99a1c`。

**判定：論文の PDF は PASS。束は、Zenodo に上げる前に F1 と F2 を直すこと。** どちらも数学と本文には触れない。

## 1. 同一性

| ファイル | SHA-256 | 照合 |
|---|---|---|
| `Paper_I_v1_0_Final_Publication_GeoEnclosure_EN.pdf`（43 ページ） | `765bd0653f845ea5d88e655bf178c577dc94420caac28a68209314e84c5a65b7` | 一致 |
| `…_GeoEnclosure_Source_and_Verification.zip` | `a60af6d088c7094fb224828c7b73420f1216d6fef957163c5bc3881bc6ebfd25` | 一致 |
| `SOURCE_DIFF_Paper_I_v1_0_Final_to_GeoEnclosure.patch` | `7b5ef750a9b185f79c097f22a0148ef64f3d93c5a33ea5dde9a02c8634c10a89` | 一致 |
| `ARTIFACT_SHA256SUMS.txt` | `e464bcf6f5d28d0ea78fddb970be033df932d782a77bbd4e2cd7f5532577368a` | 報告と一致 |

- zip の中の PDF は、外の PDF と同じ hash である。
- zip の中の `SHA256SUMS`（184 件）は全件一致した。
- commit の作者とコミッターのメールは `154295364+cotaxxxx@users.noreply.github.com`。

## 2. 差分（v1.0 `b8bc379` の PDF との全文の比較）

違いは次の 4 か所だけである。

| 箇所 | 変更 | 確認 |
|---|---|---|
| PDF の文書情報 Subject | 「; independent audit pending」を削除 | OK |
| §8 の冒頭 | 「this working draft」→「this paper」 | OK |
| §10 の題（本文と目次） | 「…and status of the draft」→「…and status」 | OK |
| 1 ページ目、結論の段落の直後 | GeoEnclosure の三文（`9a99a1c` §6 の文面どおり、DOI は文字で見える） | OK |

- ソースの差分は、`main.tex`、`sections/computational_evidence.tex`、`sections/numerical_discussion.tex` の 3 ファイルだけである。
- 数字 21,254／31,340 は、要旨と §8 の数字と一致する。
- 定理、表、図、証明、数値、参考文献は変わっていない。ページ数は 43 のまま。

## 3. 公開の前に直すこと

- **F1（古い hash の一覧）：** zip の中の `zenodo_preparation/PRIMARY_RECORDS_SHA256SUMS.txt` の 7 件のうち、2 件が中のファイルと合わない。
  - `provenance/EN_SUMMARIES/V24_JUDGE_RULING_SUMMARY_EN.md`
  - `CURRENT_REPRODUCTION_v0_5_4.md`
  - v1.0（`b8bc379`）の zip でも同じで、今回の変更で生じたものではない。一覧を作った後に、この 2 件が改訂されたためとみられる。v1.0 の監査（`b22c32d`）では見落としていた。
  - Zenodo の記録はファイルを差し替えられない。読者が確かめて合わない一覧を残さないよう、一覧を作り直すこと。2 件の中身は変えない。
- **F2（メタデータ）：** zip の中の `zenodo_preparation/PAPER_I_V1_0_ZENODO_METADATA_DRAFT.json` は古い下書きのままである。
  - description に「This v1.0 manuscript remains subject to an independent difference audit.」が残っている。この一文を外す。
  - `status: DRAFT_NOT_SUBMITTED` と `release_conditions` は、公開する束には合わない。最終のメタデータ（`…_ZENODO_METADATA_FINAL.json`）を作り、下書きは束から外すか、履歴であることをファイル名で示す。
  - 題名、著者（Furuta, Katsushi）、所属（DAYBREAK (independent research)）、ORCID、ライセンス（cc-by-4.0）、References（`10.5281/zenodo.24421364`）は正しい。変えない。
- F1 と F2 の後、zip の `SHA256SUMS` と、束の `ARTIFACT_SHA256SUMS.txt` を作り直す。**PDF は変えない**（hash `765bd065…65b7` のまま）。

## 4. 注意（直しは求めない）

- 21,254／31,340 の単位の呼び方が、要旨では「leaves」、1 ページ目の新しい文と §8 では「(terminal) boxes」である。同じ数を指している。直すなら PDF が変わるので、Judge の判断による。
- `provenance/SHA256SUMS_v0_4_Original.txt` と `…_v0_5_4_Original.txt` は、その版の時点の一覧で、今の zip の中身とは合わない。履歴の記録として置かれている。README にその旨の一行があれば、読者が迷わない。

## 5. Zenodo に上げるファイル

- 論文の PDF（`765bd065…65b7`）。
- ソースと検証資料の zip（F1 と F2 の後の版）。計算の補足の PDF と一次の記録は、この zip の中にある。

## 6. 追記：Judge の裁定（2026-11-24 07:25）

- **F3（用語をそろえる）：** 要旨の「left 21,254 of 31,340 leaves undecided」の「leaves」を「boxes」に改める。この数を「leaves」と呼んでいるのは要旨の一か所だけで、序論と §8 は「terminal boxes」、1 ページ目の新しい文は「boxes」である。
- 変えるのはこの一語だけにする。F1、F2 と同じ回に入れ、PDF、zip、patch、SHA-256 の一覧を登録する。chat が差分を監査する。
