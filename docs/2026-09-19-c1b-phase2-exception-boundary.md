# C1b Phase 2: Exception-Boundary Case Study

> **Process provenance:** The underlying computational and certification records remain in the original project repositories. This repository references those records rather than replacing them, preserving the distinction between mathematical evidence and retrospective methodological analysis.

## Status of this document

This is a retrospective methodological reconstruction of the 2026-09-19 investigation. It is **not** a certification artifact and does not replace the original source code, stdout, JSONL ledgers, checker replay, commits, hashes, or predeclared controls.

The purpose is to preserve the sequence of observation, doubt, stop, and Re without rewriting the investigation into a cleaner story than the one that occurred.

## 1. Initial observation

The first Phase 2 run stopped at coarse index 105, attempt sequence 142, depth 0, on the lambda interval `[93/160, 233/400]`. There was no `segment_end`.

The immediate classification was important: this was not evidence of a mathematical ABORT. Execution had terminated through an implementation exception in the checker path.

The traceback passed through the checker tube evaluation into `gt_box` and then checker refinement, where the condition reported was `ordinary q not positive`.

## 2. Competing hypotheses

The investigation did not begin with the final diagnosis.

One line of suspicion concerned a possible corner-branch difference. That explanation was rejected after inspection showed the relevant corner-hull condition was not active in the failing path.

A second possibility was a precision or BITS difference between producer and checker. Direct comparison of the relevant `q` enclosure eliminated that explanation: producer and checker agreed on the enclosure.

The remaining structural difference was exception handling. The producer treated the local box failure as an unresolved box-level event, whereas the checker allowed the corresponding exception to escape.

## 3. First diagnosis: exception-boundary asymmetry

The first confirmed defect was therefore an exception-boundary asymmetry rather than a mathematical disagreement.

A checker-local exception class, `BoxLocalGuard(VerificationError)`, was introduced so that box-local guard failures could be distinguished from ordinary verifier failures. The repair was deliberately narrow:

- producer behavior was unchanged;
- mathematical guards were unchanged;
- BITS was unchanged;
- the numerical quantity implementation was unchanged;
- plain `VerificationError` remained fail-closed.

The first repair made `_tube_gt_eval` catch the box-local guard in the same logical role in which the producer caught its local failure.

## 4. Acceptance controls for the first repair

The repair was not accepted merely because the failing run could proceed in a local test. Controls were used to establish the intended boundary.

The controls checked that the fault box raised the box-local guard, that `_tube_gt_eval` converted that event into an unresolved result, that ordinary verifier failures still propagated, that producer/checker logic agreed at the intended level, and that the staged tube computation could move from unresolved T0/T1 behavior to closure at T2.

These controls passed.

## 5. Production validation — and a second stop

A new production run reached the same coarse-105 region.

This time the tube stages executed as intended. The first repair therefore received a genuine production-path validation for the tube path.

However, the run stopped later in root localization with the same box-local condition escaping through a different caller.

This was a crucial correction to the scope of the first diagnosis. The first repair was not wrong at the location it addressed; the audit boundary had been too narrow. The investigation had inspected the exception boundary inside `_tube_gt_eval` without enumerating every checker caller of `gt_box`.

## 6. C-2a: full exception-boundary symmetry

The next step was not another isolated patch. The producer and checker exception sites were compared systematically.

Eight corresponding producer/checker ValueError catch locations were identified. One was already covered by the first repair. The remaining seven checker locations were changed to recognize `BoxLocalGuard` at the same logical boundary.

The repair was constrained by a predeclared scope:

- no producer changes;
- no change to Phase 1 sealed records;
- no change to mathematical guards;
- no BITS change;
- no change to the underlying quantity computation;
- no widening to plain `VerificationError`.

Acceptance controls required all eight checker locations to include the box-local guard, a one-to-one producer/checker correspondence, no unintended changes to non-target exception sites, reproduction of the coarse-105 depth-0 unresolved root behavior, and logical agreement with producer behavior.

The controls and preflight passed.

## 7. A pinning incident exposed another layer

During restart preparation, only one apparent pin layer — the seven `expected_blobs` entries — was initially updated.

Ignition did not proceed. The numeric import closure failed closed.

This revealed that the launch gate contained two relevant pin layers rather than one. The event was therefore recorded not as a failure of the mathematics but as evidence that the gate was performing its intended function: an incomplete update did not silently enter production.

## 8. Restart state

After C-2a, the full restart began from coarse index 0 under the newly pinned commit. Early observation showed normal CPU activity, passing preflight, and progression through the initial coarse cells.

At the close of this case record, the decisive next field test had not yet occurred: the run still needed to pass coarse index 105 in production.

Accordingly:

> **C-2a controls/preflight: PASS. Phase 2: RUNNING. C1b: NOT CERTIFIED.**

No stronger conclusion is licensed by this document.

## 9. Corrections preserved rather than erased

Several mistakes occurred during the investigation and are part of the methodological record.

The failing module was initially named incorrectly because the location of the exception class was confused with the location of the raising function.

Producer behavior was initially described as if `q>0` held on all GT boxes. This was corrected after recognizing that the producer encountered the same local guard but caught it, which changed what appeared in stdout.

A repair direction was recommended, withdrawn, and then restored when direct evidence supported it.

An audit script used a fixed-line-window heuristic around calls and falsely classified the `root_localize` try structure. Direct source inspection corrected that result.

Most importantly, the first repair's scope audit was incomplete. The second production stop exposed that incompleteness and forced the audit boundary to expand from one function to all corresponding exception sites.

These corrections are indexed separately in [CORRECTIONS.md](../CORRECTIONS.md).

## 10. C1c byproduct: recovering an existing obligation

The same period produced a separate read-only audit of the sealed Phase 1 ledger for a C1c assembly obligation.

For every accepted slab, C1c requires a supply establishing the anchor condition at `t=1/2`. The audit classified accepted slabs into an A path, a B path, or missing supply.

The result was:

- accepted slabs: 159;
- A path: 0;
- B path: 159;
- missing: 0;
- final exterior stages: E0 = 120, E1 = 37, E2 = 2;
- exact lambda union: `[9/20, 5/8]`;
- adjacent exact endpoints: verified.

This establishes that the sealed Phase 1 ledger contains anchor-supply material for all 159 accepted slabs. It does **not** establish final C1c assembly, which still depends on the later cross-lineage and receipt work.

## 11. Methodological reading

This case illustrates why the final word in the sequence is **Re**, not merely “retry.”

The process included re-reading source paths, reclassifying an exception, re-comparing producer and checker, re-running controls, restarting production, and re-auditing an existing sealed ledger for a different proof obligation.

The important property was not that the AI or human participant avoided mistakes. They did not. The important property was that the workflow contained boundaries at which unsupported continuation could be stopped and evidence could force a correction.

The case therefore instantiates the repository's organizing principle:

> **Observe → Doubt → Stop → Re**  
> **見る → 疑う → 止める → 再する**

The research value of the record lies in the trace from an initial observation through incorrect hypotheses and corrections to a narrower justified state — not in presenting the final diagnosis as if it had been obvious from the beginning.
