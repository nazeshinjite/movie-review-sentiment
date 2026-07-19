# Contribution log

The source for the paper's required **per-member contribution appendix** and a reference for the 7.3 peer evaluations. Update it as work lands — do not reconstruct it at the end.

## Lane assignments

| Member | Lane | Notebooks | Report sections | Presentation |
|---|---|---|---|---|
| Keana Gindlesperger | *(assign at kickoff)* | | | |
| Yesid Cardenas Marin | *(assign at kickoff)* | | | |
| Ian Schmitt | *(assign at kickoff)* | | | |

Lanes to slot names into (full detail, calendar, and rationale in [`workload-plan.md`](workload-plan.md)):

- **T1 — Foundation + Neural Network:** notebooks 00 (core + `shared.py`, early) and 03 (NN, late); report intro & related work, data & preprocessing, Methods: NN; shared duty: README/PEP-8 pass + clean-clone reproducibility run.
- **T2 — Logistic Regression + Evaluation:** notebooks 02 (LR + top-k, early) and 04 (evaluation + the single final test run, late); report Methods: LR and Evaluation + Results; shared duties: slide deck, records + uploads the video.
- **T3 — EDA + Divergence/Judge:** notebooks 01 (EDA, early) and 05 (divergence + judge, late); report EDA, divergence + judge, discussion/limitations/conclusion; shared duties: paper integration, citation audit, contribution appendix, submits 7.2.

## On the 2/2/2 split

Every member owns exactly two notebooks — one **early-phase** (00/01/02) and one **late-phase** (03/04/05) — so contribution is continuous across the whole build rather than front- or back-loaded. Prose loads differ slightly (≈3.75 / 2.75 / 3.5 pp) and are offset by shared duties: T2 carries the deck and video, T3 carries integration and submission, T1 carries the reproducibility pass. This log is where non-code contribution becomes visible, so the appendix and peer evaluations reflect the whole picture and not just commit counts. Log prose, review, and video work here, not only code.

## Running log

| Date | Member | Contribution |
|---|---|---|
| 2026-07-19 | Ian Schmitt | Scaffolded the repository: structure, environment config (uv + lockfile), all READMEs, and the docs set (workload plan, shared-foundation decisions, contribution and AI-use logs). |
