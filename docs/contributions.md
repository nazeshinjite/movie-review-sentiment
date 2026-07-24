# Contribution log

The source for the paper's required **per-member contribution appendix** and a reference for the 7.3 peer evaluations. Update it as work lands — do not reconstruct it at the end.

## Lane assignments (Jul 19 kickoff; corrected Jul 20)

| Member | Lane | Notebooks | Report sections | Presentation + shared duties |
|---|---|---|---|---|
| **Keana Gindlesperger** | T1 — Foundation + Neural Network | 00 (core + `shared.py`, early), 03 (NN, late) | Data & preprocessing; Methods: NN | Data/preprocessing, NN; **slide template + final deck assembly + recording logistics; final video edit + upload; drafts + submits 4.3 (Jul 20); submits 7.2 (Aug 6)** |
| **Yesid Cardenas Marin** | T2 — Logistic Regression + Evaluation | 02 (LR + top-k, early), 04 (evaluation + final test run, late) | Intro & related work; Methods: LR; Evaluation design + Results | Opening, LR, head-to-head results, close; README/PEP-8 pass + clean-clone reproducibility run; final comparison table |
| **Ian Schmitt** | T3 — EDA + Divergence/Judge | 01 (EDA, early), 05 (divergence + judge, late) | EDA; Divergence + LLM judge; Discussion, limitations & conclusion | EDA, divergence, judge, limitations; paper integration, citation audit, contribution appendix |

Full rationale, calendar, and the presentation script: [`workload-plan.md`](workload-plan.md).

## On the 2/2/2 split

Every member owns exactly two notebooks — one **early-phase** (00/01/02) and one **late-phase** (03/04/05) — so contribution is continuous across the whole build rather than front- or back-loaded. Prose loads differ (≈2.25 / 4.25 / 3.5 pp) and are offset by shared duties: T1 (Keana) carries the full deck/video pipeline and both Canvas submissions, T2 (Yesid) carries the reproducibility/PEP-8 pass, T3 (Ian) carries paper integration. This log is where non-code contribution becomes visible, so the appendix and peer evaluations reflect the whole picture and not just commit counts. Log prose, review, and video work here, not only code.

## Running log

| Date | Member | Contribution |
|---|---|---|
| 2026-07-19 | Ian Schmitt | Scaffolded the repository: structure, environment config (uv + lockfile), all READMEs, and the docs set (workload plan, shared-foundation decisions, contribution and AI-use logs). |
| 2026-07-19 | All | Kickoff meeting: workload plan confirmed, lanes assigned (T1 Yesid, T2 Keana, T3 Ian), PR + one-approval git workflow adopted, 4.3 submission assigned to Keana. |
| 2026-07-20 | All | Lane correction: Keana and Yesid swapped lanes — T1 Keana (core + NN), T2 Yesid (LR + evaluation). Keana keeps the full deck/video pipeline (template, assembly, recording, edit, upload) and both Canvas submissions (drafts + submits 4.3); Yesid takes Intro & related work, the video opening, and the reproducibility/PEP-8 pass. PR reviewers unchanged: Yesid → Keana's, Keana → Ian's, Ian → Yesid's. |
| 2026-07-20 – 07-23 | Ian Schmitt | Judge lane groundwork ahead of notebook 05: hand-curated 32-review golden set, judge prompt development and freeze (three candidate prompts, evaluated head-to-head), the disagreement tagging protocol (v1.1, piloted and adjudicated), and the running development log in `judge-dev-log.md`. |
| 2026-07-23 | Ian Schmitt | Built notebook 01 (EDA): corpus balance, review-length distributions by class, the `<br />` markup-artifact demonstration, frequent and class-distinctive n-grams, and data-quality checks. Four figures and four tables, all fit-split only. |
| 2026-07-23 | Ian Schmitt | Scaffolded notebook 05: frozen judge configuration, checkpointed adjudication runner, and the golden-set evaluation that selected the configuration. |
| 2026-07-24 | Ian Schmitt | Reviewed PR #1 (Keana's `00_core` + `shared.py`) by executing it rather than reading the diff, which caught a split-construction defect that would have put ~50% unlabeled rows into every split. Re-verified after her fix, approved, and merged. Rebased and re-ran 01 against the real artifacts, then corrected two markup claims that the pre-PR review showed were unsupported. |
