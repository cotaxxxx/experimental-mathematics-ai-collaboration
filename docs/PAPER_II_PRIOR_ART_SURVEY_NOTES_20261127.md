# 論文 II（候補B）先行研究の予備調査メモ（2026-11-27 JST）

出所：Dig の予備調査（Judge が chat に共有）。chat（Claude）が整理。**書誌は未照合**（原稿に入れる前に 1 件ずつ原典で確認する）。

## 結論（予備）
同じ角度エネルギーについて、三軸楕円体の形状空間の四本の零曲線と六組の関係を確定した先行例は、調査範囲では未確認。世界初とは書かない。新規性は「このエネルギーに固有の分岐構造の確定」に置く。

## 候補文献（要照合）
| 分類 | 文献 | 関係 |
|---|---|---|
| 角度の量 | Akgül ほか 2007（SMI、doi:10.1109/SMI.2007.27） | 放射方向と法線の内積を形状特徴量に使用 |
| 角度の量 | Santos・Coutinho・Soares 2022（J. Chem. Inf. Model.、doi:10.1021/acs.jcim.2c00673） | 楕円体の deflection angle の分布。基点の変分問題ではない |
| 凸幾何 | Böröczky ほか 2020, The Gauss Image Problem（CPAM、doi:10.1002/cpa.21898） | radial Gauss map |
| 内部点の汎関数 | Herburt・Moszyńska・Peradzyński 2005（doi:10.1007/s11040-005-2968-4） | 凸体の放射中心 |
| 分岐 | Domokos・Holmes・Lángi 2016（J. Nonlinear Sci.、doi:10.1007/s00332-016-9319-4） | 形状変化による勾配場の分岐。最重要の比較対象、論文 III にも関係 |
| 精度保証 | Krawczyk 1969、Plantinga–Vegter 2004、Hijazi–Breuel 2007、Rump 2010、Carvalho ほか 1998（最後は特に要確認） | 陰関数曲線の配置の区間演算による検証 |

論文 I v1.1 の候補（Guan–Ni、Sakata、Domokos–Lángi；PAPER_I_V1_1_CANDIDATES_20261124.md）と合わせて扱う。

## 原稿への反映（chat の指摘）
1. **用語**：Z₁, Z₂ は「中心 Hessian の零曲線」、∂₁, ∂₂ は「極点トレースの零曲線」と書く。「停留点が生まれる曲線」とは書かない（実際の生成・消滅には局所の分岐条件の検証が別に要る）。
2. 区間演算による曲線配置の検証そのものには先行研究がある。GeoEnclosure の寄与は、幾何の構造で計算を減らした具体的な過程（v1→v4：核不変、5 時間 PARTIAL → 3 分で被覆完了）で示す。
3. 題名案：Four Critical Curves and Their Intersections: An Angle Energy on Triaxial Ellipsoids（「critical」の語は 1 の用語と整合させる）。
