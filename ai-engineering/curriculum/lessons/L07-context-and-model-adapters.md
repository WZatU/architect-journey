# L07 上下文、结构化输出与模型接入

项目：[SDK 证据检索台](../../projects/p02-sdk-evidence-search/README.md) · 前置：L06

目前基线只检索，不调用语言模型。这个单元把证据拼接、模型适配器和输出校验作为独立扩展，避免把检索指标误报成回答质量。

知识点：69、81、82、83、84、85、95、100。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S03: Full Stack LLM Bootcamp, Spring 2023](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)，阅读范围：Augmented Language Models; Project Walkthrough askFSDL; LLMOps。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 设计模型适配器接口与一个固定响应的测试替身，校验超时、错误与 JSON 输出。
2. 把授权检索结果按预算组成上下文；构造无证据问题，定义澄清或拒答条件。
3. 在明确请求数和预算后接入一个可用模型，用相同任务比较质量与成本；结构化数值通过受控 SQL 查询获取。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_service.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

模型调用与检索分别测试；引用逐项可验证；输出字段经过程序校验；实际模型结果与测试替身结果分开。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

多租户过滤在哪里发生？为什么不能接受请求体传来的 tenant 作为身份？
