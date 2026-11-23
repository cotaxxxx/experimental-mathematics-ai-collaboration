# chat の監査：第一論文 v0.5.2 の Zenodo 公開の束（説明文・メタデータ・ファイル）

2026-11-23、Claude（通常監査）。

**判定：このままでは公開しない。** 直す点が 2 つ（M1、M2）と、Judge の判断が要る点が 3 つ（J1〜J3）ある。

## 1. 対象と同一性

| ファイル | SHA-256 | 照合 |
|---|---|---|
| `Paper_I_v0_5_2_Integrated_EN-2.pdf` | `091019a9…b144` | 監査済みの v0.5.2（`8c56cf8`）と同じ |
| `Paper_I_v0_4_Computational_Supplement_EN.pdf` | `2441b82e…e481` | v0.4 の束の `SHA256SUMS` と同じ（中身は v0.4 から変わっていない） |
| `Paper_I_v0_5_2_Zenodo_Description_EN.md` | — | 下の §2 |
| `Paper_I_v0_5_2_Zenodo_Metadata_Draft.json`、`…_Review_JA.md` | — | 下の §3 |

ソースの zip（`Paper_I_v0_5_2_Manuscript_and_Verification.zip`）は受け取っていない。公開の前に、その SHA-256 が `c76656b0…fc4a` であることを確かめる。

## 2. 直す点

### M1（必須）：計算の監査の範囲を、PDF と説明文で正確に、同じ言い方で書く

- **事実（V24 の記録 `127be52` と STATE による）：**
  - V24 で chat が監査したのは、組み立ての論証と引用である。
  - その土台の区間計算（D5 など）については、次の確認がされている。
    - 抜き取った箱を、独立に計算し直した（例：200/200、201/201、20/20 の箱で下界が一致）。
    - 被覆を整数の算術で検査した。
    - 一部を Muse が監査した。
  - **一方、行われていないこと：**
    - すべての包囲を独立に流し直すこと。
    - producer の独立比較 2 件（採用後の補強として残っている）。
    - 外部の人間による解析補題の監査。
- **PDF v0.5.2 の書き方：**「including an independent audit of the supporting computations」は、全部を独立に計算し直したと読める。**言い過ぎである。**
  - この言い方は、chat が v0.5 の監査（`6b3388e`）で例として示した文に由来する。chat の誤りである。
- **説明文の書き方：**「a project-level audit of the argument and its supporting references」は、抜き取りの再計算に触れていない。逆に、**言い足りない。**
- **直し方：** PDF（v0.5.3）と説明文の両方を、同じ中身にする。例：
  > The assembly argument and its references were audited in a separate AI-assisted review; the underlying interval computations were checked by independent recomputation of sampled boxes and by exact coverage checks, not by a complete independent replay. Two producer-side comparisons and an external human review of the analytic lemmas remain open.
- Zenodo では、公開したあとファイルを差し替えられない。だから、PDF を直してから出す。

### M2（必須）：AI の利用の記載を、事実どおり、PDF と説明文でそろえる

- **PDF の書き方：** ChatGPT だけを挙げ、「Final scientific review and approval … are pending」で終わっている。このまま公開すると、「著者の承認がまだ」と書いた論文を公開することになる。
- **実際に使ったもの：**
  - ChatGPT（Codex、GPT-6.2 Astra を含む。OpenAI）：作る側。
  - Claude と Claude Code（Anthropic）：監査。
  - Muse（Meta）：構成要素の一部の監査。
- **直し方：** PDF と説明文の両方に、この三つを同じ書き方で挙げる。「承認待ち」の文は、公開の時点の事実（著者が確かめて承認した）に改める。

### 小さな点

- PDF の文書情報（Title、Author）が空である。v0.5.3 を作るときに埋める。
- 補足の PDF のファイル名は v0.4 のままである。説明文がその理由を書いているので、変えなくてよい。

## 3. Judge の判断が要る点

- **J1 所属：**
  - 下書きは「Independent researcher」で、原稿もそう書いている。
  - GeoEnclosure の Zenodo の記録では、所属を DAYBREAK にした。
  - どちらにそろえるかを決める。
- **J2 ライセンス：**
  - 案：記録全体は CC BY 4.0 とし、zip の中のコードには MIT の LICENSE を添える（GeoEnclosure と同じ組み合わせ）。
  - v0.5 の束を調べた範囲では、第三者のコードや、ライセンスの表示を持つファイルは見当たらなかった。
- **J3 GeoEnclosure の DOI との関係：**
  - 本文の §1 は「GeoEnclosure」の名前を使っている。
  - GeoEnclosure の記録は、DOI `10.5281/zenodo.24421364`（版 1.0）、すべての版をまとめた DOI `10.5281/zenodo.24421363`。DOI は Judge が公開した記録の画面で確かめた。
  - 「関連する研究」として、関係を References または Is related to でつなぐか、つながないかを決める。

## 4. 合っている点

- 題名、著者、ORCID、版、言語、種類（Preprint）、キーワード。
- 説明文の条件付きの分類（臨界値の近い値も含めて、表 1・表 2 と一致する）。
- 球を命題 4.2 で計算なしに証明していること。
- 扁平側を [2/5, 33/50] に限っていること。
- 「提出用の認証ではない」と明記していること。
- hash は同一性を示すだけで、数学の正しさを示すものではない、と書いていること。
- 架空の資金、学術誌、DOI を書いていないこと。

## 5. Judge の裁定（2026-11-23）

- **J1：** 所属は DAYBREAK にそろえる。Zenodo の所属は DAYBREAK とし、原稿の表紙は「DAYBREAK (independent research)」とする。
- **J2：** 記録全体は CC BY 4.0 とする。zip の中のコードには MIT の LICENSE を添える。
- **J3：** GeoEnclosure の記録（`10.5281/zenodo.24421364`）と、関係 References でつなぐ。論文の参考文献にも、この DOI を足す。

M1・M2 と J1・J3 の原稿への反映は v0.5.3 で行い、chat が差分を監査してから公開する。
