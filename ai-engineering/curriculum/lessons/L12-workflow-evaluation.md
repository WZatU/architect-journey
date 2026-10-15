# L12 执行过程评测与故障实验

项目：[可恢复工具工作流](../../projects/p03-durable-tool-workflow/README.md) · 前置：L11

最终状态相同，过程仍可能重复扣减、泄漏数据或超出预算。过程评测检查工具轨迹与业务不变量。

知识点：110、115、117、185。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S06: LangGraph official documentation](https://docs.langchain.com/oss/python/langgraph/persistence)，阅读范围：Persistence and checkpointing; overview。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 建立正常、拒批、库存不足、越权、重复和中断六类任务，记录期望事件。
2. 为每步增加 trace_id、耗时和错误分类；控制记录中的敏感信息。
3. 对比可重试与不可重试错误，写重试上限和人工接管条件；如果接入 LangGraph，保留相同业务验收。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_workflow.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

故障矩阵、轨迹记录和业务不变量检查；确定性控制器与 LLM 规划器效果分别报告。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

成功率提升是否可能来自重复执行？哪个错误应立即停止重试？
