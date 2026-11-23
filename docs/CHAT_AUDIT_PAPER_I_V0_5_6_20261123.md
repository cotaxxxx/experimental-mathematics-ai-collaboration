# chat の監査：第一論文 v0.5.6（v0.5.4 からの差分）

2026-11-23、Claude（通常監査）。

**判定：PASS。** v0.5.4 の監査（`2af6b07`）の §3 の 1〜4 と、先行研究の 5 項目は、すべて入っている。数学の変更はない。小さな直しを一つ勧める（§4）。直したあとは、Judge が本文を通読する段階に進める。

## 1. 対象と同一性

- 置き場所：`cotaxxxx/bg-spheroid-family`、枝 `paper/paper-i-v0.5.6-review-20261123`、commit `c5501c8214312b00ba971cede00190307c86a8d4`、`manuscripts/2026-11-23/Paper_I_v0_5_6/`。
- 外側の `Paper_I_v0_5_6_ARTIFACT_SHA256SUMS.txt` の 5 件は、すべて一致した。
  - PDF：`136d61aa…fb35`、39 ページ
  - zip：`b4b720f0…034b`
- zip は 166 ファイル。危険なパスはない。中の `SHA256SUMS` も全件一致した。
- patch（`SOURCE_DIFF_v0_5_4_to_v0_5_6.patch`、187 行の変更）が触っているファイルは次の 6 つだけ：`LICENSE`、`main.tex`、`references_additions.bib`、`sections/core.tex`、`sections/numerical_discussion.tex`、`sections/related_work.tex`。
- 変更した行は全部読んだ。定理、表、C1〜C6、証明、数値の変更はない。PDF の本文の比較でも、変わっていたのは改行の位置だけだった。

## 2. v0.5.4 の監査 §3 の照合

| 項目 | v0.5.6 | 判定 |
|---|---|---|
| 1 所属 | 「DAYBREAK (independent research)」 | OK（裁定 J1） |
| 2 GeoEnclosure | 参考文献に DOI `10.5281/zenodo.24421364` を入れ、§1 の GeoEnclosure の箇所から引いている | OK（J3） |
| 3 AI の記載 | ChatGPT、Codex、GPT-6.2 Astra（OpenAI）、Claude、Claude Code（Anthropic）、Muse（Meta）を、それぞれの役割とともに挙げている | OK |
| 4 監査の範囲 | 1 ページ目、§3 の末尾、§10 のどれも、次の三点を書いている。抜き取った箱の独立な再計算と、整数での被覆の検査をした。その範囲は `CURRENT_REPRODUCTION_v0_5_4.md`（zip に入っている）にある。C1〜C6 を全部流し直してはいない | OK。言い過ぎも、言い足りなさもない |
| 最後の一文 | 「… is pending」が残っている | OK（Judge の通読を待つ） |
| J2 ライセンス | 一つの `LICENSE` に二つを書いている。文書、図、表には CC BY 4.0、著者が書いたコードには MIT。第三者のものは、それぞれのライセンスに従う | OK |

## 3. 先行研究の 5 項目

| 項目 | v0.5.6 | 判定 |
|---|---|---|
| (1) O'Hara | 0 < β < 3 での境界積分表示を書き、重み (x−p)·n dA が共通であることと、違い（距離の冪と極値の中心 / 角の二乗と停留集合の全体）を書いた。定理と式の番号は使っていない | OK。式は発散定理から正しい |
| (2) Sakata | 平面の円環 {1 ≤ \|y\| ≤ 2} で、r^{−1/2} のポテンシャルの中心の集合が円になること、円板の和では中心が二つになりうること。非凸の平面の図形と、凸な三次元の鞍点の円との違い。例の番号は使っていない | OK（chat が原文で読んだ範囲と一致） |
| (3) 新しい文献 | Böröczky ほか 2020（CPAM 73(7)）、Bertrand 2016（Geom. Dedicata、式 (6) の費用 −log cos d）、Johansson 2018（ICMS、LNCS 10931）。三つとも引用され、参考文献に出ている | OK。DOI は chat が確かめた。巻とページは確かめていない |
| (4) 球の旧稿 | `furutaSphere`（`basepoint-geometry` `abf704b`）を先行の記録として示した。命題 4.2 は自己完結していると明記 | OK |
| (5) 貢献の締め | C1〜C6 の下で、局所分岐を軸比全体の分類（鞍点の対と円の範囲、境界に達する比、ほかの成分の排除）につないだ、と書いた | OK |

## 4. 勧める小さな直し

参考文献の書式で、固有名詞が小文字になっている。BibTeX で `{G}auss`、`{S}tandard` のように中括弧で守ること。

- 「The gauss image problem」→「The Gauss image problem」
- 「Prescription of gauss curvature」→「Prescription of Gauss curvature」
- 「research note and standard v1.1」→「Standard v1.1」

数学には触れないので、直したあとの確認は、PDF の参考文献の表示だけでよい。

## 5. 次

1. Dig が §4 を直す（v0.5.7、またはこの版の差し替え）。
2. Judge が本文を通読する。
3. 第 10 節の最後の一文を、通読の範囲どおりに差し替える。
4. Zenodo の説明文とメタデータを、この版の文面にそろえて、chat が最終の束を監査する。
5. 公開する。
