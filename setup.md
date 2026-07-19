# Setup

Environment and run instructions for the movie-review-sentiment repo. Target: any teammate can go from a clean clone to a running pipeline.

## Prerequisites

- **Python 3.12**
- **[uv](https://docs.astral.sh/uv/)** for environment and dependency management. Install:
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- **git**

We use uv exclusively. Do not `pip install` into a global or system Python; do not create a separate conda env.

## First-time setup

```bash
git clone <repo-url>
cd movie-review-sentiment
uv sync            # creates .venv and installs the pinned dependencies from uv.lock
```

`uv sync` reads `pyproject.toml` + `uv.lock` and builds an identical `.venv` on every machine.

### Select the kernel

The Jupyter kernel is this project's `.venv`. In VS Code, pick the interpreter at `.venv/bin/python` (Windows: `.venv\Scripts\python.exe`). If you launch Jupyter directly:

```bash
uv run jupyter lab
```

## Dependencies are added as we build

The initial environment is deliberately lean. Two heavier dependencies are added with `uv add` when the notebook that needs them is built, so everyone re-runs `uv sync` and picks them up:

```bash
uv add tensorflow      # notebook 03 (feed-forward neural network, Keras)
uv add openai          # notebook 05 (OpenAI-compatible LLM-as-judge client)
```

After anyone adds a dependency and commits the updated `pyproject.toml` + `uv.lock`, pull and run `uv sync` to stay in sync.

> **TensorFlow platform note.** On Apple Silicon, `tensorflow` runs on CPU/Metal out of the box; on other platforms the standard `tensorflow` wheel is fine. If a machine cannot install TensorFlow, scikit-learn's `MLPClassifier` is a documented fallback for the feed-forward network — note the substitution in `docs/decisions.md` and the paper's Methods section.

## LLM-as-judge configuration (notebook 05)

The judge uses an **OpenAI-compatible** client, so the same code points at a local server or a cloud endpoint. Copy the template and fill in values:

```bash
cp .env.example .env
```

`.env` is gitignored — never commit a real key. Share a cloud key with the judge owner through a private channel, not GitHub. See `.env.example` for local (llama.cpp / LM Studio / Ollama) and cloud (OpenAI) examples.

## How we collaborate in git

Simple rules sized for a 3-person, 7-week project — notebooks merge badly, so we avoid merges instead of resolving them:

- **Commit straight to `main`.** No branches or PRs; the review step is the round-robin lane review, not GitHub ceremony.
- **`git pull` before every work session and before every push.**
- **One notebook, one owner.** Never edit someone else's notebook — if you need a change in it, ask the owner (that is what the two weekly syncs and the group chat are for). This is what makes conflicts nearly impossible.
- **Restart & Run All before committing a notebook**, so committed outputs match the committed code.
- Shared files (`src/shared.py`, `docs/*`) change only after a team decision — log it in `docs/decisions.md`.

## Running the pipeline

Run the notebooks **in order**:

```
00_core → 01_eda → 02_logistic_regression → 03_neural_network → 04_evaluation → 05_divergence_judge
```

Each notebook reads the previous step's saved artifacts and writes its own. Notebook 00 downloads the dataset from Hugging Face on first run (cached afterward). From a clean clone, running 00 → 05 regenerates every figure and number the paper reports.

## Code style

PEP 8 is a graded requirement. Lint before committing:

```bash
uv run ruff check .
uv run ruff format .
```

## Notebook hygiene (reproducibility)

- Imports at the top; seeds set (`SEED` from `src/shared.py`).
- Notebooks must run clean top-to-bottom (Kernel → Restart & Run All).
- Relative paths only (via the path constants in `src/shared.py`) — never hard-code an absolute path.
- Clear noisy outputs before committing; keep figures that the paper references.
- Notebooks 02 and 03 never load the test split. All test-set scoring happens once, in notebook 04, on the final run.
