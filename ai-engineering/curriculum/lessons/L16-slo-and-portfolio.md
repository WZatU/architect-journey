# L16 SLO、恢复与作品集证据

项目：[AI 服务与架构实验](../../projects/p04-ai-service-architecture/README.md) · 前置：L15

架构判断需要运行数据与故障记录支持。这里把备份、恢复、成本和用户任务指标连接到面试能够核查的材料。

知识点：158、159、160、187、188、189、190、194、196、197、198、199、200。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S01: Stanford CS329S, Winter 2022](https://stanford-cs329s.github.io/syllabus.html)，阅读范围：Training Data; Offline Evaluation; Deployment; Diagnosis and Monitoring。
- [S02: Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/)，阅读范围：Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 定义检索延迟与错误率的窗口和目标，说明本地压测能支持哪些结论。
2. 恢复一份任务数据库备份，测量恢复时间并核对业务记录；写一次故障复盘。
3. 使用 case study 模板写问题、贡献、取舍、结果与限制，录制演示；将真实证据对应到三份目标 JD。

从 `ai-engineering/` 运行起点命令：

```bash
python scripts/validate_curriculum.py
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

SLO 定义、恢复记录、案例页、演示与 JD 对照；个人贡献和未实施部分清晰。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

你会在什么信号出现时扩容？这次设计中代价最大的取舍是什么？
