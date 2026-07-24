# EAIC Architect Journey

这是一个“用真实系统建设学习架构”的长期作品集。目标不是收集名词，而是逐步做出、
解释、压测和审计一条完整的机器人云平台链路：

```text
Project → Submission → Validation → Reservation
        → Deployment → Run → Result → Billing
```

## 现在有什么

- [`robot_cpp/`](robot_cpp/)：C++17 机器人 CSV 读取、运动指标分析与 JSON 导出工具。
- [`robot_metrics.py`](robot_metrics.py)：同一计算管线的 Python 版本，便于比较语言与实现。
- [`docs/MEMORY_MAP.md`](docs/MEMORY_MAP.md)：每次回来先看这里；一分钟恢复上下文。
- [`docs/ROADMAP.md`](docs/ROADMAP.md)：12 个月学习和建设路线。
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)：EAIC 主链设计、数据归属和失败恢复。
- [`docs/BACKLOG.md`](docs/BACKLOG.md)：按依赖排序的可执行任务与验收标准。

## 如何学习每个任务

每个任务都必须留下五件东西：

1. 可运行代码；
2. 自动化测试；
3. 一张小图或一段数据流解释；
4. 一次失败实验；
5. 一段“我学到了什么”的简短记录。

完成不等于“代码能启动”。完成是你能够回答：

- 数据存在哪里，谁是 Owner？
- 重复请求会不会重复扣费或重复运行？
- 服务在任意一步重启后怎样恢复？
- 哪些失败能重试，哪些必须人工处理？
- 如何从账单反查到一次 Run，再反查到原始 Submission？

## 当前入口

先验证已有 C++ 项目：

```bash
cmake -S robot_cpp -B robot_cpp/build
cmake --build robot_cpp/build
ctest --test-dir robot_cpp/build --output-on-failure
```

然后从 [`P0`](docs/BACKLOG.md#p0仓库与学习底座第-1-周) 开始，按编号推进。

