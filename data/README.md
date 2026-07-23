# data

Datasets and derived data artifacts. `data/raw/` and `data/processed/` are **gitignored** — large and fully regenerable from notebook 00. `data/golden/` is **committed** — hand-curated files cannot be regenerated, which is exactly why they are tracked. Record source, license, and access date below for every dataset.

## Layout

| Path | Contents | Produced by |
|---|---|---|
| `raw/` | The dataset as downloaded (Hugging Face cache / exported copy). Never edited by hand. Gitignored. | 00 (download) |
| `processed/splits.parquet` | Canonical split table: `id, text, label, split∈{fit,val,test}`. The join source for all downstream text and labels. Gitignored. | 00 |
| `golden/golden_set.csv` | Hand-curated 32-review calibration set for the LLM judge (train-split sourced, stratified by difficulty category). Committed. | T3, by hand |
| `golden/pilot-tags-golden.csv` | Blinded tagging sheet for the tagging-protocol pilot (`docs/tagging-protocol.md`). Committed. | T3, by hand |

Feature matrices are **not stored** — every notebook derives them on the fly from `splits.parquet` + the fitted vectorizer via `shared.load_features(split)`, so they can never go stale.

## Dataset provenance

**Stanford Large Movie Review Dataset (IMDB)**

- Source: Hugging Face — `stanfordnlp/imdb` (https://huggingface.co/datasets/stanfordnlp/imdb)
- Origin: Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). *Learning word vectors for sentiment analysis.* ACL.
- Size: 50,000 labeled reviews (25,000 train / 25,000 test), balanced 50/50.
- License: see the dataset card — `[VERIFY]` and record the exact license + access date here before submission.
- Access date: `[record on first download]`

## Data budget

Split sizes, seed, and the test-set policy are recorded once, in [`../docs/decisions.md`](../docs/decisions.md).
