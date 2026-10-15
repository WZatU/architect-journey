# P01 机器人遥测实验台

把合成遥测转换成按设备隔离、可复现的分类实验。

当前范围：**CPU baseline implemented**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
python -m ai_path.experiment --seed 17 --output outputs/p01.json
```

已有检查：

```bash
python -m unittest discover -s tests -p test_experiment.py -v
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L01 把实验变成可运行的软件](../../curriculum/lessons/L01-reproducible-python.md)
- [L02 数据契约、SQL 与设备隔离](../../curriculum/lessons/L02-data-contracts-and-splits.md)
- [L03 基线、指标与统计不确定性](../../curriculum/lessons/L03-baselines-and-uncertainty.md)
- [L04 把实验写成可审查的研究记录](../../curriculum/lessons/L04-experiment-reports.md)

## 项目里程碑

- [ ] 新增树模型与按设备误差分析。
- [ ] 引入公开或自有授权遥测，重新设计标签与验证方案。
- [ ] 提交模型卡、消融与可复查实验报告。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
