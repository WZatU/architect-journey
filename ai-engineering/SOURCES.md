# Sources and independent adaptations

Reviewed on 2026-10-15. Course editions are stated explicitly; older courses provide durable design principles, while current library APIs must be checked against the installed version.

This curriculum is independently authored. It is not affiliated with Stanford, FSDL, Anyscale, Hugging Face, LangChain, or the referenced projects. Reading a course does not imply enrollment or certification.

## What was extracted

Learning objectives, experiment patterns, and the separation of data, evaluation, serving, and operations. Each lesson links the relevant source. Exercise statements, simulator data, implementations, and acceptance criteria here are original.

| ID | Primary source | Inspected scope | Adaptation |
|---|---|---|---|
| S01 | [Stanford CS329S, Winter 2022](https://stanford-cs329s.github.io/syllabus.html) | Training Data; Offline Evaluation; Deployment; Diagnosis and Monitoring | P01/P04: connect requirements, data, evaluation and operations. |
| S02 | [Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/) | Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring | P01/P04: reproducible experiments, tests, deployment and monitoring. |
| S03 | [Full Stack LLM Bootcamp, Spring 2023](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) | Augmented Language Models; Project Walkthrough askFSDL; LLMOps | P02: retrieval, context construction and application evaluation. |
| S04 | [Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/) | Design; Data; Evaluation; Testing; Versioning; CI/CD workflows | P01/P04: independently implement a small experiment-to-service lifecycle. |
| S05 | [Stanford CS336, Spring 2026](https://cs336.stanford.edu/) | Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule | P05/P06: reduce broad learning objectives to original document-LM and measurement exercises. |
| S06 | [LangGraph official documentation](https://docs.langchain.com/oss/python/langgraph/persistence) | Persistence and checkpointing; overview | P03: independent SQLite state machine first; framework port as an extension. |
| S07 | [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) | LoRA conceptual guide | P05: adapter memory accounting and a separately measured adaptation experiment. |
| S08 | [Hugging Face TRL documentation](https://huggingface.co/docs/trl/index) | SFT; DPO; GRPO; reward modeling; distillation | P05: compare objectives and data contracts; advanced training is elective. |
| S09 | [vLLM official documentation and open-source project](https://docs.vllm.ai/en/latest/cli/bench/serve/) | Online serving benchmark; metrics; parallelism and scaling | P06: real serving measurements after validating metric formulas. |
| S10 | [PyTorch official distributed tutorial](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | DistributedDataParallel; initialization, synchronization and checkpoint considerations | P06: single-process reference, then a separately measured distributed run. |
| S11 | [scikit-learn official model evaluation documentation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Classification metrics, scoring and model evaluation | P01: macro-F1, confusion matrix, Brier score and fixed holdout evaluation. |
| S12 | [Google Cloud Architecture Center, MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) | CI/CD/CT; data and model validation; metadata management | P04: release criteria, version lineage and operational experiments. |

## Code and material reuse

- No upstream course handouts, assignment solutions, lecture text, or repository source files are vendored in this initial version.
- Made With ML source is referenced at [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML), with its [MIT license](https://github.com/GokuMohandas/Made-With-ML/blob/main/LICENSE). Its course website and repository are separate resources.
- vLLM is referenced at [vllm-project/vllm](https://github.com/vllm-project/vllm), with its [Apache-2.0 license](https://github.com/vllm-project/vllm/blob/main/LICENSE). No vLLM implementation is copied here.
- LangGraph is studied through official documentation; the initial controller uses the Python standard library. A framework port should cite the exact version and commit.
- Future copied or modified code must record the upstream URL, commit, file, modifications, and applicable license notices in this file before inclusion.
- Stanford coursework has its own collaboration and publication policies. The projects here use separate fictional tasks and do not publish official assignment answers.

## Reference citation

Goku Mohandas, *MLOps Course — Made With ML*, 2023, https://madewithml.com/. Other resources are identified by authoring organization, edition, URL, and inspected section above.
