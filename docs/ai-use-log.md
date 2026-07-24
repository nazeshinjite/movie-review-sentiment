# AI-use disclosure log

AAI-501 permits generative-AI use **with disclosure.** This log records what AI tools did, so the paper's disclosure statement and APA citation are accurate. Log every non-trivial use: code generation, drafting, debugging, analysis. The LLM-as-judge (notebook 05) is a *method*, not an authoring aid — describe it in Methods; still note here which model/endpoint adjudicated.

## How to log

One row per use: date, member, tool + model, what it did, and how the output was verified (the master's-level bar is that a human understands and can defend every result).

| Date | Member | Tool / model | What it did | Verification |
|---|---|---|---|---|
| 2026-07-19 | Ian Schmitt | Claude Code (Claude Opus 4.8) | Scaffolded the repository structure, READMEs, and environment config (this framing step). No analysis or model code generated. | Structure reviewed and approved by the repo owner before commit. |
| 2026-07-23 | Ian Schmitt | Claude Code | Assisted in building notebook 01 (EDA): cell scaffolding, matplotlib plotting code, and the smoothed log-ratio distinctiveness statistic, from an analysis plan I wrote. Interpretation and the takeaways are mine. | Notebook re-executed from a clean kernel; every numeric claim in the takeaways recomputed against `splits.parquet` independently of the notebook before commit. |
| 2026-07-24 | Ian Schmitt | Claude Code (Claude Opus 5) | Reviewed teammate PR #1 (00_core + shared.py) by executing it rather than reading the diff, which surfaced a split-construction defect; after the fix, re-verified the artifacts and approved. Then ran the bundled `notebook-reviewer` agent over notebook 01 pre-PR. | Split correctness confirmed by rebuilding it independently from the same seed and comparing row by row. Every reviewer finding re-derived by hand before acting: the flagged markup claim was an overlap fallacy, and recomputing the disjoint count gave 2 regex false positives and 0 real HTML tags. Corrections applied and the notebook re-executed. |

## For the paper

The disclosure statement summarizes this log. Cite each AI tool in APA 7 (e.g., the LLM-judge model and any drafting/coding assistant). Keep model names and versions accurate — `[VERIFY]` anything uncertain before submission.
