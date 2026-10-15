# L04 把实验写成可审查的研究记录

项目：[机器人遥测实验台](../../projects/p01-telemetry-experiments/README.md) · 前置：L03

一个分数无法解释模型为何改善、在哪些条件下失败。研究记录把假设、资源、数据与结果对应起来。

知识点：56、58、59、60、186、191、192、193、195。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S02: Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/)，阅读范围：Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 从报告中挑三种失败，按设备、噪声与标签边界分类，写可检验的假设。
2. 只改变一个因素做消融，并保留失败运行；先规定验证选择规则，再查看测试结果。
3. 使用实验报告模板写英文摘要，标明合成数据、个人修改和未验证的外推；选择一篇相关论文说明复现实验的差距。

从 `ai-engineering/` 运行起点命令：

```bash
python scripts/run_cpu_baselines.py
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

一次可复现实验、一个消融表、三个失败案例和一份含限制的英文实验摘要。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

如果验证集也被反复试验利用，应怎样保护最终评估？哪个结论需要新的真实数据？
