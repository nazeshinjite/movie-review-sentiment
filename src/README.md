# src — shared foundation

One small module, **`shared.py`**, holding the plumbing every lane must agree on so the two-model comparison is fair and the paper's numbers regenerate identically. It is deliberately *not* a package — notebooks import it via a short path bootstrap (no install step).

`shared.py` is built with notebook 00 at kickoff. Planned contents:

| Item | Purpose |
|---|---|
| `SEED = 42` | The single random seed every split, model, and shuffle uses. |
| `PATHS` | Path constants for `data/`, `artifacts/`, `outputs/` so no notebook hard-codes an absolute path. |
| Preprocessing params | `strip <br />`, lowercase, keep stop words, ngram `(1, 2)`, `min_df=2`, `max_features≈20000` — the agreed TF-IDF settings. |
| Split sizes | 10,000 fit / 5,000 validation / 25,000 test. |
| `TOPK = [50, 100, 500]` | The grid for the "does a simple top-k model rival the full model" experiment. |
| `compute_metrics(y_true, y_pred, y_proba)` | Returns accuracy, precision, recall, F1, ROC-AUC, and the confusion matrix — the **one** metrics function both model lanes and evaluation call, so results are computed identically. |
| Plot helpers | Shared ROC, confusion-matrix, and comparison-bar functions so every figure has a consistent style and regenerates from the harness. |

Model-specific and analysis code stays in the notebooks — that is the graded work each owner writes and defends. `shared.py` holds only the settled, communal pieces.

## Import convention

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent / "src"))
from shared import SEED, PATHS, compute_metrics
```

Any change to a shared constant (a seed, a preprocessing setting) is a team decision — record it in [`../docs/decisions.md`](../docs/decisions.md), because changing it invalidates saved artifacts and forces a rerun from 00.
