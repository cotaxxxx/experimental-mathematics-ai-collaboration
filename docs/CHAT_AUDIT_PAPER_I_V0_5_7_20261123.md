# chat の監査：第一論文 v0.5.7（v0.5.6 からの差分、指示書 `50d1224` との照合）

2026-11-23、Claude（通常監査）。

**判定：PASS。** 指示書の A〜K はすべて入っている。数学の変更はない。直す点が一つ（R1、要旨の内部の用語）と、勧める点が三つある。

## 1. 対象と同一性

- 置き場所：`bg-spheroid-family` の枝 `paper/paper-i-v0.5.7-50d1224-20261123`、commit `5a5d5c54922167dfdc796df58a50989dd44d87b2`（親は `c5501c8`）。
- `ARTIFACT_SHA256SUMS.txt` の 6 件は、すべて一致した。PDF は 43 ページで、文書情報の題名は新しい題名になっている。
- patch が触るのは 6 ファイルだけ：`main.tex`、`core.tex`、`related_work.tex`、`references_additions.bib`、`computational_evidence.tex`、`numerical_discussion.tex`。
- 変わった行は全部読んだ。定理、表 1・表 2、C1〜C6、証明、数値の変更はない。
- 1 ページ目は、画像に描いて確かめた。

## 2. 指示書との照合

| 項目 | v0.5.7 | 判定 |
|---|---|---|
| A 結論 | 1 ページ目の先頭に Conclusion の段落。状態の説明は一文で、細部は §10 にある | OK（文面は指示どおり） |
| B なぜその範囲か | §3.1。扁平側の a_c と B_o、扁長側の h_c と h_b の符号の表がある。両端の二種類の出来事、§6.1 の端点、存在と一意性の区別も書かれている | OK。符号は表 1、§6、C2 の表と一致する。扁長の表を λ ≤ 5 に限り、λ ≥ 5 は C5・C6 に回すのも正確 |
| C 読み方と系 | 視線と法線の段落（「すべての点が正面を向く必要はない」と断っている）。系：内部の局所最小は c_o < λ < c_p でだけ存在し、中心ただ一つ。c_o と c_p では退化した鞍点 | OK。表 2 から直接出る |
| D 先行研究 | Golubitsky–Schaeffer、Golubitsky–Stewart–Schaeffer、Cabré–Chanillo（仮定つき）、O'Hara の平行体（プレプリントと断っている）、Borodzik–Némethi–Ranicki（境界つき多様体の Morse 理論。本稿の g∂ = 0 とは別物と断っている）。位置づけの文もある | OK。chat は原文の仮定までは確かめていない（Dig が確かめたと記録している） |
| E 大文字 | Gauss、Standard | OK |
| G 証拠への道筋 | §8 の冒頭に GeoEnclosure の説明。「計算は主に producer の核で行い、GeoEncloseReader ではない」と明記 | OK |
| H 題名 | 新しい題名。要旨の一文目に C1〜C6 の条件 | OK |
| I 図 | λ の数直線に c_o、b_o、球、b_p、c_p と、内部の局所最小の範囲。説明文に C1〜C6 の条件 | OK |
| J 反例の居場所 | 一文があり、「六つすべてを独立に再計算したとは主張しない」と添えている | OK |
| K 規模の表 | §8 の冒頭の表（C1〜C6 の範囲、数、包み方）と、21,254 / 31,340 の一文 | OK |
| F 変えないもの | §10 の最後の一文（pending）は残っている | OK |
| 束の準備 | V24 の判定と C2 の組み立ての写し、英語の要約、メタデータの下書き | V24 の写しは、一次の記録（`127be52`）とバイト単位で一致した（SHA-256 `89435cf9…2c3c`） |

## 3. 直す点

**R1（公開の前に必要）：要旨の最後の文が、内部の用語に戻っている。**

- 今の文：「The oblate window λ ∈ [2/5, 33/50] is separately verified by the V24 ruling」。v0.5.1 で外した「ruling」が、要旨に戻っている。
- 直し方の例：「is separately verified in the author's recorded audit (record V24; see Section 10)」。

## 4. 勧める点

1. **1 ページ目の結論の文字の大きさ。** Conclusion の段落を小さい文字（footnotesize）にし、余白も縮めて、1 ページに押し込んでいる。論文で一番大事な段落なので、本文と同じ大きさがよい。そのために図が 2 ページ目に回っても構わない。
2. **Zenodo のメタデータの下書き：**
   - 関連する研究に、GeoEnclosure の DOI `10.5281/zenodo.24421364`（関係 References）がない（裁定 J3）。
   - 説明文の最後に、「この分類を確かめた方法論は GeoEnclosure として別に公開している」という一文を足す。
   - 説明文の「author verification remains pending」は、公開のときに、Judge の通読の範囲どおりの文に差し替える。
3. **V24 の英語の要約：**
   - 「Judge」が誰かを、外の読者のために一行で書く。例：「In this project's governance, "Judge" denotes the author (Katsushi Furuta) acting as final decision-maker.」
   - λ_x を「a transverse root at t = 1/2」と書いているが、「the axial root passes t = 1/2」のほうが正確である。

## 5. 次

1. R1 と §4 を直す。数学は変わらないので、chat の確認は差分だけでよい。
2. Judge が、変わったところ（1 ページ目、§3.1、系、関連研究、§8 の冒頭）を読む。
3. §10 の最後の一文を差し替える。
4. Zenodo の最終の束を監査する。
5. 公開する。

## 6. 追記（2026-11-24）：直しの確認と日本語の通読版

**直し（`2009fda`、`paper/paper-i-v0.5.7-audit-fixes-d9342f9-20261124`）：PASS。**

- `ARTIFACT_SHA256SUMS.txt` の 6 件は、すべて一致した。
- patch はわずかな行だけである。
- R1：要旨の文が「verified in the author's recorded audit (record V24; see Section 10)」になった。
- §4-1：結論の段落を本文と同じ大きさの文字（normalsize）にし、余白を詰める設定を外した。
- §4-2：メタデータに、GeoEnclosure の DOI（関係 references）と、GeoEnclosure を紹介する一文が入った。「pending」の文は、Judge の通読と承認のあとに差し替える、と公開の条件に書かれた。
- §4-3：V24 の英語の要約に、「Judge」とは著者が最終の判断者として務める役だ、という一行が入った。λ_x を「the axial root passes through t = 1/2」と直した。
- 数学の変更はない。

**日本語の通読版（`fd416db`、42 ページ）：抜き取りで照合し、忠実だった。**

照合した箇所は、題名、要旨、1 ページ目（結論、条件つきの分類、検証の状態、図 1）、§3.1 の二つの符号の表と本文、系（内部の局所最小）、扁平側の検証の範囲の段落。どれも英語の原本 v0.5.7 と中身が一致し、符号、範囲、条件の断り書きも正しく訳されている。

全ページの照合はしていない。訳は通読のための参考で、正本は英語である（README のとおり）。

**§10 の最後の一文への提案：** Judge は日本語の通読版で読むので、差し替える文にもそのことを正直に書くのがよい。例：

> The author has read the full manuscript, with the aid of a Japanese reading translation, and approves it and this disclosure. The computer code, computational records and supplement were not re-checked by the author; for these the author relies on the documented audits described in this section.
