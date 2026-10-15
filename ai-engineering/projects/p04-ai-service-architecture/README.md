# P04 AI 服务与架构实验

把检索封装成可测试的本地 API，并测量负载、恢复和成本。

当前范围：**Local HTTP baseline implemented; cloud operations are exercises**。所有课程练习的个人完成状态仍为未开始。

## 起点

从 `ai-engineering/` 运行：

```bash
AI_PATH_TOKEN=local-demo python -m ai_path.service --port 8000
```

已有检查：

```bash
python -m unittest discover -s tests -p test_service.py -v
```

P01–P04 的代码在 `ai_path/`。P05 提供独立 PyTorch starter，P06 的时间分析器在 `ai_path/trace_metrics.py`。
当前 CPU 验证与限制见 [验证记录](../../reports/VALIDATION.md)。

## 四个课程单元

- [L13 服务 API 与组件边界](../../curriculum/lessons/L13-api-and-component-boundaries.md)
- [L14 架构、容量、缓存与失败路径](../../curriculum/lessons/L14-architecture-and-capacity.md)
- [L15 部署、CI 和可观测性](../../curriculum/lessons/L15-deployment-and-observability.md)
- [L16 SLO、恢复与作品集证据](../../curriculum/lessons/L16-slo-and-portfolio.md)

## 项目里程碑

- [ ] 移植 FastAPI 并保持接口语义。
- [ ] 完成容器与预发布运行、观测和回滚。
- [ ] 编写容量、恢复和架构案例报告。

每项里程碑提交独立 PR，附运行命令、原始输出、失败案例与设计判断。合成数据和测试时间戳的结论不能外推成真实设备或 GPU 成绩。

## GitHub 交付

使用 [项目案例模板](../../templates/CASE_STUDY.md)、[实验模板](../../templates/EXPERIMENT.md)、[ADR 模板](../../templates/ADR.md)。至少交付问题定义、可运行代码、架构或数据流、对照结果、失败分析、个人贡献和来源。

项目扩展完成后，再以自己的结果填写案例页。研究方向的训练和系统实验是选修，不能用结构检查通过代替实验完成。
