# L01 把实验变成可运行的软件

项目：[机器人遥测实验台](../../projects/p01-telemetry-experiments/README.md) · 前置：Python 与基本 ML

同一段算法在 Notebook 中成功，换一台机器就失败，通常与环境、路径和隐式状态有关。这里从可调用函数、命令行入口与测试边界开始。

知识点：1、2、3、4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S02: Full Stack Deep Learning, 2022](https://fullstackdeeplearning.com/course/2022/)，阅读范围：Lecture 2 infrastructure; Lecture 3 testing; Lecture 4 data; Lecture 5 deployment; Lab 8 monitoring。
- [S04: Made With ML, Goku Mohandas](https://madewithml.com/courses/mlops/)，阅读范围：Design; Data; Evaluation; Testing; Versioning; CI/CD workflows。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 运行 P01，指出数据生成、划分、拟合与报告各自的函数边界。
2. 把一个参数通过命令行传入，补输入错误和资源释放检查；解释线程、进程、异步各适用于什么负载。
3. 建立新环境重跑，记录 Python 与依赖版本；用一个故意引入的错误演示最小复现和调试过程。

从 `ai-engineering/` 运行起点命令：

```bash
python -m ai_path.experiment --seed 17 --output outputs/p01.json
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

在新环境通过同一命令运行；错误输入返回可理解的错误；提交小型 PR、环境记录和一次调试复盘。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

哪个状态依赖当前工作目录？CPU 密集任务能否仅靠 async 提速？
