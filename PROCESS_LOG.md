# Process Log

This file is a chronological, append-only index of research-process events.

Detailed evidence remains in the original research repositories. Longer methodological case studies are stored under `docs/`.

## 2026-09-19 — C1b Phase 2 exception boundary

C1b Phase 2 stopped at coarse index 105 without a `segment_end`. The stop was classified as an implementation exception rather than a mathematical ABORT. Investigation moved through several hypotheses before identifying an asymmetry in exception handling between producer and checker paths. A first repair fixed the tube path and passed its controls, but production later stopped again in root localization. The scope audit was then widened from one caller to the full producer/checker exception boundary. Eight corresponding catch sites were identified and symmetrized under the adopted C-2a repair. During restart preparation, a separate two-layer pin structure was exposed when an incomplete pin update failed closed. The gate behaved as designed.

The same day's read-only audit also recovered C1c anchor-supply material from the sealed Phase 1 ledger: all 159 accepted slabs used the B path, with no A or missing cases. This establishes the presence of anchor-supply material; it does not by itself complete C1c assembly.

Detailed case: [C1b Phase 2 exception boundary](docs/2026-09-19-c1b-phase2-exception-boundary.md)

### Status at close

C-2a controls and preflight passed. Phase 2 had been restarted and was running. C1b was **not CERTIFIED**. The next decision point was production passage through coarse index 105.

## 2026-11-22 — REDDS v1.0 supreme canon: session handoff and acceptance log

- **Proposer:** Claude Code (special auditor). The proposing session identifier was not supplied.
- **Judge:** 古田勝士. **Recorder:** Dig (ChatGPT).
- **Decision:** Record the operational requirement to present the immutable REDDS v1.0 canon to each new participating AI session, verify its receipt and role, and distinguish receipt from permission to start work. Future proposal records must explicitly identify their **proposer**; revision decisions and history remain Judge-controlled.
- **Reception:** Claude Code reported reading and accepting the fixed canon. This status applies only to the reporting session and does not prove reception by other sessions.
- **Preservation:** Canonical file at `64115f7cb0f663fde47bbfd25e19c7ea42fccba1` remains unchanged. Triaxial research remains stopped; no restart or calculations were authorized by this record.

Detailed record: [REDDS v1.0 — Claude Code reception and session handoff](docs/2026-11-22-redds-v1-supreme-canon-session-handoff.md)
