# L15 部署、CI 和可观测性

项目：[AI 服务与架构实验](../../projects/p04-ai-service-architecture/README.md) · 前置：L14

本仓库提供 CI 工作流与本地服务测试。容器、云部署和观测栈是明确列出的扩展任务，实际运行后再登记结果。

知识点：151、152、153、154、155、156、157。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S02: Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/)，阅读范围：Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring。
- [S12: Google Cloud Architecture Center, MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)，阅读范围：CI/CD/CT; data and model validation; metadata management。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 阅读 CI，故意引入一个接口回归确认检查失败，再修复并保留证据。
2. 制作容器并在选定平台启动预发布环境，配置探针、资源限制和服务端凭据。
3. 打通日志、指标与 trace；演示一次灰度和回滚，记录镜像与模型版本对应关系。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

CI 记录、可复现镜像、预发布运行记录与回滚演示；没有运行过的基础设施继续标为 planned。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

健康检查通过是否说明模型质量正常？哪个变更需要重建索引或重跑评测？
