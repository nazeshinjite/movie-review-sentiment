# Notebooks — the pipeline

The project is built as a **linear sequence of notebooks that hand off artifacts on disk.** Each notebook reads the previous step's saved outputs and writes the inputs for the next. The files on disk are the contract between people — nothing is passed in memory. Run them **in order, 00 → 05.**

Notebooks do not exist yet; they are designed and built together, one at a time. This README is the spec each one implements.

## Why it is built this way

- **Parallel work.** A downstream lane loads the saved artifacts of an upstream lane instead of rerunning its expensive steps. Three people move at once.
- **Reproducibility.** From a clean clone, running 00 → 05 regenerates every figure and number the paper reports.
- **The fairness rules become structural.** TF-IDF is fit once (in 00) and saved, so there is no leakage; the test set lives in its own artifact and is read only on the final run, so it is touched exactly once.
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

Stable join key: every row keeps its **`id`** (the review's index in `splits.parquet`), so any notebook can rehydrate review text. Every prediction file shares one schema: **`id, y_true, y_pred, y_proba_pos`** — which makes evaluation model-agnostic.

| # | Notebook | Reads | Writes |
|---|---|---|---|
| **00** | `core` | `stanfordnlp/imdb` (Hugging Face) | `data/processed/splits.parquet` (`id, text, label, split∈{fit,val,test}`)<br>`artifacts/tfidf_vectorizer.joblib`<br>`data/processed/tfidf_{fit,val,test}.npz`<br>`data/processed/labels_{fit,val,test}.npy` |
| **01** | `eda` | `splits.parquet` | `outputs/figures/eda_*.png`<br>`outputs/tables/eda_*.csv` |
| **02** | `logistic_regression` | `tfidf_{fit,val}.npz` + labels | `outputs/predictions/lr_{val,test}.parquet`<br>`artifacts/logreg.joblib`<br>`outputs/tables/lr_top_coefficients.csv`<br>`outputs/tables/lr_topk_results.csv` (k = 50/100/500) |
| **03** | `neural_network` | `tfidf_{fit,val}.npz` + labels | `outputs/predictions/nn_{val,test}.parquet`<br>`artifacts/nn_model.keras`<br>`outputs/tables/nn_training_history.csv` |
| **04** | `evaluation` | `outputs/predictions/{lr,nn}_*.parquet` | `outputs/tables/metrics_comparison.csv`<br>`outputs/figures/{roc,confusion,comparison}_*.png`<br>`outputs/predictions/disagreements_{val,test}.parquet` |
| **05** | `divergence_judge` | `disagreements_*.parquet` + `splits.parquet` (for text) | `outputs/tables/adjudication.csv`<br>`outputs/tables/disagreement_taxonomy.csv`<br>`outputs/figures/judge_*.png` |

Notes:
- **`fit` vs `val` vs `test`.** `fit` (10,000) trains the models; `val` (5,000) tunes them; `test` (25,000) is scored once on the final run. 00 produces all three; the model notebooks predict on `val` during development and add `test` only on the single final run (Jul 29 per the plan).
- **Disagreement set (04 → 05).** A review is a disagreement when LR and NN predict different labels. 04 exports those `id`s (with each model's label and probability); 05 rehydrates the text from `splits.parquet`, tags the hard-case type, and runs the LLM judge.

## Import convention

Each notebook imports the shared foundation from `src/shared.py` with a short path bootstrap in the first code cell:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent / "src"))
from shared import SEED, PATHS, compute_metrics   # etc.
```

No package install — it works on any machine after `uv sync`.

## Standard notebook layout

Every notebook opens with: a **title + purpose** markdown cell, the **owner**, and its **reads/writes** line from the table above. Then imports (shared foundation first), then the work, then an explicit **"write handoff artifacts"** cell at the end. Notebooks must run clean top-to-bottom (Kernel → Restart & Run All) with `SEED` set.
