# src — shared foundation

One small module, **`shared.py`**, holding the plumbing every lane must agree on so the two-model comparison is fair and the paper's numbers regenerate identically. It is deliberately *not* a package — notebooks import it via a short path bootstrap (no install step). It is built alongside notebook 00 — T1's early-phase deliverable and the first thing in the pipeline — with the shared constants reviewed by the whole team.

Planned contents (values and rationale live in [`../docs/decisions.md`](../docs/decisions.md) — not duplicated here):

- **Constants:** `SEED`, `PATHS` (so no notebook hard-codes a path), the agreed preprocessing/split/top-k parameters.
- **`load_features(split)`** — loads `splits.parquet` + the fitted vectorizer and returns `X, y` for `"fit"`, `"val"`, or `"test"`. Matrices are derived on the fly (seconds), never stored, so they can't go stale against the vectorizer.
- **`compute_metrics(y_true, y_pred, y_proba)`** — accuracy, precision, recall, F1, ROC-AUC, confusion matrix. The **one** metrics function every lane calls, so results are computed identically.
- **A small matplotlib style dict** (`rcParams`) so figures across notebooks look consistent. Plot *functions* stay in the notebooks that draw them — each figure is produced in exactly one place.

Model-specific and analysis code stays in the notebooks — that is the graded work each owner writes and defends. `shared.py` holds only the settled, communal pieces.

## Import convention

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent / "src"))
from shared import SEED, PATHS, load_features, compute_metrics
```

Any change to a shared constant (a seed, a preprocessing setting) is a team decision — record it in [`../docs/decisions.md`](../docs/decisions.md), because changing it invalidates saved artifacts and forces a rerun from 00.
