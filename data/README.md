# data

Datasets and derived data artifacts. **Gitignored** (`data/raw/` and `data/processed/`) — large and fully regenerable from notebook 00. Only this README and `.gitkeep` files are tracked. Record source, license, and access date below for every dataset.

## Layout

| Path | Contents | Produced by |
|---|---|---|
| `raw/` | The dataset as downloaded (Hugging Face cache / exported copy). Never edited by hand. | 00 (download) |
| `processed/splits.parquet` | Canonical split table: `id, text, label, split∈{fit,val,test}`. The join source for all downstream text. | 00 |
| `processed/tfidf_{fit,val,test}.npz` | Sparse TF-IDF feature matrices (SciPy `.npz`). | 00 |
| `processed/labels_{fit,val,test}.npy` | Label vectors aligned to the matrices. | 00 |

## Dataset provenance

**Stanford Large Movie Review Dataset (IMDB)**

- Source: Hugging Face — `stanfordnlp/imdb` (https://huggingface.co/datasets/stanfordnlp/imdb)
- Origin: Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). *Learning word vectors for sentiment analysis.* ACL.
- Size: 50,000 labeled reviews (25,000 train / 25,000 test), balanced 50/50.
- License: see the dataset card — `[VERIFY]` and record the exact license + access date here before submission.
- Access date: `[record on first download]`

## Data budget (from the workload plan)

Model fitting uses a stratified, seeded subsample of the 25,000-review training pool: **10,000 fit + 5,000 validation.** The **full 25,000-review test set** is held out and scored exactly once, on the final run. EDA may describe the full corpus.
