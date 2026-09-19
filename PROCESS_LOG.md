# Process Log

This file is a chronological, append-only index of research-process events.

Detailed evidence remains in the original research repositories. Longer methodological case studies are stored under `docs/`.

## 2026-09-19 — C1b Phase 2 exception boundary

C1b Phase 2 stopped at coarse index 105 without a `segment_end`. The stop was classified as an implementation exception rather than a mathematical ABORT. Investigation moved through several hypotheses before identifying an asymmetry in exception handling between producer and checker paths. A first repair fixed the tube path and passed its controls, but production later stopped again in root localization. The scope audit was then widened from one caller to the full producer/checker exception boundary. Eight corresponding catch sites were identified and symmetrized under the adopted C-2a repair. During restart preparation, a separate two-layer pin structure was exposed when an incomplete pin update failed closed. The gate behaved as designed.

The same day's read-only audit also recovered C1c anchor-supply material from the sealed Phase 1 ledger: all 159 accepted slabs used the B path, with no A or missing cases. This establishes the presence of anchor-supply material; it does not by itself complete C1c assembly.

Detailed case: [C1b Phase 2 exception boundary](docs/2026-09-19-c1b-phase2-exception-boundary.md)

### Status at close

C-2a controls and preflight passed. Phase 2 had been restarted and was running. C1b was **not CERTIFIED**. The next decision point was production passage through coarse index 105.
