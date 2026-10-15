# AI Engineering Project Curriculum

Six project tracks turn 200 AI engineering competencies into 24 practical learning units. Original baselines use fictional robot telemetry, SDK documents, and simulated reservations. Instruction is mainly Chinese; code and portfolio templates support English technical communication.

**Start:** [START_HERE](START_HERE.md) · [Syllabus](curriculum/SYLLABUS.md) · [200-point map](curriculum/KNOWLEDGE_MAP.md) · [Sources](SOURCES.md) · [Validation](reports/VALIDATION.md)

| Track | What is supplied now | What the learner builds next |
|---|---|---|
| P01 Telemetry experiments | CPU classification, group split, baseline, validation selection, uncertainty | Additional models, real-data validation and research report |
| P02 SDK evidence search | BM25/overlap comparison, labels, tenant and expiry filtering | Embeddings, model-backed answers and independent holdout |
| P03 Durable tool workflow | SQLite transactions, approvals, idempotency and recovery tests | Authenticated planner integration, tracing and external-effect design |
| P04 AI service architecture | Local HTTP adapter, contract tests and local benchmark | FastAPI, containers, staged deployment and observability |
| P05 Language-model lab | Independent PyTorch starter and four experiment units | Actually run training, adaptation and checkpoint comparisons |
| P06 Inference systems | Validated trace formulas on explicit fixtures | Actual GPU benchmarks, compiler or distributed experiments |

## Quick start

From this directory, use Python 3.12:

```bash
python -m pip install -r requirements.lock
python -m unittest discover -s tests -v
python scripts/run_cpu_baselines.py
python scripts/validate_curriculum.py
```

CPU baselines need no paid model call or GPU. Training, real LLM generation, cloud deployment and GPU benchmarks remain separate experiments. The supplied HTTP server binds only to localhost and is a teaching adapter.

## Learning loop

Read a selected source section → run the baseline → make one independent change → compare under fixed conditions → explain a failure → submit evidence in a PR.

The source catalogue identifies what was inspected and how objectives were adapted. No upstream assignments or solution code are republished. Existing robot tools and architecture documents remain separate and are linked in [EXISTING_WORK](docs/EXISTING_WORK.md).

All learner milestones start uncompleted. Passing the supplied tests establishes the baseline's checked behavior, not completion of all 200 competencies.
