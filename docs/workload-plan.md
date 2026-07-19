# Workload plan

The authoritative plan for lanes, calendar, and the report/presentation split. Supersedes the pre-repo `Lean-Workload-Plan.docx` (kept outside the repo). Shared-foundation values live in [`decisions.md`](decisions.md); the scope fence is in the [root README](../README.md#scope-fence-explicitly-not-doing). Plan date: July 19, 2026. Everything is recorded and submitted by **Thu Aug 6** (one teammate is away Aug 7–10; no extensions exist).

## Lanes — 2/2/2, phased early + late

Each member owns exactly two notebooks: **one early-phase deliverable** (00/01/02, week 1) and **one late-phase deliverable** (03/04/05, weeks 2–3). The point of the pairing: contribution stays continuous and visible across the whole build — nobody's work is front-loaded or back-loaded, which is what the rubric's sustained-contribution emphasis (and the peer evaluations) actually measure.

| Lane | Notebooks (early → late) | Report sections (≈10 pp total) | Presentation + shared duties |
|---|---|---|---|
| **T1 — Foundation + Neural Network** | `00_core` (+ `src/shared.py`) → `03_neural_network` | Introduction & related work; Data & preprocessing; Methods: NN (≈3.75 pp) | Opening, data/preprocessing, NN; README/PEP-8 pass + clean-clone reproducibility run |
| **T2 — Logistic Regression + Evaluation** | `02_logistic_regression` (incl. top-k) → `04_evaluation` (incl. the single final test run) | Methods: LR; Evaluation design + Results (≈2.75 pp) | LR, head-to-head results, recommendation & close; designs the shared slide template + assembles the final deck; records + uploads the video; final comparison table |
| **T3 — EDA + Divergence/Judge** | `01_eda` → `05_divergence_judge` | EDA; Divergence + LLM judge; Discussion, limitations & conclusion (≈3.5 pp) | EDA, divergence, judge, limitations; paper integration, citation audit, contribution appendix; submits 7.2 |

Prose loads are intentionally uneven (3.75 / 2.75 / 3.5 pp): T2 carries the deck, recording logistics, and video upload; T3 carries integration and submission; T1 carries the reproducibility/PEP-8 pass. Technical hours are roughly equal (~9–10 h each). Names slot into lanes at kickoff — recorded in [`contributions.md`](contributions.md).

**Content boundary (T1 ↔ T3):** T1's *Data & preprocessing* covers what we **did to** the data — data budget, splits, vectorizer, preprocessing choices and their rationale. T3's *EDA* covers what the data **looks like** — distributions, balance, artifacts, top n-grams. The two are adjacent in both paper and talk; describe the corpus once (edge cases settled at kickoff).

**Slides:** T2 designs the shared PPTX template (masters, title slide, styles) and commits it by **Wed Jul 29**; each member builds their **own slides** for their segments in that template; T2 assembles the final deck and manages the recording.

**On notebook 00:** it is everyone's dependency, so it is deliberately tiny (two artifacts: splits + fitted vectorizer), it lands **first** on the calendar, and its shared constants are a team decision — reviewed by all three and recorded in `decisions.md`, not chosen unilaterally.

## Required EDA (lean — feeds T3's report section and slides)

| EDA item | What to include | Why it matters |
|---|---|---|
| Corpus shape & balance | Counts per split and class (known 50/50). | Establishes scope; justifies accuracy as a usable headline metric. |
| Review length | Distribution of tokens per review by class. | Motivates the vocabulary cap. |
| HTML artifacts | Check for `<br />` tags and other markup noise. | Untreated, "br" becomes a top feature — the annotation-artifact problem. |
| Top n-grams by class | Most frequent unigrams/bigrams per class. | Previews the sentiment lexicon the models should recover. |

## Calendar (dated; team-wide milestones in bold)

> **Phasing is deliberate:** week 1 delivers every member's early-phase notebook (T1: 00, T3: 01, T2: 02); weeks 2–3 deliver every member's late-phase notebook (T1: 03, T2: 04 with the final test run, T3: 05). Each person ships in both halves of the build.

| Dates | Work |
|---|---|
| **Sun Jul 19 – Mon Jul 20** | **Kickoff** (30-min Zoom): confirm this plan, slot names into lanes. Repo is live; everyone: `uv sync` works, dataset loads. Plan author drafts the **4.3 Status Update**; one member submits after team review — **due Mon Jul 20, 11:59 pm PT**. |
| Tue Jul 21 – Sun Jul 26 | **Early-phase deliverables.** T1: `00_core` + `shared.py` done by **Wed Jul 22** (everyone's dependency — first priority), then starts 03. T3: `01_eda` done by Sun Jul 26; paper scaffold from template; judge prompt/script drafted and smoke-tested on hand-picked val reviews (the disagreement *filter* needs both models, but prompt development doesn't). T2: `02_logistic_regression` done by Sun Jul 26 (tuned, ≤6 configs, val predictions committed). Sync Wed Jul 22 evening + weekend checkpoint. |
| Mon Jul 27 – Wed Jul 29 | **Late-phase spin-up.** T1: `03_neural_network` done by Tue Jul 28 (tuned, ≤6 configs, val predictions committed). T2: builds `04_evaluation` against the val prediction files. T3: runs the judge on **val** disagreements (available once both val prediction files land), finishes the tagging protocol. T2: commits the shared slide template by **Wed Jul 29**. **Wed Jul 29: SINGLE FINAL TEST RUN** — T2 runs 04 once; `test_predictions.parquet` committed the same day. |
| **Thu Jul 30** | **RESULTS FREEZE.** All figures/tables regenerated. T3 runs the adjudicator on test disagreements and completes tagging (execution, not development). No new experiments after today — late ideas go to Discussion as future work. |
| Fri Jul 31 | Each member builds their own slides in T2's template; T2 assembles the final deck. Evening: full dry run on Zoom with a visible timer — the 20-min floor and 30-min ceiling are both graded. |
| **Sat Aug 1** (backup Sun Aug 2) | **RECORD** the 20–30 min presentation: one continuous Zoom recording, presenters switch live. T2 uploads the video; the link goes on the slide title page. |
| Mon Aug 3 – Wed Aug 5 | Mon: all report sections final. Tue: round-robin reviews (T1 → T2's lane, T2 → T3's, T3 → T1's): run the notebooks clean, sanity-check claims against outputs — the `notebook-reviewer` agent (`.claude/agents/`) automates the first pass. Wed: T3 integrates — citation audit, contribution appendix, AI-use disclosure; T1 runs the clean-clone reproducibility check + README/PEP-8 pass. |
| **Thu Aug 6** | **SUBMIT 7.2** (paper + slides with video link + repo link) — T3 submits, before the traveling teammate departs. All three submit **7.3 peer evaluations** (early if Canvas allows; otherwise from a phone by Aug 10). |
| Aug 7 – Mon Aug 10 | **Buffer only.** The two teammates in town are on call for Canvas issues. Nothing is scheduled here by design. Mon Aug 10: hard deadline, no extensions. |

## Presentation script (target ≈24 min; equal portions; order mirrors the report)

| Time | Presenter / segment | Focus |
|---|---|---|
| 0:00–1:30 | T1: Opening | Problem, recommender framing, roadmap |
| 1:30–5:00 | T1: Data & preprocessing | Corpus, data budget, splits, TF-IDF foundation |
| 5:00–7:30 | T3: EDA | Balance, review lengths, artifacts, top n-grams |
| 7:30–10:30 | T2: Logistic regression | Theory, tuning, top coefficients, top-k finding |
| 10:30–13:30 | T1: Neural network | Architecture, tuning, early stopping, what non-linearity buys |
| 13:30–16:30 | T2: Head-to-head results | Metrics table, ROC, confusion matrices; who wins where |
| 16:30–19:00 | T3: Divergence analysis | Hard-case taxonomy with real review examples |
| 19:00–21:00 | T3: LLM-as-judge | Setup, adjudication results, what the LLM resolves |
| 21:00–22:30 | T3: Limitations & future work | Domain generalization, coefficient caveats, what we won't claim |
| 22:30–24:30 | T2: Recommendation & close | Model choice for the use case; contributions slide; takeaway |

Per-member time: T1 ≈ 8 min, T2 ≈ 8 min, T3 ≈ 8.5 min (total ≈ 24.5). **Every segment is written and presented by the same member** — the trade is a three-segment T3 block (16:30–22:30) near the end. Recording: one continuous Zoom take; T2 shares the deck; presenters unmute and switch live.

## Success criteria

- Code runs end-to-end from a clean clone; every figure and number in the paper regenerates from the pipeline.
- Both models tuned under documented, comparable budgets; test set touched exactly once (notebook 04).
- The divergence analysis and adjudication table turn the comparison into findings, not just scores.
- Each member has a visibly equal contribution across code, report, and video — one early and one late deliverable each, made accountable by the contribution appendix, Turnitin, and the 7.3 peer evaluations.
- Everything submitted **Thu Aug 6** — four days of buffer against a no-extensions deadline.
