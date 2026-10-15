# 项目课程总表

默认主线 P01 → P02 → P03 → P04；P05 与 P06 按岗位选修。每单元包含原理、指定阅读、三个实验任务、验收与口头复查。
先运行已有基线，再做独立修改。主线可按约 8–12 周、每周 10–15 小时安排；这是排程示例，完成时间取决于基础与项目扩展范围。GPU 选修另外排期。

| 项目 | 课程单元 | 学习成果 |
|---|---|---|
| [P01 机器人遥测实验台](../projects/p01-telemetry-experiments/README.md) | L01–L04 | 把合成遥测转换成按设备隔离、可复现的分类实验。 |
| [P02 SDK 证据检索台](../projects/p02-sdk-evidence-search/README.md) | L05–L08 | 在虚构 SDK 文档上比较检索，并追踪来源、权限和时效。 |
| [P03 可恢复工具工作流](../projects/p03-durable-tool-workflow/README.md) | L09–L12 | 模拟预留库存，验证审批、事务、重复执行和恢复。 |
| [P04 AI 服务与架构实验](../projects/p04-ai-service-architecture/README.md) | L13–L16 | 把检索封装成可测试的本地 API，并测量负载、恢复和成本。 |
| [P05 语言模型训练实验室](../projects/p05-language-model-lab/README.md) | L17–L20 | 从小型因果模型出发，研究领域适配与可靠的训练实验。 |
| [P06 推理与训练系统实验室](../projects/p06-inference-systems-lab/README.md) | L21–L24 | 先验证测量工具，再研究 GPU 推理与分布式训练的资源取舍。 |

| 单元 | 标题 | 主项目 | 交付验收 |
|---|---|---|---|
| [L01](lessons/L01-reproducible-python.md) | 把实验变成可运行的软件 | P01 | 在新环境通过同一命令运行；错误输入返回可理解的错误；提交小型 PR、环境记录和一次调试复盘。 |
| [L02](lessons/L02-data-contracts-and-splits.md) | 数据契约、SQL 与设备隔离 | P01 | 训练、验证、测试设备集合两两不相交；SQL 与 Python 聚合一致；数据字典说明时间语义与标签产生方式。 |
| [L03](lessons/L03-baselines-and-uncertainty.md) | 基线、指标与统计不确定性 | P01 | 报告包含基线、验证选择依据、测试结果、区间与失败样本；新增方案使用相同设备划分。 |
| [L04](lessons/L04-experiment-reports.md) | 把实验写成可审查的研究记录 | P01 | 一次可复现实验、一个消融表、三个失败案例和一份含限制的英文实验摘要。 |
| [L05](lessons/L05-documents-and-evidence.md) | 把文档变成有来源的证据 | P02 | 新增文档能追踪回原文；过期与删除内容不会进入新查询；解析丢失通过具体样例展示。 |
| [L06](lessons/L06-retrieval-comparison.md) | 比较关键词、向量与重排序 | P02 | 至少两个方法的逐查询结果、失败分组和可复现配置；独立 holdout 与公开开发集分开报告。 |
| [L07](lessons/L07-context-and-model-adapters.md) | 上下文、结构化输出与模型接入 | P02 | 模型调用与检索分别测试；引用逐项可验证；输出字段经过程序校验；实际模型结果与测试替身结果分开。 |
| [L08](lessons/L08-evaluation-and-release-gates.md) | 评测集与发布门槛 | P02 | 冻结集、标注说明、分组指标和一条实际执行的发布检查；解释每个指标的分母。 |
| [L09](lessons/L09-tools-and-state-machines.md) | 工具契约与任务状态机 | P03 | 状态转换图、工具契约和非法转换测试；接入规划器后仍经过同一控制器。 |
| [L10](lessons/L10-durability-and-idempotency.md) | 崩溃恢复、幂等与事务 | P03 | 并发重复执行一次扣减；提交前故障无部分状态；写清本地事务保证与外部副作用边界。 |
| [L11](lessons/L11-identity-approval-and-isolation.md) | 身份、审批和执行边界 | P03 | 角色、租户和审批绑定测试；一份数据保留与密钥处理说明；不得把 CLI 的模拟角色当成生产认证。 |
| [L12](lessons/L12-workflow-evaluation.md) | 执行过程评测与故障实验 | P03 | 故障矩阵、轨迹记录和业务不变量检查；确定性控制器与 LLM 规划器效果分别报告。 |
| [L13](lessons/L13-api-and-component-boundaries.md) | 服务 API 与组件边界 | P04 | 接口契约、错误示例与可运行服务；迁移前后语义一致；只读检索和有副作用操作分开授权。 |
| [L14](lessons/L14-architecture-and-capacity.md) | 架构、容量、缓存与失败路径 | P04 | 一张架构图、一个容量表、两份 ADR 与故障路径；假设和实测数据分开标记。 |
| [L15](lessons/L15-deployment-and-observability.md) | 部署、CI 和可观测性 | P04 | CI 记录、可复现镜像、预发布运行记录与回滚演示；没有运行过的基础设施继续标为 planned。 |
| [L16](lessons/L16-slo-and-portfolio.md) | SLO、恢复与作品集证据 | P04 | SLO 定义、恢复记录、案例页、演示与 JD 对照；个人贡献和未实施部分清晰。 |
| [L17](lessons/L17-small-transformer.md) | 小型 Transformer 的结构与数值 | P05 | 有限损失、形状记录、参数预算与因果性检查；训练报告记录真实运行环境。 |
| [L18](lessons/L18-adaptation-and-data.md) | 领域数据、SFT 与 LoRA | P05 | 数据卡、训练配置、预算与独立评测；LoRA/QLoRA 训练结果只有在实际运行后才填写。 |
| [L19](lessons/L19-preference-and-rewards.md) | 偏好、奖励与蒸馏实验设计 | P05 | 明确的目标、数据格式、失败案例和对照实验计划；没有训练记录时只提交设计结论。 |
| [L20](lessons/L20-training-reproducibility.md) | 训练检查点与复现实验 | P05 | 恢复行为对照、环境与配置记录，以及清晰标明规模限制的实验报告。 |
| [L21](lessons/L21-gpu-resource-accounting.md) | GPU 资源预算与性能分析 | P06 | 资源预算、测量协议与实际 profiler 证据；缺少 GPU 时只登记预算与计划。 |
| [L22](lessons/L22-serving-benchmark.md) | KV Cache、批处理与推理指标 | P06 | 公式测试通过；真实 benchmark 报告包含版本与负载；单独报告 fixture 和实测结果。 |
| [L23](lessons/L23-compiler-and-kernels.md) | 编译、融合算子与 Kernel | P06 | 正确性测试、预热协议、编译与稳态耗时分别报告；硬件加速结论来自实际运行。 |
| [L24](lessons/L24-distributed-training.md) | 分布式训练与故障恢复 | P06 | 单进程参考、多卡实测、扩展效率与恢复记录；未运行的并行方案继续标为设计选修。 |

## 按岗位选择

- Applied AI：完成 P01 的数据与实验基础，重点扩展 P02/P03/P04。真实模型接入与云部署需要后续实际完成。
- ML Engineer：深入 P01，完成 P04；选择 P05 的训练、数据与恢复实验。
- Research Engineer：以 P01 的严谨实验为基础，深入 P05，并选择 P06 的 profiling 或训练系统。
- ML Systems / Inference：深入 P04/P06，重点提供真实硬件上的性能与正确性证据。

## 一个项目何时值得展示

别人能够复现；有合理基线；比较条件公平；有真实测量与失败案例；能够说明自己的修改；已实施、未实施和适用限制明确。完成阅读本身不计作工程成果。
