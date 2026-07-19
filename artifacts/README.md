# artifacts

Fitted models and the vectorizer — binary, large, and fully regenerable, so this folder is **gitignored** (only this README is tracked). Anyone can rebuild everything here by running the pipeline from 00.

| File | What it is | Produced by |
|---|---|---|
| `tfidf_vectorizer.joblib` | The TF-IDF vectorizer, **fit on the fit split only** and reused everywhere (no leakage). | 00 |
| `logreg.joblib` | The tuned logistic-regression model. | 02 |
| `nn_model.keras` | The trained feed-forward neural network. | 03 |

These are loaded by downstream notebooks so a lane never has to retrain another lane's model. Because they are gitignored, the *reproducible* record of results lives in `outputs/` (committed), not here.
