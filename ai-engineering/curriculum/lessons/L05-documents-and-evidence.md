# L05 把文档变成有来源的证据

项目：[SDK 证据检索台](../../projects/p02-sdk-evidence-search/README.md) · 前置：L04

检索系统只能利用解析后保留下来的信息。这里先使用手写 JSON 文档，之后再引入 PDF、标题与表格解析。

知识点：86、87、88、97、98、99。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S03: Full Stack LLM Bootcamp, Spring 2023](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)，阅读范围：Augmented Language Models; Project Walkthrough askFSDL; LLMOps。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 检查 12 份虚构 SDK 文档的 ID、来源、租户和过期时间，列出每个字段的用途。
2. 加入一份自己的公开文档并保留来源，比较按段落与固定长度切块；为表格设计可追踪的表示。
3. 实现文档更新与删除测试，给每条引用保留文档版本和片段位置。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.retrieval
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

新增文档能追踪回原文；过期与删除内容不会进入新查询；解析丢失通过具体样例展示。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

引用存在是否就能证明回答正确？更新一个文档会影响哪些缓存与索引？
