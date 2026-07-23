import nbformat
from pathlib import Path
nbp = Path('notebooks/00_core.ipynb')
nb = nbformat.read(nbp, as_version=4)
new_src = [
"# Bootstrap import of src/shared.py (follows repo guidance)",
"import sys, pathlib, os",
"# Prefer src/ in the repo root when running from the project root; otherwise use parent/src when running from notebooks/",
"p = pathlib.Path.cwd()",
"candidate = p / 'src'",
"if not candidate.exists():\n    candidate = p.parent / 'src'",
"sys.path.insert(0, str(candidate))",
"from shared import SEED, PATHS, preprocess_text, fit_and_save_vectorizer",
"import pandas as pd",
"import numpy as np",
"import os",
"",
"print('SEED =', SEED)",
"print('splits target =', PATHS['splits_parquet'])",
"print('tfidf target =', PATHS['tfidf'])",
]
# Replace second cell
nb['cells'][1]['source'] = [s + "\n" for s in new_src]
nbformat.write(nb, nbp)
print('patched')
