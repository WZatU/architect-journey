# L21 GPU 资源预算与性能分析

项目：[推理与训练系统实验室](../../projects/p06-inference-systems-lab/README.md) · 前置：L17

性能分析先确定测量边界与硬件，再判断计算、访存或数据供应是否限制吞吐。GPU 不可用时可以先完成预算与公式检查。

知识点：161、162、163、164、165、166、172。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S05: Stanford CS336, Spring 2026](https://cs336.stanford.edu/)，阅读范围：Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 列出目标设备和模型配置，计算权重、梯度、优化器、激活与缓存预算。
2. 写预热、同步和计时边界；分析混合精度与量化对精度和硬件支持的要求。
3. 在可用 GPU 上保存一份 profiler 轨迹，依据证据提出一个优化，并检查数值一致性。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.trace_metrics --input data/inference-fixture.jsonl
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

资源预算、测量协议与实际 profiler 证据；缺少 GPU 时只登记预算与计划。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

显存占用下降为什么未必加速？计时前后的同步会改变哪些观察？
