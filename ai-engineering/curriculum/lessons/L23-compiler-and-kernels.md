# L23 编译、融合算子与 Kernel

项目：[推理与训练系统实验室](../../projects/p06-inference-systems-lab/README.md) · 前置：L22

算子优化需要与正确参考比较，并把编译与预热成本纳入报告。这里保留小算子实验范围，避免在没有证据时修改整套模型。

知识点：174、175、176。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S05: Stanford CS336, Spring 2026](https://cs336.stanford.edu/)，阅读范围：Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 选择一个小算子建立 CPU 或 PyTorch 参考，规定数值误差与输入形状范围。
2. 比较 eager 与 torch.compile，记录图中断和首次编译；有条件时增加 Triton 实现。
3. 通过 profiler 解释访存和 Kernel 启动变化，验证不同形状与精度下的结果。

从 `ai-engineering/` 运行起点命令：

```bash
python scripts/validate_curriculum.py
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

正确性测试、预热协议、编译与稳态耗时分别报告；硬件加速结论来自实际运行。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

某个形状加速能否推及所有输入？融合如何改变中间张量与访存量？
