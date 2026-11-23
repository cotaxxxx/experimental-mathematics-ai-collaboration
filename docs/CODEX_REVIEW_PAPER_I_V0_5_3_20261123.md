# 第一論文 v0.5.3 査読所見

| 項目 | 記録 |
| --- | --- |
| 査読日 | 2026年11月23日 |
| 査読・改訂提案 | Codex（OpenAI） |
| 対象 | Katsushi Furuta, *Counting stationary points and saddle circles of a cone-volume-weighted angle energy on spheroids*, Paper I v0.5.3、36頁 |
| 記録の種別 | 原稿への査読所見と改訂提案 |
| 対象原稿のソース | [Paper I v0.5.3 `354ffaabc1be34618c182fcc9aebbb20e7e73333`](https://github.com/cotaxxxx/bg-spheroid-family/tree/354ffaabc1be34618c182fcc9aebbb20e7e73333/manuscripts/2026-11-23/Paper_I_v0_5_3) |
| 対象PDFのSHA-256 | `2054ebe7eeb194351e836bb32ae10e5ff62a0073d03bfb8f5d198b77c196ccc4` |
| 対応する検証ZIPのSHA-256 | `5be67aae44517525180a1524b1336ea45a63a35f12905e0527caad67a3a56c5d` |

## 査読判定

**条件付きの研究稿として公開できる段階にある。Experimental Mathematicsへの全族分類の証明としての投稿を想定する場合は、大幅改訂後に再査読を勧める。** 現行の公開工程は、Judge裁定に基づくZenodo公開準備と学術誌投稿の保留である。[第一論文の公開方針の裁定](https://github.com/cotaxxxx/experimental-mathematics-ai-collaboration/blob/8c56cf8cd9172900a53a15d621d8c084d1933482/docs/2026-11-23-JUDGE-PAPER-I-ZENODO-PUBLICATION-RULING.md)

論文の中心は式 (6.5) にある。赤道上の接方向四階微分の符号から半径方向の単調性を得て、停留円の数を中心と境界の二つの符号で決める。中心付近では四階微分を直接評価し、境界付近では弦で表示した二階微分の差を使う。最初の符号判定で多くの箱が未判定となり、そこから判定に使う量を選び直す過程は、実験と形式的結果を結びつける同誌の趣旨に沿う。[Experimental Mathematicsの誌面方針](https://www.tandfonline.com/journals/uexm20)

## 主要な改訂提案

1. **C2の軸根の個数を、計算記録から追跡できる証明にする（§8.1、pp. 25–26）。** C2(3)は正の軸根が一つであるという分類結果を仮定している。本文は160区画、159本の根の管、極近傍の符号条件を挙げている。どのパラメータ区分でどの条件が存在・一意性・排除を与えるかを読めるように、端点符号、単調区間、その外側の排除、共有端点の扱いを表にする。投稿用の計算証拠の整備では、この接続を最優先とする。[軸上分類の組み立て v1.1](https://github.com/cotaxxxx/bg-spheroid-family/blob/2c084bc05e5dd0b0d7deeb9f9c293deeb1d5e40a/drafts/2026-11-16/C_AXIS_GLOBAL_COVER_ASSEMBLY_V1/C_AXIAL_GLOBAL_COVER_ASSEMBLY_DRAFT_V1.md)
2. **現行版の再現手順を一か所にまとめる（§10、検証ZIP）。** 本文と `verification/cap.py` はC6の全1,024箱の第二実装による再評価を記録している。同梱の旧 `REPRODUCTION.md` には、第二実装による全箱積分を主張しないとする以前の記述が残っている。$c_o$ の $10^{-12}$ 幅の括弧も、本文と `verification/endpoints.py` にあり、旧出典ノートは粗い括弧を案内している。履歴を保存し、現行の案内にはC1〜C6ごとの入力・実装・台帳・実行コマンドの対応表を置く。C1とC3・C4の鉛直符号では、全域の被覆と抜き取り再評価の範囲を明記する。
3. **§10の “English drafting” が指す作業を確定する。** Taylor & Francisの方針は、生成AIによる原稿や節の初稿作成を禁じ、著者が確認した翻訳や語句・文法等の編集を認めている。翻訳や英文編集だった箇所は実際の作業を記す。生成AIで初稿を作った箇所があれば、著者自身が研究記録から起稿し直す。投稿用の開示は、使用したツールと版、用途、著者による内容とコードの確認を、完了した事実に基づいて記載する。[Taylor & FrancisのAI利用方針](https://authorservices.taylorandfrancis.com/editorial-policies/using-ai-in-your-research-and-manuscript-preparations/)

## 数学と構成

- **扁平側の枝の両端を§6.1で示す。** 図2には $z_*(c_o+)=0$ と $z_*(b_o-)=1$ が描かれている。$c_o$ 側ではC2の内点での零点排除と極での非零性から、連続性により唯一の集積点が $0$ になる。$b_o$ 側では $h_o(b_o)>0$ から $g(z,\lambda)/z>0$ が中心近傍で一様に成り立つので、枝は中心に戻れない。C2が内点の他の極限を排除するため、極限は $1$ である。
- **球と薄い扁平端の解析結果を要旨に載せる。** §4.2は球を扱い、§5は $0<\lambda\le 1/32$ で中心が唯一の内点停留点であり、指数1の鞍点で、境界の全勾配トレースに零点がないことを解析的に示している。これらは全族分類の計算上の仮定に依存しない。
- **C4の形状微分の用途を明記する。** $H_\lambda<0$ を使うのは、停留円の参照半径が形状パラメータに関して減少することを示す段階である。個数・存在範囲・型を決める上では、鉛直方向の排除、半径方向の単調性、中心と境界の符号が必要になる。

## 今回確認した範囲

球のTaylor係数と薄い扁平側の式 (5.2) を再導出し、本文と一致した。$c_o$ の狭い括弧の両端と $b_o$ は、非区間積分で符号と位置を照合した。添付PDFはZIP内のPDFとバイト単位で一致し、付属のSHA-256台帳の153項目を照合した。保存済み計算記録の被覆・有理数比較の検査（`verification/check.py`）を再現し、V24原本をGitHub固定版とバイト単位で照合した。C1〜C6を計算核から全件再評価する作業は未実施である。[V24固定原本](https://github.com/cotaxxxx/bg-spheroid-family/blob/127be52046e9498d1306fe3d35c3e02e91c636de/runs/2026-11-16/D_OB_GLOBAL_CLOSED_V24/JUDGE_RULING_D_OB_GLOBAL_CLOSED_20261116.md)
