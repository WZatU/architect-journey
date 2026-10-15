# L03 基线、指标与统计不确定性

项目：[机器人遥测实验台](../../projects/p01-telemetry-experiments/README.md) · 前置：L02

多数类基线能暴露类别失衡。模型选择使用验证集，最后一次测试保留给选定方案；设备 Bootstrap 保留组内相关性。

知识点：41、42、43、44、45、46、47、48、49、50、51、52、53、54、55、57。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S11: scikit-learn official model evaluation documentation](https://scikit-learn.org/stable/modules/model_evaluation.html)，阅读范围：Classification metrics, scoring and model evaluation。
- [S01: Stanford CS329S, Winter 2022](https://stanford-cs329s.github.io/syllabus.html)，阅读范围：Training Data; Offline Evaluation; Deployment; Diagnosis and Monitoring。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 解释 DummyClassifier、标准化和 LogisticRegression 的位置，确认 scaler 没有看到测试数据。
2. 手算一个小混淆矩阵的 Precision、Recall 与 F1，再解释宏平均为何可能与准确率不同。
3. 根据设备 Bootstrap 区间讨论样本量，补充阈值成本表和概率校准图；比较一种树模型但不根据测试集反复调参。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.experiment --seed 17
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

报告包含基线、验证选择依据、测试结果、区间与失败样本；新增方案使用相同设备划分。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

Brier score 与 F1 测量什么？为什么逐行 Bootstrap 会低估某些不确定性？
