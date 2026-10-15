# P02 SDK 证据检索台

在虚构 SDK 文档上比较检索，并追踪来源、权限和时效。

当前范围：**CPU retrieval baseline implemented; generation is an extension**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
python -m ai_path.retrieval --output outputs/p02.json
```

已有检查：

```bash
python -m unittest discover -s tests -p test_retrieval.py -v
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L05 把文档变成有来源的证据](../../curriculum/lessons/L05-documents-and-evidence.md)
- [L06 比较关键词、向量与重排序](../../curriculum/lessons/L06-retrieval-comparison.md)
- [L07 上下文、结构化输出与模型接入](../../curriculum/lessons/L07-context-and-model-adapters.md)
- [L08 评测集与发布门槛](../../curriculum/lessons/L08-evaluation-and-release-gates.md)

## 项目里程碑

- [ ] 增加向量检索与重排序对照。
- [ ] 接入模型并独立评价事实性与引用支持。
- [ ] 建立未参与开发的 holdout 与自动回归门槛。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
