# L02 数据契约、SQL 与设备隔离

项目：[机器人遥测实验台](../../projects/p01-telemetry-experiments/README.md) · 前置：L01

同一台设备的多次运行常共享偏差。随机拆行会把设备特征同时带进训练与测试，夸大对新设备的表现。

知识点：21、22、23、24、25、26、27、28、29、30、31、32、33、34、35、36、37、38、39、40。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S01: Stanford CS329S, Winter 2022](https://stanford-cs329s.github.io/syllabus.html)，阅读范围：Training Data; Offline Evaluation; Deployment; Diagnosis and Monitoring。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 检查 generated telemetry 的四个特征、标签来源和 device 分组，写数据字典。
2. 将记录写入本地 SQLite，编写设备聚合与窗口查询；检查重复运行、缺失字段和无效范围。
3. 对比随机拆行、按设备划分和时间前向划分；构造一个未来信息泄漏特征并说明为什么应排除。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_experiment.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

训练、验证、测试设备集合两两不相交；SQL 与 Python 聚合一致；数据字典说明时间语义与标签产生方式。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

为什么本项目不能宣称真实机器人的故障检测率？什么时候按设备划分还不够？
