# 論文 II 原稿の骨子（2026-11-27 JST、chat 起草・Judge 承認前）

題：**A Map of the Angle Energy on Triaxial Ellipsoids**／三軸楕円体の角度エネルギー地図
副題：対応条件の結果で決定（A: Four Zero Curves and Their Intersections ／ B: Four Threshold Curves of Stationary Points）
公開：Zenodo のみ。著者 Katsushi Furuta（DAYBREAK）。

## 節の構成
1. **Introduction** — 角度エネルギー、論文 I の結果（辺の上の 4 点）、本論文の問い（面の中でどうつながるか）、主結果の図（地図）。
2. **Setting** — 形 diag(1,y,z)、x=1 中間軸、R=[1/4,1]×[1,7]、参照球表示、四つの量 A_y, A_x, T_y, T_x の定義と正則性。座標の対応（V56：y=1/s, z=t）。
3. **Main theorem (configuration)** — 下の定理 1。
4. **Local correspondence** — 定理 C（中心）・定理 P（極）と、九つの係数の符号の結果（**結果待ち**）。対称辺 y=1 の停留円、交点 Z₁∩∂₂ の二事象。
5. **Proof of Theorem 1** — 符号箱による被覆、帯（両面反符号＋横断微分）、境界根からの接続、共有端点（差から (1−y) を外す）、帯の拡張、交点（Poincaré–Miranda＋傾きの積、Krawczyk）。
6. **Computation and verification** — MPFR 核、角度求積と剰余、台帳、検査器、独立監査、実行記録の表。
7. **How the proof was closed (GeoEnclosure)** — v1→v4 の表（核不変）。正直な限界。
8. **Relation to earlier work** — 凸幾何（錐体積測度、放射 Gauss 写像）、内部点の汎関数の臨界点、分岐の分類（Domokos–Holmes–Lángi）、法線の本数の古典との違い（短い段落）、精度保証（枝の検証付き追跡）。
9. **Scope and open problems** — R の外、各領域の停留点の総数（H3・H12・HB、球全体）、等級と前提。
10. **Process and AI disclosure**、**Data and code availability**、**References**。
付録：記号表、コミットとハッシュの一覧、日本語要旨。

## 定理 1（採用済み 2d2576e。文面案）
Let R=[1/4,1]×[1,7] and let Z₁={A_y=0}, Z₂={A_x=0}, ∂₁={T_y=0}, ∂₂={T_x=0} in R.
(i) Each of the four sets is a single arc joining two boundary points of R, a graph over one coordinate on each certified strip.
(ii) Z₁∩Z₂={c_p} and ∂₁∩∂₂={b_p}, both on the edge y=1.
(iii) Z₁∩∂₁=Z₂∩∂₁=Z₂∩∂₂=∅.
(iv) Z₁∩∂₂ is exactly one point, in the interior of R, the crossing is transversal, and y*∈[0.63813110, 0.63821937], z*∈[2.29643023, 2.29674050].
（端点の座標と区間は原稿作成時に台帳の辺根から記入。弧の両端がどの辺にあるかも明記する。）

## 定理 2（対応、**結果待ち**。文面の型）
On each arc, away from [the certified exceptional set], crossing the arc transversally creates or absorbs exactly one pair of stationary points at the centre (Z arcs) or at the poles ±e_i (∂ arcs), on the side A_i·B_i<0, resp. T_i·N_i>0. On the edge y=1 the pair is replaced by one stationary circle.

## 図の一覧
F1 地図（四曲線・c_p・b_p・交点）／F2 論文 I の 4 点との接続（辺の拡大）／F3 対応条件の符号（曲線に沿った色分け、**結果待ち**）／F4 v2 の未決箱と b_p（方法の説明）／F5 交点の箱 X と小箱。

## 言わないこと
R の外。各領域の停留点の総数。大域の条件 H3・H12・HB。世界初。
