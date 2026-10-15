# P06 推理与训练系统实验室

先验证测量工具，再研究 GPU 推理与分布式训练的资源取舍。

当前范围：**Trace analyzer tested on fixtures; GPU and multi-GPU labs not run**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
python -m ai_path.trace_metrics --input data/inference-fixture.jsonl
```

已有检查：

```bash
python -m unittest discover -s tests -p test_trace_metrics.py -v
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L21 GPU 资源预算与性能分析](../../curriculum/lessons/L21-gpu-resource-accounting.md)
- [L22 KV Cache、批处理与推理指标](../../curriculum/lessons/L22-serving-benchmark.md)
- [L23 编译、融合算子与 Kernel](../../curriculum/lessons/L23-compiler-and-kernels.md)
- [L24 分布式训练与故障恢复](../../curriculum/lessons/L24-distributed-training.md)

## 项目里程碑

- [ ] 收集真实推理服务数据，比较质量、延迟、吞吐和成本。
- [ ] 完成一个编译或 Kernel 实验。
- [ ] 有硬件条件后选修多卡训练与恢复。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
