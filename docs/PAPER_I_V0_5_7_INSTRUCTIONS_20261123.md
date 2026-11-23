# 第一論文 v0.5.7 の改訂指示（Judge 承認済み、2026-11-23）

作成：Claude（通常監査）。宛先：Dig（ChatGPT）。
v0.5.6（`bg-spheroid-family`、commit `c5501c8`）を親とする。v0.5.6 の監査は `c5a3249`。

**大原則：** 数学の主張、定理、表、証明、数値、計算の資料は変えない。新しい文は、どれも既にある結果から直接言えることだけにする。新しい計算や推定の数字は入れない。

## 背景

Judge が v0.5.6 を通読して、次のことが分かった。

- v0.5.6 は「何が起こるか」の正確な記録である。しかし、「なぜその範囲だけか」「それで何が言えるか」「何が新しいか」が書かれていない。
- Zenodo は査読ではないので、題名と 1 ページ目で面白いと思われなければ読まれない。
- 面白いと思った研究者は、正しいかを確かめに資料を見る。そこで GeoEnclosure に出会う。

## A. 1 ページ目の結論（最重要）

「Main result and status」の先頭に、次の中身の段落を置く。

> For this energy, the bifurcation patterns themselves are classical: a reflection-symmetric pitchfork at the centre produces an axial pair of saddles, and its rotation-symmetric counterpart produces a circle of saddles. What this paper determines, across the whole range of aspect ratios, is where these patterns occur (c_o < λ < b_o on the axis, b_p < λ < c_p on the equator), where the new stationary sets leave or enter through the boundary (the axial pair reaches the poles at b_o; the circle reaches the boundary equator at b_p), and that nothing else occurs. The boundary events and the absence of any further stationary component do not follow from general bifurcation theory. Consequently, an interior local minimizer exists exactly for c_o < λ < c_p, and there it is the centre alone.

- 状態は一文にする：全族の分類は六つの有限の計算の主張 C1〜C6 を条件とする。扁平側の λ ∈ [2/5, 33/50] と球は、それとは別に確かめ終えている。
- 境界の上の制約つき最小は分類していない、と一言添える。
- 監査の範囲の細かい説明（抜き取りの再計算、被覆の検査など）は、1 ページ目から第 10 節へ移す。中身は消さない。

## B. 「なぜその範囲か」の小節（§3.1、定理 3.1 と表 2 の直後）

- **軸の上（扁平側）：** 中心での軸方向の曲率 a_c(λ) = ∂²Ê/∂q₃²(0) と、極での軸方向のトレース B_o(λ) の符号の表を作る。
  - λ < c_o：a_c < 0、B_o < 0
  - c_o < λ < b_o：a_c > 0、B_o < 0
  - λ > b_o：a_c > 0、B_o > 0
  - 食い違うのは真ん中の範囲だけ。そこでは軸に沿って上ってから下がるので、途中に零点が要る。軸方向に極大、横方向に極小なので、指数 1 になる。
- **赤道の上（扁長側）：** 中心での赤道方向の曲率 h_c(λ) = ∂²Ê/∂q₁²(0) と、赤道の縁での半径方向のトレースで、同じ表を作る。食い違うのは b_p < λ < c_p だけで、回転の対称性から、零点は円になる。
- **両端は二種類の出来事：**
  - 中心での曲率の符号の変化（c_o、c_p）：中心から生まれる、または中心に消える。§6.1 の z\*(c_o+) = 0 につなぐ。
  - 境界でのトレースの符号の変化（b_o、b_p）：境界から出る、または入る。§6.1 の z\*(b_o−) = 1 につなぐ。
- **言えることと言えないことを分ける：** 符号が食い違えば、中間値の定理から零点は少なくとも一つある。一つだけであることと、軸と赤道の外にないことは、§4・§6・C1〜C6 が担う。
- 符号は、表 1 の定義、§6、C2 の表（`C2_AXIS_CENSUS_TRACE_v0_5_4.md` の第 1、3、10 行）と一致させる。
- 1 ページ目に一文を足して、この小節を指す。

## C. 汎関数の読み方（序論に短い段落）

- α_p(x) は、点 p から境界の点 x への視線と、x での外向きの法線とのなす角である。
- E は、内部のどこから見れば境界がいちばん正面から見えるかを測る。
- A の最後の一文（内部の極小は c_o < λ < c_p でだけ存在し、そこでは中心だけ）は、表 2 から直接出る系として §3 にも書く。

## D. 先行研究（関連研究の節）

- 分岐の一般論：Golubitsky–Schaeffer (1985)、Golubitsky–Stewart–Schaeffer (1988)。鏡映の対称性での熊手型の分岐と、O(2) の対称性で円になること。
- 凸な領域での中心・臨界点の一意性：Cabré–Chanillo (1998)、O'Hara「Uniqueness of radial centers of parallel bodies」。
- 原文で仮定と結論を確かめてから引く。形の変形で臨界点が生まれる、または境界から出入りする先行研究も調べる。
- 位置づけは A の段落と同じにする：型は一般論から予想される。新しさは、軸比全体での確定、境界での出入り、ほかにないこと。

## E. 参考文献の大文字

`{G}auss`、`{S}tandard` を中括弧で守る（監査 `c5a3249` §4）。

## G. 主張から証拠への道筋（§8）

- C1〜C6 のそれぞれに、束の中のどこで確かめられるか（`CURRENT_REPRODUCTION` の該当の行）を一行で添える。
- どの包み方（箱の分け方、区間の積分、被覆の検査）で示したかを、GeoEnclosure の言葉で一行ずつ書く。
- 書き方の注意：「GeoEnclosure という方法で示した」とは書いてよいが、「GeoEncloseReader で示した」とは書かない。C1〜C6 の計算は、主にそれぞれの producer の核で行ったため。

## H. 題名

- 題名は「Saddle pairs, a saddle circle, and nothing else: stationary points of an angle energy across all spheroid shapes」。PDF の文書情報と、Zenodo のメタデータの題名も同じにする。
- 要旨の一文目か二文目で、必ず条件を述べる。例：「Assuming six explicit finite computational assertions (C1–C6), we show …」。
- 扁平側の λ ∈ [2/5, 33/50] と球は、条件なしで確かめ終えていることも、要旨に一文で残す。

## I. 1 ページ目の図

- λ の数直線（対数目盛でよい）に、次を描く。
  - c_o：軸上の対が中心から生まれる。
  - b_o：極から抜ける。
  - b_p：円が赤道の縁から入る。
  - c_p：中心に消える。
  - λ = 1 の球。
  - 内部の極小がある範囲 (c_o, c_p)。
- 値は表 1 の近い値を使う。
- 図の説明文に、全族の分類は C1〜C6 を条件とすることを一言入れる。

## J. 反例の居場所（§3、定理 3.1 の後）

次の中身の一文を置く。

> Each of C1–C6 is a finite, checkable assertion; any stationary point outside the classification would have to violate one of them.

## K. 計算の規模の表（§8 の冒頭）

- C1〜C6 のそれぞれについて、範囲、箱・葉・帯の数、使った包み方を、記録にある数字だけで並べる（`CURRENT_REPRODUCTION_v0_5_4.md` の数字）。
- 最初の探索で 31,340 個のうち 21,254 個の符号が決まらなかったこと、そこから一次元への縮約で解決したことを一文で添え、GeoEnclosure の DOI を引く。

## F. 変えないもの

- 第 10 節の最後の一文（pending）。Judge が、変わったところを読み終えるまで残す。
- 定理、表、証明、数値、計算の資料。

## 束の準備（Zenodo、v0.5.7 と並行）

本文が引く主な一次の記録の写しと、その英語の要約を、Zenodo の束に入れる準備をする。対象は V24 の判定（日本語）と、C2 の組み立ての原本。

## 渡すもの

PDF、ソースの zip、v0.5.6 からの patch、SHA-256 の一覧。chat が差分を監査する。監査では、特に次を確かめる。

- 題名、要旨の最初の二文、図の説明の三か所に、条件が抜けていないこと。
- B の符号が、本文の定義と一致すること。
