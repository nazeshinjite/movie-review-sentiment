# Notebooks — the pipeline

The project is built as a **linear sequence of notebooks that hand off artifacts on disk.** Each notebook reads the previous step's saved outputs and writes the inputs for the next. The files on disk are the contract between people — nothing is passed in memory. Run them **in order, 00 → 05.**

Notebooks do not exist yet; they are designed and built together, one at a time. This README is the spec each one implements.

## Why it is built this way

- **Parallel work.** A downstream lane loads the saved artifacts of an upstream lane instead of rerunning its expensive steps. Three people move at once.
- **Reproducibility.** From a clean clone, running 00 → 05 regenerates every figure and number the paper reports.
- **The fairness rules become structural.** TF-IDF is fit once (in 00) and saved, so there is no leakage. The model notebooks (02, 03) only ever see the `fit` and `val` splits — **all test-set scoring lives in notebook 04**, so the plan's "single final test run, both models, one script" is enforced by the structure, not by calendar discipline.
- **Legible contribution.** Each owner's commits land in their own notebook.

## Ownership

| # | Notebook | Owner |
|---|---|---|
| 00 | `00_core.ipynb` | **Team** (built jointly at kickoff) |
| 01 | `01_eda.ipynb` | Teammate 1 |
| 02 | `02_logistic_regression.ipynb` | Teammate 1 |
| 03 | `03_neural_network.ipynb` | Teammate 2 |
| 04 | `04_evaluation.ipynb` | Teammate 2 |
| 05 | `05_divergence_judge.ipynb` | Teammate 3 |

The shared foundation (00) is team-owned on purpose: it is communal plumbing everyone depends on, so it should not sit inside one person's lane or block the others. Lanes map to the Lean workload plan (T1 = data + LR, T2 = NN + evaluation, T3 = analysis + judge + paper). See [`../docs/contributions.md`](../docs/contributions.md).

## Handoff contract

Two canonical artifacts anchor everything: **`data/processed/splits.parquet`** (`id, text, label, split∈{fit,val,test}`) and **`artifacts/tfidf_vectorizer.joblib`** (fit on the `fit` split only). Feature matrices are *derived*, never stored: every notebook calls `shared.load_features(split)`, which loads both artifacts and transforms on the fly (seconds), so matrices can never go stale against the vectorizer.

**Predictions are the interface between lanes.** Every prediction file uses one schema — **`id, y_true, y_pred, y_proba_pos`** — and joins back to review text on `id`. Anything downstream (metrics, figures, disagreements) is derived from predictions plus `splits.parquet`.

| # | Notebook | Reads | Writes |
|---|---|---|---|
| **00** | `core` | `stanfordnlp/imdb` (Hugging Face) | `data/processed/splits.parquet`<br>`artifacts/tfidf_vectorizer.joblib` |
| **01** | `eda` | `splits.parquet` | `outputs/figures/eda_*.png`<br>`outputs/tables/eda_*.csv` |
| **02** | `logistic_regression` | `load_features("fit")`, `load_features("val")` | `artifacts/logreg.joblib`<br>`outputs/predictions/lr_val.parquet`<br>`outputs/tables/lr_top_coefficients.csv`<br>`outputs/tables/lr_topk_results.csv` (k = 50/100/500) |
| **03** | `neural_network` | `load_features("fit")`, `load_features("val")` | `artifacts/nn_model.keras`<br>`outputs/predictions/nn_val.parquet`<br>`outputs/tables/nn_training_history.csv` |
| **04** | `evaluation` | val predictions; saved models; `load_features("test")` **on the final run only** | `outputs/predictions/test_predictions.parquet` (long format: adds a `model` column)<br>`outputs/tables/metrics_comparison.csv`<br>`outputs/figures/{roc,confusion,comparison}_*.png` |
| **05** | `divergence_judge` | prediction files + `splits.parquet` (for text) | `outputs/tables/adjudication.csv`<br>`outputs/tables/disagreement_taxonomy.csv`<br>`outputs/figures/judge_*.png` |

Notes:
- **`fit` vs `val` vs `test`.** `fit` (10,000) trains the models; `val` (5,000) tunes them; `test` (25,000) is scored exactly once. Notebooks 02 and 03 never load the test split — they end at a frozen model artifact plus validation predictions.
- **The single final test run is notebook 04** (Jul 29 per the plan). It loads both frozen models, transforms the test set once, scores both models in one pass, and writes one combined `test_predictions.parquet`. Before that day, 04 is developed and validated entirely against the val prediction files.
- **Disagreements are derived, not stored.** A disagreement is `y_pred_lr != y_pred_nn` — notebook 05 computes it in one merge from the prediction files (val predictions for week-1 judge development, `test_predictions.parquet` after the final run) and rehydrates review text from `splits.parquet`.

## Import convention

Each notebook imports the shared foundation from `src/shared.py` with a short path bootstrap in the first code cell:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent / "src"))
from shared import SEED, PATHS, load_features, compute_metrics   # etc.
```

No package install — it works on any machine after `uv sync`.

## Standard notebook layout

Every notebook opens with: a **title + purpose** markdown cell, the **owner**, and its **reads/writes** line from the table above. Then imports (shared foundation first), then the work, then an explicit **"write handoff artifacts"** cell at the end. Notebooks must run clean top-to-bottom (Kernel → Restart & Run All) with `SEED` set.
