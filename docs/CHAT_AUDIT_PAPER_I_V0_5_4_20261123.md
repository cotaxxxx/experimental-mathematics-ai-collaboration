# chat の監査：第一論文 v0.5.4（v0.5.2 からの差分、Zenodo の束の監査 `8c28d44`・裁定 `6bed2a8` との照合）

2026-11-23、Claude（通常監査）。

**判定：数学の追加は PASS。ただし、公開の条件はまだ満たしていない。** 裁定 J1・J3 が入っていない。M2 が足りない。著者の確認が「pending」のままである。

## 1. 対象

- `Paper_I_v0_5_4_Integrated_EN.pdf`（37 ページ）
  - SHA-256 `6fa3a41e1ea1f5e79a65e4f5b1f805d67827bbd583c7c6b9ef023b0e5de722bb`
  - 添付の一覧と一致した。
  - PDF の文書情報（Title、Author）は埋まっている。
- 添付の文書：
  - `Paper_I_v0_5_4_Revision_Notes_JA.md`
  - `C2_AXIS_CENSUS_TRACE_v0_5_4.md`
  - `CURRENT_REPRODUCTION_v0_5_4.md`
  - `AI_PROVENANCE_REVIEW_v0_5_4.md`
- 改訂の根拠：Codex の査読 `docs/CODEX_REVIEW_PAPER_I_V0_5_3_20261123.md`（`f5f345f`、枝 `codex/paper-i-v0.5.3-review-20261123`）。
- 監査のしかたと範囲：
  - v0.5.3 の PDF は GitHub（`bg-spheroid-family` の `354ffaa`）に置かれていないので、v0.5.2 → v0.5.4 の本文を全文で比べた。v0.5.3 の差分は、chat は個別には監査していない。
  - ソースの zip と patch は受け取っていない。

## 2. 新しい数学の記述（PASS）

| 箇所 | 中身 | 確認 |
|---|---|---|
| 要旨 | 球は内部の停留点が唯一の最小点。0 < λ ≤ 1/32 では、内部の停留点は指数 1 の鞍点である中心だけで、境界のトレースに零点はない | §5 の内容（Lemma 5.1 の赤道の不等式、Lemma 5.2 の軸方向の一様な凹性）と命題 4.2 をまとめたもの。§5 の本文は v0.4 から変わっていない。要旨は既存の結果の要約で、新しい主張ではない |
| §6.1 端点 | z\*(c_o+) = 0、z\*(b_o−) = 1 | 論理を確かめた。c_o 側：集積点 z ∈ (0, 1] は g(·, c_o) の零点になる。C2 の第 2 行（正の根なし）と極での負の符号から 0 しかない。b_o 側：g_z(0, b_o) = a_c(b_o) > 0 から、λ が b_o に近く z が小さいとき、一様に g/z > 0 になる。したがって枝は中心に戻らない。C2 の第 9 行で内部の零点が除かれるので、極限は 1 である。C2 とトレースの連続性に依る、条件付きの論証として正しい |
| §6.3 | H_λ < 0 は半径の減少に使い、円の個数・存在・型は別の符号で決まる | 正しい区別 |
| §8 C2 の表（10 区分） | 下半分と上半分の門、λ_x、各区分の N₊、共有端点の扱い | 一次記録 v1.1（`2c084bc`、本日 chat が差分監査で PASS）の §2 の表と一致する。N₊ は 0、0、1、1、1、1、1、1、0、0 で、内部の停留点の数 1 → 3 → 1 と合う。83/200 と 703/1600 と 5/8 の扱い、t = 1 を数えないことも一次記録どおり |

## 3. 公開の前に残っている点

1. **J1（裁定どおりでない）：** 表紙の所属が「Independent researcher」のままである。裁定は「DAYBREAK (independent research)」。
2. **J3（裁定どおりでない）：** GeoEnclosure の DOI（`10.5281/zenodo.24421364`）が参考文献にない。§1 では「GeoEnclosure」の名前を使っている。
3. **M2（足りない）：** AI の利用の段落が、ChatGPT（OpenAI）と Claude（Anthropic）だけを挙げている。
   - 足りないもの：Codex と GPT-6.2 Astra（OpenAI。Codex は v0.5.3 の査読もした）、Claude Code（Anthropic）、Muse（Meta。D5 などの一部の監査）。
   - v0.5.4 の文は、「Claude が支援した」の範囲を「論証・出典・差分の監査」としている。これは事実と合う。
4. **M1（言い足りない側に寄った）：**
   - §3 の末尾は「A separate project AI audit checked the assembly and source citations, not the computations anew」と書いている。
   - 実際には、扁平側の窓 [2/5, 33/50] を支える D5 などについて、次の確認がされている。
     - 抜き取った箱の独立な計算し直し（200/200、201/201、20/20 で下界が一致）
     - 被覆の整数での検査
     - Muse の監査
   - 「not the computations anew」は、これらを打ち消してしまう。
   - 例：「…checked the assembly and source citations; the supporting interval computations were checked by independent recomputation of sampled boxes and exact coverage checks, not by a complete replay.」
   - `CURRENT_REPRODUCTION_v0_5_4.md` は、C1〜C6 ごとに抜き取りの範囲を正確に書いている。本文もそれとそろえる。
5. **著者の確認（著者だけができる）：**
   - AI の段落は「Author verification … is pending」で終わっている。
   - 公開は著者の承認そのものなので、著者が確認を終え、文を事実（確認して承認した）に改めてから公開する。
   - 英文の初稿の由来（`AI_PROVENANCE_REVIEW`）は、学術誌に投稿するときの問題である。Zenodo の公開では、由来がまだ確定していないことを正直に書いておけば足りる。今の文はそうなっている。
6. **J2：** zip の LICENSE（コードは MIT、文書は CC BY 4.0）は、zip を受け取っていないので確かめていない。

## 4. 合っている点

- 定理 3.1、表 1、表 2、C1〜C6 の主張と定数は変わっていない。
- 「提出用の認証ではない」と明記している。
- `CURRENT_REPRODUCTION_v0_5_4.md` は、C1〜C6 ごとに、producer の被覆、抜き取りの再計算、第二の実装の範囲を分けて書いている。言い過ぎがない、良い表である。
