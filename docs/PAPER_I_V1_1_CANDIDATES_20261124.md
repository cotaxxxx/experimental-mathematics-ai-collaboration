# 第一論文 v1.1 の候補（Judge 承認、2026-11-24 20:15）

作成：Claude（通常監査）。v1.0（DOI `10.5281/zenodo.24495446`、確認の記録 `9dfc0cb`）は変えない。ここに挙げるのは、次の版を作るときの候補だけである。作る時期は決めていない。

## 1. 関連研究に足す候補

先行研究・新規性の調査（2026-11-24、Judge から受領）で挙がった、v1.0 で未引用の文献。引くときは、これまでの決まりどおり、原文で定義と主張を確かめてからにする。

| 文献 | 実在の確認 | 本論文との関係 |
|---|---|---|
| P. Guan, L. Ni, Entropy and a convergence theorem for Gauss curvature flow in high dimension, JEMS 19 (2017) 3735–3761, doi:10.4171/JEMS/752 | chat が出版社のページで確認 | 基点 p の関数 ∫ log(h_K(u) − p·u) の最大点（エントロピー点）。h_K(u) − p·u は本論文の錐体積の重み (x − p)·n と同じ量。狭義凹で一意の最大点しかない点が、鞍点の対と円が現れる本論文との対比になる。最優先 |
| S. Sakata, Stationary radial centers and symmetry of convex polytopes, Colloq. Math. 159 (2020) 91–106, doi:10.4064/cm7712-11-2018 | chat が出版社のページで確認 | パラメータに依らず停留する中心と対称性。本論文で中心がすべての λ で停留点に残り、指数だけが変わることとの比較 |
| G. Domokos, Z. Lángi, On the average number of normals through points of a convex body, Studia Sci. Math. Hungar. 52 (2015), doi:10.1556/012.2015.52.4.1320 | chat が arXiv:1406.0813 で確認 | 点を通る法線の本数（α_p(x) = 0）と、エネルギーの停留（∇E = 0）は別の条件であることを一文で述べるのに使う |
| S. Sakata, Movement of centers with respect to various potentials, Trans. AMS 367 (2015) 8347–8381, doi:10.1090/tran/6138 | 未確認 | 核のパラメータに伴う中心の移動。本論文は形の比を動かす |
| S. Sakata, Every convex body has a unique illuminating center, J. Geom. 108 (2017) 655–662, doi:10.1007/s00022-016-0365-8 | 未確認 | 照明中心の一意性。角度エネルギーの停留点の一意性は意味しない |

- 調査の結論（同じエネルギーで全族を分類した先行研究は見つからない）は、v1.0 の主張と合っている。網羅的な文献調査（MathSciNet、zbMATH）ではない。
- O'Hara、Bertrand（Eq. (6) の −log cos との比較を含む）、Sakata 2016、Bott は v1.0 で引用済み。

## 2. 本文の候補

- v1.0 の 1 ページ目では、要旨が 31,340 個を「boxes」と呼ぶ（F3 で統一済み）。v1.1 で変える点はない。
- 変更は関連研究の節と参考文献だけにとどめ、定理、表、証明、数値、計算の資料は変えない。
