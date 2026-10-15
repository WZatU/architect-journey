# L20 训练检查点与复现实验

项目：[语言模型训练实验室](../../projects/p05-language-model-lab/README.md) · 前置：L19

训练恢复涉及模型之外的优化器、随机数和数据进度。先在单进程固定数据上验证，再扩展到分布式。

知识点：173、180。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S05: Stanford CS336, Spring 2026](https://cs336.stanford.edu/)，阅读范围：Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule。
- [S10: PyTorch official distributed tutorial](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)，阅读范围：DistributedDataParallel; initialization, synchronization and checkpoint considerations。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 检查 starter 保存的模型、优化器和 RNG 状态，在相同环境做连续与中断恢复对照。
2. 比较两种学习率与一种正则化设置，只用验证集选择；记录数值稳定与数据加载问题。
3. 保存模型卡、失败运行和最小复现实验；复现目标与资源受限的简化版本分别说明。

从 `ai-engineering/` 运行起点命令：

```bash
python projects/p05-language-model-lab/train_tiny_lm.py --steps 10 --resume outputs/p05-smoke.pt --output outputs/p05-resumed.pt
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

恢复行为对照、环境与配置记录，以及清晰标明规模限制的实验报告。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

只保存模型权重能否恢复相同训练轨迹？分布式采样器的进度还需要保存什么？
