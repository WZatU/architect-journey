# L08 评测集与发布门槛

项目：[SDK 证据检索台](../../projects/p02-sdk-evidence-search/README.md) · 前置：L07

开发查询用于找问题，冻结测试用于评估下一版。无答案问题使用独立分母，防止它们被当成普通命中问题计算。

知识点：111、112、113、114、116、118、119、120。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S03: Full Stack LLM Bootcamp, Spring 2023](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)，阅读范围：Augmented Language Models; Project Walkthrough askFSDL; LLMOps。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 为查询标注相关文档和困难类型，检查标注分歧；补充中文、长文和无答案问题。
2. 把事实正确、引用支持、任务完成分别评分；有程序验证器的任务优先用验证器。
3. 如加入模型裁判，先对齐人工标注再设回归门槛，记录线上反馈如何变成新测试。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.retrieval --output outputs/p02.json
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

冻结集、标注说明、分组指标和一条实际执行的发布检查；解释每个指标的分母。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

怎样发现裁判偏好长回答？哪些反馈可以进入训练，哪些应继续留在测试？
