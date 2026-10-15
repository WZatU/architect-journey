# L10 崩溃恢复、幂等与事务

项目：[可恢复工具工作流](../../projects/p03-durable-tool-workflow/README.md) · 前置：L09

一次请求超时不说明动作没发生。示例把库存修改、任务终态和事件记录放在同一 SQLite 事务中，并验证重试只产生一次效果。

知识点：105、106、146、147。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S06: LangGraph official documentation](https://docs.langchain.com/oss/python/langgraph/persistence)，阅读范围：Persistence and checkpointing; overview。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 重复执行同一任务，检查库存与 SUCCEEDED 事件数量；用相同幂等键提交不同参数。
2. 在提交前注入故障，重建 WorkflowStore 后恢复；并发提交相同任务观察锁与唯一约束。
3. 说明外部邮件或真实机器人命令无法被本地数据库回滚的原因，为其设计 Outbox 与对账流程。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_workflow.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

并发重复执行一次扣减；提交前故障无部分状态；写清本地事务保证与外部副作用边界。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

这个示例是否证明了跨系统 exactly-once？数据库提交后但网络响应前崩溃会怎样？
