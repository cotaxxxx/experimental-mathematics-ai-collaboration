# Corrections Index

This file indexes material corrections in the research process. It is not a list of every conversational mistake. An entry belongs here when an incorrect diagnosis, assumption, or report materially affected the research path, audit, or interpretation.

Each entry records: what was wrong, what evidence corrected it, and where the detailed process record is preserved.

## 2026-09-19 — C1b Phase 2 exception-boundary investigation

**Incorrect module attribution.** The failing function was initially associated with `monotone_tube_interval_checker.py`, confusing the location of the exception class with the location of the function that raised it. Source-path inspection corrected the attribution.

**Incorrect producer interpretation.** It was initially stated that the producer had positive `q` on all GT boxes. The producer in fact encountered the same local guard condition but caught it, so the event did not appear in stdout in the same way. Producer/checker enclosure comparison eliminated the alternative BITS explanation.

**Repair recommendation reversal.** The A-2-style repair direction was recommended, withdrawn, and later restored after direct evidence established exception-boundary asymmetry.

**Incomplete exception-site audit.** The first repair audited the exception boundary inside `_tube_gt_eval` but did not enumerate all callers of `gt_box`. Production therefore passed the repaired tube path and later stopped at root localization. A full producer/checker comparison then identified eight corresponding ValueError catch locations and led to C-2a.

**Faulty audit script heuristic.** An exception-counting script classified a site by searching only a fixed number of lines after a call, causing the `root_localize` try block to be falsely reported as bare. Direct structural inspection corrected the result.

**Incomplete pin update.** Only the `expected_blobs` layer was initially updated before ignition. The numeric import closure then failed closed, revealing that the pinning system had two layers. This was treated as evidence that the launch gate worked rather than as a mathematical failure.

Detailed case: [C1b Phase 2 exception boundary](docs/2026-09-19-c1b-phase2-exception-boundary.md)
