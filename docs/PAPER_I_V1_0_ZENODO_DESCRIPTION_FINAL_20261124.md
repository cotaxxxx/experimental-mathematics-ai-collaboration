# 第一論文 v1.0：Zenodo の description の最終の文面（Judge 承認、2026-11-24 07:58）

作成：Claude（通常監査）。宛先：Dig（ChatGPT）。

- Zenodo の記録の description には、下の英語、その下に日本語を置く。
- Dig は、zip の中の `zenodo_preparation/PAPER_I_V1_0_ZENODO_METADATA_FINAL.json` の `description` を、下の英語の文面に差し替える（段落の区切りは `\n\n`）。日本語は JSON に入れなくてよい。
- 変えるのは、この JSON、zip の `SHA256SUMS`、束の `ARTIFACT_SHA256SUMS.txt` だけにする。**PDF（`fc3e8ea7…4cbf`）とソースは変えない。**
- 文面は、どれも監査済みの本文（`da8706f`、監査 `7403e1d`）にある文から取った。新しい主張はない。

## 英語

Where do the stationary points of an angle energy sit inside a spheroid, where do they enter or leave through the boundary, and is there anything else? This paper answers the question across all aspect ratios λ: besides the centre there is an axial pair of saddles for c_o < λ < b_o (about 0.408 to 0.644), an equatorial circle of saddles for b_p < λ < c_p (about 2.065 to 4.724), and nothing else. The pair reaches the poles at b_o; the circle enters from the boundary equator at b_p. Consequently an interior local minimizer exists exactly for c_o < λ < c_p, and there it is the centre alone.

The bifurcation patterns themselves are classical. What does not follow from general bifurcation theory is where they occur, the boundary events, and the absence of any further stationary component.

The full-family classification is conditional on six explicit finite computational assertions (C1-C6). Each is a finite, checkable assertion; any stationary point outside the classification would have to violate one of them. The oblate window λ in [2/5, 33/50] has a separate adopted verification record, and the sphere λ = 1 is proved analytically without computational input. Constrained minimizers on the boundary are not classified.

The global part required a dedicated method: a first box search left 21,254 of 31,340 boxes undecided, and the assertions became checkable only after a reduction to one-dimensional problems. The method, GeoEnclosure, is published separately (DOI: 10.5281/zenodo.24421364).

The author has read the entire manuscript using the Japanese reading translation and approves the manuscript and the AI-use disclosure. The author has not personally verified the code, computational records or supplementary materials, and relies on the recorded audits for those materials. Code in the source bundle is licensed MIT; the paper and prose materials are CC BY 4.0.

## 日本語

回転楕円体の内部で、角度エネルギーの停留点はどこにあるのか。どこで境界から出入りするのか。そして、ほかにはないのか。本論文は、この問いに軸比 λ の全体で答える。中心のほかにあるのは、c_o < λ < b_o（およそ 0.408 から 0.644）での軸上の鞍点の対と、b_p < λ < c_p（およそ 2.065 から 4.724）での赤道上の鞍点の円だけで、それ以外はない。対は b_o で極に達し、円は b_p で境界の赤道から入る。その結果、内部の極小は c_o < λ < c_p のときにだけ存在し、そこでは中心だけである。

分岐の型そのものは古典的である。一般の分岐理論から出てこないのは、それがどこで起こるか、境界での出入り、そして、ほかの停留成分がないことである。

全族の分類は、明示した六つの有限の計算の主張（C1〜C6）を条件とする。どれも有限で、確かめられる主張であり、分類の外に停留点があるなら、そのどれかを破っていなければならない。扁平側の区間 λ ∈ [2/5, 33/50] には別に採用された検証の記録があり、球 λ = 1 は計算を使わずに解析的に証明している。境界の上の制約つき極小は分類していない。

大域の部分には専用の方法が要った。最初の箱の探索では 31,340 個のうち 21,254 個が決まらず、一次元の問題への縮約で、はじめて主張が確かめられる形になった。この方法 GeoEnclosure は、別に公開している（DOI: 10.5281/zenodo.24421364）。

著者は、日本語の通読用の翻訳で本文の全体を読み、本論文と AI の利用の開示を承認した。コード、計算の記録、補足の資料は著者自身では確かめておらず、記録された監査に依っている。ソース一式の中のコードは MIT、論文と文章の資料は CC BY 4.0 である。
