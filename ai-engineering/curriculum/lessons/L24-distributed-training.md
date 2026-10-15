# L24 分布式训练与故障恢复

项目：[推理与训练系统实验室](../../projects/p06-inference-systems-lab/README.md) · 前置：L23

DDP、分片和模型并行解决不同资源限制。先建立单进程正确性参考，再测量多卡扩展和失败恢复。

知识点：177、178、179。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S10: PyTorch official distributed tutorial](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)，阅读范围：DistributedDataParallel; initialization, synchronization and checkpoint considerations。
- [S05: Stanford CS336, Spring 2026](https://cs336.stanford.edu/)，阅读范围：Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 写出设备数、梯度累积和每卡批量对应的有效批量，说明数据采样与梯度同步。
2. 在实际多卡环境选择 DDP 与一种分片方案比较吞吐、峰值内存与通信时间。
3. 模拟进程退出，恢复检查点并验证样本进度、优化器和模型状态；记录资源与运行日志。

从 `ai-engineering/` 运行起点命令：

```bash
python scripts/validate_curriculum.py
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

单进程参考、多卡实测、扩展效率与恢复记录；未运行的并行方案继续标为设计选修。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

卡数翻倍为何可能没有两倍吞吐？分片什么时候增加了通信成本？
