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

Pull-request workflow: **`main` is branch-protected — nothing lands without a PR approved by at least one other team member.** Notebooks merge badly, so the conflict defense stays structural: one notebook one owner, short-lived branches.

- **Branch, then PR.** Start from a fresh `main` (`git pull`), branch as `<name>/<topic>` (e.g. `ian/03-neural-network`), push, and open a PR (`gh pr create` or the web UI). Fill in the PR template's checklist.
- **Review assignment.** Default reviewer is your round-robin partner — Yesid reviews Keana's PRs, Keana reviews Ian's, Ian reviews Yesid's; if they're unavailable, anyone else approves. Review = pull the branch, run the notebook clean, sanity-check claims against outputs — not a rubber stamp.
- **One approval merges.** Squash-merge (keeps `main` linear, one commit per PR — the PR itself preserves the detail), then delete the branch. Keep branches alive days, not weeks: long-lived notebook branches are how merge hell starts.
- **Before requesting review:** Restart & Run All so outputs match code; run the bundled reviewer agent — open Claude Code at the repo root and ask it to *"use the notebook-reviewer agent on notebooks/0X_*.ipynb"* — and clear its Blockers; confirm no API key sits in any cell or output. Not a Claude Code user? `.claude/agents/notebook-reviewer.md` reads as a plain checklist — walk it manually.
- **One notebook, one owner.** Never edit someone else's notebook — if you need a change in it, ask the owner (that is what the two weekly syncs and the group chat are for). This is what makes conflicts nearly impossible.
- Shared files (`src/shared.py`, `docs/*`) change only after a team decision — log it in `docs/decisions.md`; the PR approving the change is the paper trail.
- **Emergency hatch:** the repo admin can push to `main` directly (protection exempts admins). Deadline emergencies only — announce it in the group chat when it happens.

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
