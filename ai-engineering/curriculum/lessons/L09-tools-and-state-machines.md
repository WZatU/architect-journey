# L09 工具契约与任务状态机

项目：[可恢复工具工作流](../../projects/p03-durable-tool-workflow/README.md) · 前置：L08

工具产生业务状态变化，控制器需要明确允许哪些转换。当前实现是确定性的模拟器，语言模型规划器留作后续适配。

知识点：101、102、103、104。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S06: LangGraph official documentation](https://docs.langchain.com/oss/python/langgraph/persistence)，阅读范围：Persistence and checkpointing; overview。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 画出 WAITING_APPROVAL、APPROVED、SUCCEEDED 的转换，逐条对应公开方法。
2. 为 propose、approve、execute 写参数、错误、前置条件和返回值说明。
3. 设计一个可替换规划器，只允许输出受校验的工具调用；给无效工具和无限循环设置退出条件。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.workflow
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

状态转换图、工具契约和非法转换测试；接入规划器后仍经过同一控制器。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

模型输出一个 execute 指令能否直接更改库存？任务成功怎样得到验证？
