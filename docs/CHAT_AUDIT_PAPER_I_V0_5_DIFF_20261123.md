# chat の監査：第一論文 v0.4 → v0.5 の差分

2026-11-23、Claude（通常監査）。

**判定：数学の内容は PASS。** ただし、Zenodo で公開する前に、直す点が一つある（§3 の R1）。

## 1. 対象

| 版 | ファイル | SHA-256 |
|---|---|---|
| v0.4 | `bg-spheroid-family` 枝 `codex/paper-i-v0.4-20261120` の `Paper_I_v0_4_Manuscript_and_Verification.zip` | `57ee540bb8f3679e1b5abfaf043d6c961d934a981bddfb9d0dba0bd32a4c4d91`（同じ枝の `Paper_I_v0_4.sha256` と一致） |
| v0.5 | Judge から受け取った `Paper_I_v0_5_Manuscript_and_Verification.zip`（146 ファイル） | `ed0c20f1cb8830e7d72a94e9d3d9f7aca5a1be1b56afbb85cc44f21d1a8ab814` |
| v0.5 の PDF | `Paper_I_v0_5_Integrated_EN.pdf`（36 ページ） | `91c5f11cd02922080ce9c2aaad9ee233d393f44e32d6977a63ffce630c6da300` |

v0.5 の束の中の `SHA256SUMS` は、全部のファイルで一致した。

## 2. 変わったところ（二つの木を、ファイルごとに比べた）

**中身が変わったファイル：** `main.tex`、`sections/core.tex`、`README.md`、`SHA256SUMS`。
**足されたファイル：** `REVISION_v0_5_JA.md`、`SOURCE_DIFF_v0_4_to_v0_5.patch`、`provenance/`。
**PDF の名前：** v0.4 から v0.5 に変わった。

検証のコード、計算の結果、監査の台帳、図、計算の補足の PDF、参考文献は、**すべて v0.4 とバイト単位で同じ**。

| 箇所 | 変更 | 確認 |
|---|---|---|
| `main.tex` 日付 | v0.4 → v0.5（2026-11-23） | OK |
| `main.tex` 「Main conclusion and certification scope」（要旨の後、目次の前） | 条件付きの分類の要約と、証明の範囲の説明 | 分類の要約は、定理 3.1 と表 2 の各行と一致する（中心、c_o < λ < b_o の軸上の鞍点の対、b_p < λ < c_p の鞍点円、c_o と c_p での中心の型の変化、λ = b_o の極と λ = b_p の赤道円での境界の零点）。範囲の文は §3 の R1 を見よ |
| `core.tex` §3 の末尾「Scope of the separate oblate closure」 | 扁平側の CLOSED の範囲は [2/5, 33/50] に限る、という段落 | 事実として正しい。言い方は §3 の R1 を見よ |
| `core.tex` 命題 4.2 の証明：偶関数性 | θ(−r, ψ) = −θ(r, π − ψ) と ψ → π − ψ の置き換えから e(−r) = e(r) を示し、奇数次の係数が 0 になると書いた | 正しい（1 − r cosψ の因子も置き換えで対応する）。SP-01 の監査の補足 2 を満たす |
| 同：優収束 | 1/2 ≤ r < 1 で Δ ≥ 2r(1 − cosψ)、sin²ψ/Δ ≤ 1/r、0 ≤ θ ≤ π/2、\|2 − r² − r cosψ\| ≤ 3 から、被積分関数が一様に有界。各点の極限 θ(1, ψ) = (π − ψ)/2、Δ(1, ψ) = 2(1 − cosψ) | 正しい。SP-01 の監査の補足 1 を満たす |
| 同：境界のトレース | g∂(q₀; 1) = e′(1⁻)q₀ が定義 2.1 のトレースそのものであり、境界に沿った接線方向の勾配ではない、と明記した | 正しい |

**ページ数：** 36 のままで、削られた箇所はない。差分は追加と置き換えだけで、削除は表現を直した 2 文だけである。

**数学の主張：** 定理 3.1、表 1、表 2、C1〜C6 の文、数値は変わっていない。

## 3. 直す点

**R1（Zenodo で公開する前に必要）：内部の用語を論文から外す。**

- v0.5 は、論文の本文に「The Judge's V24 ruling records *CLOSED*」と書いている（目次の前の節と §3 の末尾の 2 か所）。末尾の文「changes no … evidence grade」も同じく内部の用語である。
- v0.4 の本文には「Judge」は一度も出てこない。
- 外の読者には、「Judge」「V24」「CLOSED」「evidence grade」の意味が分からない。しかも Judge は著者自身なので、第三者の判定と誤って読まれるおそれがある。
- **直し方の例：**「In the author's verification records (record V24, 16 November 2026; see Section 10), the oblate window λ ∈ [2/5, 33/50] has been checked and closed, including an independent audit of the supporting computations.」のように書く。
  - 誰が何をしたかを、外の読者に分かる言葉で書く。
  - 記録の場所を、固定した参照（commit または DOI）で示す。
  - 「evidence grade」は「the status of the computational inputs」などに言い換える。
- 「Proposition 4.2 independently proves」の「independently」は、「without computational input」と書くほうが誤解がない。

## 4. 範囲

- この監査は、v0.4 → v0.5 の差分だけを対象とする。v0.4 で変わっていない部分の数学は、ここでは見直していない（命題 4.2 は別に監査済み：`CHAT_AUDIT_PAPER_I_PROP_4_2_20261123.md`）。
- PDF は束に入っていたものを確かめた。ソースから組み直してはいない。
