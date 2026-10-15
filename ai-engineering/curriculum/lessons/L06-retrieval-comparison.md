# L06 比较关键词、向量与重排序

项目：[SDK 证据检索台](../../projects/p02-sdk-evidence-search/README.md) · 前置：L05

基线提供词项重叠与独立实现的 BM25。不同方法可能在短查询、精确编号和语义改写上各有表现。

知识点：66、89、90、91、92、93、94、96。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S03: Full Stack LLM Bootcamp, Spring 2023](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)，阅读范围：Augmented Language Models; Project Walkthrough askFSDL; LLMOps。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 比较 overlap 与 BM25 的逐查询排名，指出相同分数与失败查询。
2. 添加一个 Embedding 检索器，保持文档、过滤规则、查询和 K 相同；再尝试排序融合。
3. 只对候选集增加重排序，测量召回、MRR、延迟和资源；单独收集未参与开发的查询。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_retrieval.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

至少两个方法的逐查询结果、失败分组和可复现配置；独立 holdout 与公开开发集分开报告。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

Recall@K 高是否保证生成答案正确？向量检索何时漏掉型号和编号？
