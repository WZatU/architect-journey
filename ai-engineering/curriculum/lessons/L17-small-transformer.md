# L17 小型 Transformer 的结构与数值

项目：[语言模型训练实验室](../../projects/p05-language-model-lab/README.md) · 前置：L04

独立训练脚本使用虚构文档构造字节级因果语言模型。它用于检查训练流程，不能据此声称学到了可靠的领域能力。

知识点：61、62、63、64、65、67、68、70、71。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S05: Stanford CS336, Spring 2026](https://cs336.stanford.edu/)，阅读范围：Assignments 1 Basics, 2 Systems, 3 Scaling, 4 Data, 5 Alignment; lecture schedule。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 检查嵌入、位置、因果掩码、残差和输出层的张量形状；手算参数和激活开销。
2. 在安装 PyTorch 后运行 CPU smoke，确认损失有限；打乱掩码观察因果性测试会检查什么。
3. 解释字节编码与子词编码的取舍，再分别讨论图像、图结构数据应使用的归纳偏置。

从 `ai-engineering/` 运行起点命令：

```bash
python projects/p05-language-model-lab/train_tiny_lm.py --steps 20 --output outputs/p05-smoke.pt
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

有限损失、形状记录、参数预算与因果性检查；训练报告记录真实运行环境。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

为什么不能对未来 Token 可见？模型训练损失下降能否证明文档问答正确？
