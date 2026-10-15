# L13 服务 API 与组件边界

项目：[AI 服务与架构实验](../../projects/p04-ai-service-architecture/README.md) · 前置：L12

已有 localhost HTTP 适配器暴露健康检查与只读检索。组件逻辑与 HTTP 解耦，便于迁移到 FastAPI 等生产框架。

知识点：121、122、123、125、126、127、128、129、130。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S02: Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/)，阅读范围：Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 运行服务，验证 200、400、401 和 404；检查身份映射与字段边界。
2. 将 HTTP 适配器移植到 FastAPI，复用检索逻辑，并保持契约测试通过。
3. 设计长任务的创建、状态、取消接口以及 SSE 流式响应；为任务与大文件选择不同存储。

从 `ai-engineering/` 运行起点命令：

```bash
AI_PATH_TOKEN=local-demo python -m ai_path.service --port 8000
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

接口契约、错误示例与可运行服务；迁移前后语义一致；只读检索和有副作用操作分开授权。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

为什么模型输出格式不能代替服务端校验？连接中断是否应该取消后台任务？
