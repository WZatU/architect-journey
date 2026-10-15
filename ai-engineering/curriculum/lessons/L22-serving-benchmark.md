# L22 KV Cache、批处理与推理指标

项目：[推理与训练系统实验室](../../projects/p06-inference-systems-lab/README.md) · 前置：L21

先用明确标为 fixture 的时间戳验证 TTFT、TPOT 和吞吐公式，再对真实服务收集数据；两类数据禁止混合。

知识点：167、168、169、170、171。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S09: vLLM official documentation and open-source project](https://docs.vllm.ai/en/latest/cli/bench/serve/)，阅读范围：Online serving benchmark; metrics; parallelism and scaling。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 手算 fixture 的首 Token、后续 Token 间隔和观测窗口吞吐，对照分析器输出。
2. 使用目标版本 vLLM 的官方 benchmark，在相同模型、输入输出长度与质量设置下比较并发度。
3. 报告 Prefill、Decode、KV Cache 与批处理的影响，保留原始数据、失败请求和硬件信息。

从 `ai-engineering/` 运行起点命令：

```bash
python -m unittest discover -s tests -p test_trace_metrics.py -v
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

公式测试通过；真实 benchmark 报告包含版本与负载；单独报告 fixture 和实测结果。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

一个 Token 的 TPOT 应填什么？固定并发闭环测试能否代表任意到达流量？
