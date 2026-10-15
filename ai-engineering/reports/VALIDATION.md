# Initial validation — 2026-10-15

Environment: Python 3.12.14, NumPy 2.3.5, scikit-learn 1.8.0, SciPy 1.17.0; local CPU container. The precise dependency set is in `requirements.lock`.

## Implemented and run

| Check | Observed result | Raw evidence |
|---|---|---|
| CPU tests | 22 tests passed; includes grouped splits, tenant filtering, authentication, overload rejection, rollback, concurrent idempotency and metric formulas | [Test log](baseline-2026-10-15/tests.txt) |
| P01 synthetic telemetry | 720 rows, 60 device groups; train/validation/test 432/144/144; test macro-F1 0.961879; majority baseline 0.389831 | [P01 JSON](baseline-2026-10-15/p01.json) |
| P01 uncertainty | Test accuracy 0.965278; device-bootstrap 95% interval [0.930556, 0.993056] | [P01 JSON](baseline-2026-10-15/p01.json) |
| P02 lexical retrieval | 36 development queries: 30 answerable, 6 unanswerable; mean Recall@3 overlap 0.883333, BM25 0.933333; MRR@3 0.866667 vs 0.916667 | [P02 JSON](baseline-2026-10-15/p02.json) |
| P02 no-evidence cases | Both retrievers return no candidates for 2/6 unanswerable queries. Four still return irrelevant candidates; generation and refusal behavior are not evaluated | [P02 per-query results](baseline-2026-10-15/p02.json) |
| P03 simulated reservation | Repeated task success leaves inventory at 8 from initial 10; one SUCCEEDED event; no external operations | [P03 JSON](baseline-2026-10-15/p03.json) |
| P04 local HTTP | 40/40 correct responses, zero HTTP errors, four concurrent closed-loop clients; warmup excluded | [P04 raw requests and timings](baseline-2026-10-15/p04-benchmark.json) |
| P06 formula validation | Hand-authored timestamps produce TTFT 0.45 s and mean TPOT 0.15 s; origin remains fixture | [P06 fixture calculation](baseline-2026-10-15/p06-fixture.json) |

The localhost HTTP run lasts only a small fraction of a second and includes no model. Its throughput and percentiles are a smoke observation, not a production capacity or LLM serving claim. Repeated runs may vary substantially.

## Structure and source checks

- Six project specifications and 24 lesson files are present.
- All 200 numbered knowledge points have a primary project, lesson, learning outcome and expected evidence.
- Prerequisite graph and links inside the new curriculum are checked by `scripts/validate_curriculum.py`.
- [Source catalogue](../SOURCES.md) records 12 primary course/documentation sources, inspected sections and independent adaptations.
- Existing robot C++ code and architecture documents are not changed by the curriculum implementation; integration links refer to their existing paths.

## Supplied but not runtime-validated here

- P05 PyTorch starter: Python syntax compilation only. PyTorch is not installed in this environment; no trained model, loss curve, LoRA result or checkpoint equivalence result is claimed.
- P06 GPU kernels, vLLM service benchmark, quantization, DDP/FSDP and multi-GPU recovery: exercise specifications, not completed measurements.
- Actual LLM-backed answers, LLM planning, cloud deployment, FastAPI migration, container orchestration and production observability: extension work.
- GitHub Actions workflow is supplied. Its remote execution status must be checked separately; local tests do not establish a hosted CI pass.

All personal learning progress starts uncompleted. The supplied implementation is a reference baseline; independent learner contributions should be recorded in subsequent PRs.
