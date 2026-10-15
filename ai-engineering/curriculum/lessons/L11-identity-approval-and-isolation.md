# L11 身份、审批和执行边界

项目：[可恢复工具工作流](../../projects/p03-durable-tool-workflow/README.md) · 前置：L10

示例中的 reviewer 是模拟输入。真实身份应由可信认证组件提供，工具权限和业务审批由服务端检查。

知识点：107、108、109、124、181、182、183、184。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S06: LangGraph official documentation](https://docs.langchain.com/oss/python/langgraph/persistence)，阅读范围：Persistence and checkpointing; overview。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 验证读者角色无法批准任务，其他租户无法访问目标任务。
2. 写一个身份适配器接口，把模拟角色与真实角色来源隔离；定义审批记录包含的请求内容摘要。
3. 设计提示注入与不可信工具返回测试，列出哪些数据可以进入日志、哪些代码需要沙箱。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_workflow.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

角色、租户和审批绑定测试；一份数据保留与密钥处理说明；不得把 CLI 的模拟角色当成生产认证。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

审批之后任务参数改变了怎么办？模型从文档读到新指令能否扩大工具权限？
