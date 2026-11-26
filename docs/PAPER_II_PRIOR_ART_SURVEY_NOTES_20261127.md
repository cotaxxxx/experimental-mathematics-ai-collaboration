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

## 追記：Claude Code による調査の査読（2026-11-27 01:06 JST 受領、chat 整理）
Claude Code は調査報告だけを読んだ（候補 B の原本は未読、文献の全文も未読）。

### 裏が取れなかった記述（引く前に本文で確認）
- Santos・Coutinho・Soares 2022：書誌（J. Chem. Inf. Model. 62(19), 4690–4701）は確認。要旨には「deflection angle」「五種類の楕円体」が見当たらない。該当箇所を示せるまで「特に注目」の扱いにしない。
- Carvalho・de Figueiredo・Cavalcanti, Computing Arrangements of Implicit Curves：実在。「1998 年」「矩形領域内」は未確認。
- Domokos–Holmes–Lángi 2016：「二パラメータ族も対象」は未確認（主題は 1 パラメータ族の一般的な分岐の可能性）。

### 抜けていた関連分野（追加候補、書誌は要確認）
1. **楕円体への法線の本数と焦曲面**（いちばん近い古典）。θ(p,x)=0 は p が x の法線上にあるとき。Joets–Ribotta 1999 ほか、19 世紀の古典。
2. **錐体積測度**：対数 Minkowski 問題（Böröczky–Lutwak–Yang–Zhang）、双対曲率測度（Huang–Lutwak–Yang–Zhang）。
3. 内部点の関数の臨界点で中心を定める系統（Santaló 点など）。論文 I の関連研究から引き継ぐ。
4. 精度保証は「曲線の配置」より「解の枝の検証付き追跡」（van den Berg–Lessard–Mischaikow、Kearfott）と分岐点の検証が近い。

### 原稿への制約（重要）
- **零曲線と停留点の出入りの対応は、いくつかの符号条件が成り立つ範囲でしか読めない。** 初期の数値地図では、主矩形の外でその条件の 1 つが数値的に破れていた。領域 R でこの条件がどうなっているかを原稿で明示する（未確認事項として残す）。
- 題名は「Critical Curves」ではなく「Zero Curves」（または threshold curves）にする。証明したのは零曲線の配置で、分岐そのものではない。

## 題名（Judge 決定 2026-11-27 05:1x JST、時刻はこのコミットを正とする）
- 主題：**三軸楕円体の角度エネルギー地図**／*A Map of the Angle Energy on Triaxial Ellipsoids*（Judge の案「3軸楕円体エネルギー地図」に「角度」を加えた形をボタンで選択）
- 副題は対応条件（04051b6）の結果を見てから決める。
  - A：四本の零曲線とその交差／*Four Zero Curves and Their Intersections*（配置のみで言える）
  - B：停留点が出入りする四本の境目／*Four Threshold Curves of Stationary Points*（対応条件が全区間で成立した場合のみ）
- 先行研究との位置づけ（chat 整理）：道具は既存／近い問題（法線の本数と焦曲面、Domokos–Holmes–Lángi、放射中心）は量が異なる／同一の問題の先行例は未確認。本文に「法線の本数の古典との違い」の節を置く。
