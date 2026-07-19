# outputs

Committed results — the paper deliverables and the small cross-lane handoff files. Unlike `data/` and `artifacts/`, this folder **is tracked in git**, so teammates can review each other's results and the paper can cite them without rerunning the pipeline.

| Subfolder | Contents | Committed? |
|---|---|---|
| `figures/` | Paper figures: EDA plots, ROC curves, confusion matrices, the head-to-head comparison, judge figures. | Yes |
| `tables/` | Metrics comparison, LR top coefficients, top-k results, NN training history, adjudication + taxonomy tables. | Yes |
| `predictions/` | Per-model prediction files (`lr_*`, `nn_*`) and the disagreement sets — the handoff between the model lanes and evaluation/analysis. Small parquet. | Yes |

## Why predictions are committed

Committing the small prediction files is what lets the lanes work in parallel: the evaluation lane (04) and the analysis lane (05) read saved predictions instead of retraining the models. The full pipeline still regenerates them from a clean clone; the committed copies are a convenience and a provenance record.

## Prediction schema

Every `*_{val,test}.parquet` here uses the same columns:

| Column | Meaning |
|---|---|
| `id` | Review index, joins to `data/processed/splits.parquet`. |
| `y_true` | Gold label (0 = negative, 1 = positive). |
| `y_pred` | Predicted label. |
| `y_proba_pos` | Predicted probability of the positive class. |

Because the schema is shared, the evaluation harness treats LR and NN identically.
