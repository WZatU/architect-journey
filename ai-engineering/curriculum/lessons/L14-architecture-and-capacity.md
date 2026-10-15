# L14 架构、容量、缓存与失败路径

项目：[AI 服务与架构实验](../../projects/p04-ai-service-architecture/README.md) · 前置：L13

以仓库现有 EAIC 架构为背景，给新增 AI 服务明确边界和依赖。小规模首先保证数据与故障语义，随后用负载数据判断拆分。

知识点：131、132、133、134、135、136、137、138、139、140、141、142、143、144、145、148、149、150。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S01: Stanford CS329S, Winter 2022](https://stanford-cs329s.github.io/syllabus.html)，阅读范围：Training Data; Offline Evaluation; Deployment; Diagnosis and Monitoring。
- [S12: Google Cloud Architecture Center, MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)，阅读范围：CI/CD/CT; data and model validation; metadata management。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 画 HLD 和一次请求的时序，标出权威存储、缓存、模型服务、在线与离线处理。
2. 假设给定峰值与延迟，估算在途请求；写缓存键、权限隔离、版本失效和背压策略。
3. 写两份 ADR：模块化单体与服务拆分、重试与降级；展示数据库或模型服务不可用时的行为。

从 `ai-engineering/` 运行起点命令：

```bash
python scripts/benchmark_local.py --requests 40 --workers 4 --output outputs/p04-benchmark.json
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

一张架构图、一个容量表、两份 ADR 与故障路径；假设和实测数据分开标记。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

增加副本后哪个状态会冲突？缓存过期、模型超时和数据库故障分别如何响应？
