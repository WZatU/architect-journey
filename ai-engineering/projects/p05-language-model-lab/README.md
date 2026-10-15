# P05 语言模型训练实验室

从小型因果模型出发，研究领域适配与可靠的训练实验。

当前范围：**PyTorch starter supplied; runtime not validated in this environment**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
python projects/p05-language-model-lab/train_tiny_lm.py --steps 20 --output outputs/p05-smoke.pt
```

已有检查：

```bash
python -m compileall -q projects/p05-language-model-lab
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L17 小型 Transformer 的结构与数值](../../curriculum/lessons/L17-small-transformer.md)
- [L18 领域数据、SFT 与 LoRA](../../curriculum/lessons/L18-adaptation-and-data.md)
- [L19 偏好、奖励与蒸馏实验设计](../../curriculum/lessons/L19-preference-and-rewards.md)
- [L20 训练检查点与复现实验](../../curriculum/lessons/L20-training-reproducibility.md)

## 项目里程碑

- [ ] 运行小模型并完成恢复对照。
- [ ] 按预算完成 SFT/LoRA 对比。
- [ ] 选修偏好、奖励或蒸馏，不要求同时完成。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
