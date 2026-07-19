# Shared-foundation decisions

The settings every lane must agree on. These live in code in `src/shared.py`; this file is the human record of *what* and *why*. **Changing any of these invalidates the saved artifacts and forces a rerun from notebook 00** — so a change is a team decision, logged here with a date.

## Authoritative plan

`Lean-Workload-Plan.docx` is the single source of truth. The `Kimi Lean Workload Plan.docx` is **deprecated** and not used.

## Decisions

| Decision | Value | Rationale |
|---|---|---|
| Random seed | `SEED = 42` | One seed for every split, shuffle, and model, so runs are reproducible and the comparison is fair. |
| Split sizes | 10,000 fit / 5,000 validation / 25,000 test | Lean-plan data budget. Fit + validation are a stratified, seeded subsample of the 25k training pool; the full test set is held out. |
| Test-set policy | Touched **exactly once**, on the final run | No peeking — otherwise the reported test performance is optimistic. |
| Vectorizer | TF-IDF, **fit on the fit split only**, saved and reused | Fitting on all 50k would leak test information into the vocabulary and IDF weights. |
| Preprocessing | strip `<br />`, lowercase, keep stop words, ngram `(1, 2)`, `min_df=2`, `max_features ≈ 20000` | Keep stop words because standard lists delete "not," which flips sentiment. `max_features` also caps the network's input width. |
| Top-k grid | `k = 50, 100, 500` | The "does a simple model on a few key features rival the full model" experiment the rubric rewards. |
| Metrics | accuracy, precision, recall, F1, ROC-AUC, confusion matrix | One `compute_metrics()` both lanes call, so numbers are computed identically. |
| Prediction schema | `id, y_true, y_pred, y_proba_pos` | Shared across LR and NN so evaluation is model-agnostic and joins to review text on `id`. |
| Tuning budgets | ≤ 6 LR configs (CV) and ≤ 6 NN configs (fixed validation split) | Comparable, documented budgets — the bar is fairness, not exhaustive search. |
| LLM-judge scope | Adjudicator on the disagreement set only | No explanation pipeline, no third headline model, no per-title aggregation. |
| NN framework | TensorFlow / Keras (fallback: sklearn `MLPClassifier`) | Keras is the clear deep-learning signal; the fallback is documented for machines that cannot install TF. |

## Change log

| Date | Change | Who | Rerun required from |
|---|---|---|---|
| 2026-07-19 | Initial decisions recorded from the Lean plan. | Team | — (baseline) |
