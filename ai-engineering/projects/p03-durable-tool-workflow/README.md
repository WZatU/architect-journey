# P03 可恢复工具工作流

模拟预留库存，验证审批、事务、重复执行和恢复。

当前范围：**Deterministic workflow implemented; LLM planner is an extension**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
python -m ai_path.workflow --database outputs/workflow.sqlite
```

已有检查：

```bash
python -m unittest discover -s tests -p test_workflow.py -v
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L09 工具契约与任务状态机](../../curriculum/lessons/L09-tools-and-state-machines.md)
- [L10 崩溃恢复、幂等与事务](../../curriculum/lessons/L10-durability-and-idempotency.md)
- [L11 身份、审批和执行边界](../../curriculum/lessons/L11-identity-approval-and-isolation.md)
- [L12 执行过程评测与故障实验](../../curriculum/lessons/L12-workflow-evaluation.md)

## 项目里程碑

- [ ] 记录身份、审批内容与 trace。
- [ ] 为外部副作用设计 Outbox 和对账。
- [ ] 接入可替换 LLM 规划器或 LangGraph，保留业务不变量。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
