# 开始训练

主线顺序：P01 数据与实验 → P02 检索 → P03 工作流 → P04 服务。P05/P06 之后按求职方向选择。

## 第一次运行

在仓库根目录：

```bash
cd ai-engineering
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python -m unittest discover -s tests -v
python scripts/run_cpu_baselines.py
```

基线无需模型 API Key、GPU 或下载训练数据。依赖安装需要网络。`outputs/` 用于本地运行结果，不自动提交数据库、密钥或模型权重。

## 第一份自己的 PR

阅读 [L01](curriculum/lessons/L01-reproducible-python.md) 和 [L02](curriculum/lessons/L02-data-contracts-and-splits.md)，然后：

1. 运行 P01，解释 train/validation/test 的设备集合和选择 C 的过程。
2. 选择一个改变：新增树模型、增加一种模拟噪声，或将遥测写入 SQLite 并查询。
3. 运行同一数据划分的比较，保留失败案例，在实验模板中填写自己的假设与结论。
4. 提交 PR，口头解释为什么没有用测试集选择参数。

首个练习完成的标准是可运行修改与可复查报告。仓库里已提供的基线不算你的独立实现成果。

## 文件入口

- [课程总表](curriculum/SYLLABUS.md)
- [200 点映射](curriculum/KNOWLEDGE_MAP.md)
- [资料与改编说明](SOURCES.md)
- [已有机器人项目的衔接](docs/EXISTING_WORK.md)
- [验证与限制](reports/VALIDATION.md)
