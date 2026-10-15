# L18 领域数据、SFT 与 LoRA

项目：[语言模型训练实验室](../../projects/p05-language-model-lab/README.md) · 前置：L17

继续预训练、监督微调与参数高效适配对数据和目标有不同要求。先写清任务与预算，再决定是否加载外部模型。

知识点：72、73、74、75、80。每项的操作目标见 [200 点映射](../KNOWLEDGE_MAP.md)。

## 阅读与提取

- [S07: Hugging Face PEFT documentation](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)，阅读范围：LoRA conceptual guide。
- [S08: Hugging Face TRL documentation](https://huggingface.co/docs/trl/index)，阅读范围：SFT; DPO; GRPO; reward modeling; distillation。

这些资料用于确定学习目标。下面练习以本仓库的独立问题和数据编写，完成情况需要由自己的代码与实验验证。

## 实验

1. 分别设计继续预训练文本与 SFT 对话样本，检查对话模板和标签掩码。
2. 对选定模型计算全量、LoRA 和 QLoRA 的显存项目，记录模型与数据许可。
3. 在另行准备的任务集上比较原模型、RAG 和适配模型；保留通用能力与领域任务的分组结果。

从 `ai-engineering/` 运行起点命令：

```bash
python -m compileall -q projects/p05-language-model-lab
```

起点命令只验证已有基线或课程结构；它不代表扩展实验已经完成。P05 的运行需要另外安装 PyTorch；GPU 与云实验只在具备相应资源时执行。

## 交付与验收

数据卡、训练配置、预算与独立评测；LoRA/QLoRA 训练结果只有在实际运行后才填写。

把命令、环境、原始输出和结论放进自己的 PR。使用 [实验报告模板](../../templates/EXPERIMENT.md)，不要把模板空白项当成结果。

## 口头复查

微调能否代替经常变化的事实数据库？适配器节省了哪些状态，哪些仍然存在？
