# 200 个知识点与课程映射

编号对应前一轮讨论的 200 项。索引完整不表示学习者已掌握；所有个人进度初始为 `not_started`。
基线示范列只表示仓库有相关实现或检查，掌握程度仍由自己的修改、实验和口头复查判断。

| # | 知识点 | 练习目标 | 主项目 / 单元 | 基线示范 |
|---|---|---|---|---|
| 1 | Python 项目组织 | 将数据、训练、推理和评测分成可独立调用的模块 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 2 | 类型系统 | 明确参数和返回值，使用类型检查发现接口不一致 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 3 | 依赖管理 | 从锁定依赖重建运行环境并记录版本 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 4 | 异常设计 | 区分输入错误、暂时故障和程序缺陷 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 5 | 资源管理 | 释放连接、文件和任务资源，检查长期运行泄漏 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 6 | 迭代器与生成器 | 分批处理数据并解释内存占用 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 7 | 异步编程 | 识别阻塞操作并实现有界并发 I/O | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 8 | 线程与进程 | 根据负载和共享状态选择并发方式 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 9 | 测试设计 | 用不同层级测试验证业务行为与边界 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 10 | 可重复运行 | 通过配置、数据摘要和命令复现实验 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 11 | Git 协作 | 提交小型变更、审查差异并解决冲突 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 12 | 代码可维护性 | 控制职责与依赖，写出可接手的代码 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 13 | Linux 基础 | 排查进程、权限、磁盘和退出状态 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 14 | 调试方法 | 构造最小复现并缩小故障范围 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 15 | 内存管理 | 定位对象引用或缓存导致的内存增长 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 16 | 并发正确性 | 复现并处理竞争、锁和死锁 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 17 | 网络基础 | 解释 DNS、TCP、TLS、HTTP 与超时 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 18 | 第二门语言 | 应用方向补 TypeScript，系统方向补 C++ 接口 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 19 | 性能分析 | 用调用与资源测量决定优化位置 | P01 / [L01](lessons/L01-reproducible-python.md) | 有相关示范 |
| 20 | AI 辅助开发 | 验证生成代码并独立解释与修改 | P01 / [L01](lessons/L01-reproducible-python.md) | 课程扩展 |
| 21 | SQL 查询 | 使用关联、聚合、窗口函数与 CTE | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 22 | 数据库建模 | 设计键、约束及对象关系 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 23 | 索引与执行计划 | 解释查询开销与索引写入代价 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 24 | 事务与隔离级别 | 说明并发读写异常和原子性边界 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 25 | 批量数据管道 | 设计可重跑的数据处理步骤 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 26 | 流式数据处理 | 处理事件时间、乱序、迟到与重复 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 27 | 数据契约 | 约定类型、缺失值语义和兼容规则 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 28 | 数据质量检查 | 检测缺失、异常范围、重复与分布变化 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 29 | 标注设计 | 定义标签规则、抽样和分歧处理 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 30 | 数据血缘 | 追踪来源、变换和模型版本 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 31 | 数据集划分 | 根据设备、用户或时间隔离验证数据 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 32 | 时间点正确性 | 排除预测时刻尚未出现的信息 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 33 | 抽样与代表性 | 判断样本是否覆盖使用人群与困难条件 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 34 | 描述统计 | 用分位数、方差和分布解释长尾 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 35 | 条件概率与贝叶斯推断 | 说明新证据如何改变估计 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 36 | 参数估计 | 解释最大似然、最大后验与假设 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 37 | 不确定性估计 | 给出区间与适合相关样本的重采样 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 有相关示范 |
| 38 | 假设检验 | 控制重复比较、样本量和停止规则 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 39 | A/B 实验 | 设计随机分组、指标和观察窗口 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 40 | 时间序列验证 | 以前向或滚动方式模拟真实预测 | P01 / [L02](lessons/L02-data-contracts-and-splits.md) | 课程扩展 |
| 41 | 任务建模 | 把业务诉求转成明确的机器学习任务 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 42 | 基线方法 | 以规则或简单模型衡量复杂方案收益 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 43 | 树模型 | 与线性模型做相同数据条件的比较 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 44 | 特征工程 | 处理数值、类别、缺失和交互 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 45 | 预处理管道 | 只在训练数据拟合预处理变换 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 46 | 损失函数选择 | 把优化目标与业务错误成本对应 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 47 | 正则化 | 检验权重衰减、早停或 Dropout 的作用 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 48 | 优化器行为 | 解释更新规则和收敛问题 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 49 | 学习率调度 | 根据曲线检验预热与衰减 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 50 | 训练故障诊断 | 定位梯度、数据或数值异常 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 51 | 分类评价 | 根据类别比例选择合适分类指标 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 52 | 回归评价 | 解释 MAE、RMSE 的单位与异常值敏感性 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 53 | 排序评价 | 解释 NDCG、MAP 与 Recall@K | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 54 | 概率校准 | 比较预测概率与实际发生频率 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 55 | 决策阈值 | 根据漏报、误报和处理成本调整阈值 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 课程扩展 |
| 56 | 分组误差分析 | 按设备、场景和困难类型定位失败 | P01 / [L04](lessons/L04-experiment-reports.md) | 有相关示范 |
| 57 | 超参数搜索 | 用验证集与预算安排公平搜索 | P01 / [L03](lessons/L03-baselines-and-uncertainty.md) | 有相关示范 |
| 58 | 消融实验 | 单独改变一个因素并保留对照 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 59 | 实验复现 | 保留代码、数据、环境、随机状态和配置 | P01 / [L04](lessons/L04-experiment-reports.md) | 有相关示范 |
| 60 | 泛化与鲁棒性 | 测试新条件、噪声和输入扰动 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 61 | 数值稳定性 | 识别浮点误差和稳定计算形式 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 62 | 模型归纳偏置 | 解释卷积、图和序列结构的适用性 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 63 | Attention 计算 | 解释 QKV、形状及计算存储开销 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 64 | 注意力掩码 | 验证因果可见性与 Padding 行为 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 65 | Tokenizer | 比较编码方式、长度和特殊符号 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 66 | Embedding 学习 | 解释相似度、对比目标和负样本 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 67 | 位置编码 | 解释位置关系和长序列外推限制 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 68 | 残差与归一化 | 分析梯度传播和训练稳定性 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 69 | 长上下文利用 | 验证远处证据是否被正确利用 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 70 | 解码策略 | 测量温度或采样设置对任务的影响 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 71 | 预训练目标 | 解释 Token 预测目标与能力边界 | P05 / [L17](lessons/L17-small-transformer.md) | 课程扩展 |
| 72 | 领域继续预训练 | 检验领域收益、遗忘和污染 | P05 / [L18](lessons/L18-adaptation-and-data.md) | 课程扩展 |
| 73 | 监督微调 SFT | 正确处理模板、标签掩码和截断 | P05 / [L18](lessons/L18-adaptation-and-data.md) | 课程扩展 |
| 74 | LoRA | 解释低秩适配的参数、目标层和开销 | P05 / [L18](lessons/L18-adaptation-and-data.md) | 课程扩展 |
| 75 | QLoRA | 区分量化基座与适配器状态 | P05 / [L18](lessons/L18-adaptation-and-data.md) | 课程扩展 |
| 76 | 偏好优化 DPO | 理解偏好对、参考模型和优化信号 | P05 / [L19](lessons/L19-preference-and-rewards.md) | 课程扩展 |
| 77 | 强化学习后训练 | 解释策略、奖励、采样与更新 | P05 / [L19](lessons/L19-preference-and-rewards.md) | 课程扩展 |
| 78 | 奖励投机 | 构造高奖励但任务失败的例子 | P05 / [L19](lessons/L19-preference-and-rewards.md) | 课程扩展 |
| 79 | 知识蒸馏 | 以质量与资源指标比较教师和学生 | P05 / [L19](lessons/L19-preference-and-rewards.md) | 课程扩展 |
| 80 | 多模态模型 | 分别测试识别、定位与推理能力 | P05 / [L18](lessons/L18-adaptation-and-data.md) | 课程扩展 |
| 81 | 模型 API 集成 | 处理鉴权、版本、错误和超时 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 82 | 提示设计 | 以固定任务集检验指令与示例 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 83 | 结构化输出 | 通过程序校验结构和业务约束 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 84 | 上下文组织 | 分配指令、历史、证据与工具预算 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 85 | 模型路由 | 以任务效果与资源实测决定路由 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 86 | RAG 适用条件 | 判断哪些事实需要检索与更新 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 课程扩展 |
| 87 | 文档解析 | 保留标题、表格、OCR 与来源关系 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 课程扩展 |
| 88 | 文档切块 | 比较结构、长度和重叠的检索表现 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 课程扩展 |
| 89 | 检索模型选型 | 覆盖专业词、短查询和多语言 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 90 | 向量索引 | 比较召回、内存、构建与查询成本 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 91 | 关键词检索 | 理解 BM25 与精确标识符匹配 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 有相关示范 |
| 92 | 混合检索 | 在相同条件下比较排序融合 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 93 | 重排序 | 测量候选集重排的质量与延迟 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 94 | 查询改写 | 处理省略和指代并检查语义偏移 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 课程扩展 |
| 95 | 检索权限过滤 | 确保上下文符合身份、租户和时效 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 有相关示范 |
| 96 | 检索评价 | 构造相关性标注并计算召回与排名 | P02 / [L06](lessons/L06-retrieval-comparison.md) | 有相关示范 |
| 97 | 证据引用 | 逐项验证来源能否支持结论 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 课程扩展 |
| 98 | 证据不足处理 | 定义拒答、澄清与人工处理路径 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 课程扩展 |
| 99 | 索引生命周期 | 处理更新、删除、重建与缓存失效 | P02 / [L05](lessons/L05-documents-and-evidence.md) | 有相关示范 |
| 100 | 结构化数据查询 | 通过受控 SQL 或业务接口读取事实 | P02 / [L07](lessons/L07-context-and-model-adapters.md) | 课程扩展 |
| 101 | 工具接口设计 | 定义参数、前置条件、返回与错误 | P03 / [L09](lessons/L09-tools-and-state-machines.md) | 有相关示范 |
| 102 | 执行状态机 | 规定允许的转换和失败恢复位置 | P03 / [L09](lessons/L09-tools-and-state-machines.md) | 有相关示范 |
| 103 | 工作流选择 | 选择固定步骤与动态规划的组合 | P03 / [L09](lessons/L09-tools-and-state-machines.md) | 课程扩展 |
| 104 | 终止条件 | 限制步骤、时间、预算与无法继续状态 | P03 / [L09](lessons/L09-tools-and-state-machines.md) | 课程扩展 |
| 105 | 记忆管理 | 区分会话状态、长期记忆和失效规则 | P03 / [L10](lessons/L10-durability-and-idempotency.md) | 课程扩展 |
| 106 | 持久化执行 | 恢复任务进度并核对已产生的效果 | P03 / [L10](lessons/L10-durability-and-idempotency.md) | 有相关示范 |
| 107 | 操作预览与确认 | 把授权绑定到可检查的具体操作 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 有相关示范 |
| 108 | 工具权限范围 | 限制任务能够访问的数据与动作 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 有相关示范 |
| 109 | 执行沙箱 | 隔离不可信代码、凭据和资源 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 课程扩展 |
| 110 | Agent 追踪 | 记录调用、结果、状态和耗时 | P03 / [L12](lessons/L12-workflow-evaluation.md) | 有相关示范 |
| 111 | 评测集设计 | 覆盖真实任务与困难情况并保留独立测试 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 112 | 固定回归样例 | 把已知失败转换成稳定检查 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 有相关示范 |
| 113 | 可验证评分 | 优先使用断言、执行结果或明确规则 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 有相关示范 |
| 114 | 模型裁判校准 | 用人工标注检查一致性和偏差 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 115 | 执行过程评价 | 检查工具序列、参数、恢复和最终结果 | P03 / [L12](lessons/L12-workflow-evaluation.md) | 有相关示范 |
| 116 | 事实性评价 | 区分正确性、引用支持与任务满足 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 117 | 故障注入 | 模拟超时、坏格式、缺失与恶意内容 | P03 / [L12](lessons/L12-workflow-evaluation.md) | 有相关示范 |
| 118 | 线上效果指标 | 记录完成率、人工修改率和反馈口径 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 119 | 评测发布门槛 | 按质量、失败率和成本决定是否发布 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 120 | 反馈处理 | 把用户问题转成复现、标注与回归 | P02 / [L08](lessons/L08-evaluation-and-release-gates.md) | 课程扩展 |
| 121 | 后端 API 开发 | 提供可调用、可验证的服务接口 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 有相关示范 |
| 122 | 通信接口选择 | 按负载和调用方式选择 REST 或 RPC | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 123 | 请求校验 | 在昂贵处理前限制形状、长度和范围 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 有相关示范 |
| 124 | 认证与授权 | 分别检查身份和允许操作 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 有相关示范 |
| 125 | 接口版本兼容 | 验证旧客户端与新字段行为 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 126 | 长任务接口 | 支持创建、状态、取消和结果查询 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 127 | 流式响应 | 处理部分结果、断线和取消 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 128 | 对象存储 | 管理大文件版本、位置和访问 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 129 | 存储职责划分 | 按持久性与访问方式选择存储 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 课程扩展 |
| 130 | 组件边界 | 明确业务、检索、推理和调度职责 | P04 / [L13](lessons/L13-api-and-component-boundaries.md) | 有相关示范 |
| 131 | 架构约束收集 | 记录用户、峰值、延迟、数据和预算 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 132 | 总体架构设计 | 说明组件与数据流的职责 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 133 | 详细设计 | 写清接口、状态、表结构和失败路径 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 134 | 单体与微服务取舍 | 根据团队、部署和负载决定拆分 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 135 | 在线与离线处理 | 划分预处理、训练与在线预测 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 136 | 控制面与数据面 | 区分配置调度与实际计算流量 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 137 | 无状态服务设计 | 支持重启、副本与外部状态一致性 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 有相关示范 |
| 138 | 模型服务抽象 | 统一接口并保留能力与错误差异 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 139 | 版本兼容关系 | 关联模型、提示、索引、数据和代码 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 140 | 架构决策记录 ADR | 保留约束、备选、代价与选择理由 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 141 | 容量估算 | 在适用条件下估算速率、时延与在途请求 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 142 | 尾部延迟 | 解释 P95/P99 与分组长尾 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 143 | 负载测试 | 记录请求长度、并发和到达模式 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 有相关示范 |
| 144 | 队列与背压 | 限制积压并定义拒绝与等待策略 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 有相关示范 |
| 145 | 缓存设计 | 检查键、权限、版本与失效 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 146 | 幂等性 | 验证重复请求不产生第二次业务效果 | P03 / [L10](lessons/L10-durability-and-idempotency.md) | 有相关示范 |
| 147 | 消息投递语义 | 处理重复、丢失和事务消息边界 | P03 / [L10](lessons/L10-durability-and-idempotency.md) | 课程扩展 |
| 148 | 分布式一致性 | 说明暂时不一致与对账修复 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 149 | 重试预算 | 结合超时、退避和抖动控制请求放大 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 150 | 故障隔离与降级 | 限制故障扩散并提供可用路径 | P04 / [L14](lessons/L14-architecture-and-capacity.md) | 课程扩展 |
| 151 | 容器化 | 构建可重复启动且资源明确的镜像 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 152 | 持续集成 CI | 自动检查代码、测试、构建与契约 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 有相关示范 |
| 153 | 持续交付 CD | 验证预发布、灰度和回滚 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 154 | 云平台基础 | 实际使用计算、网络、存储与权限 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 155 | Kubernetes 基础 | 理解工作负载、探针和资源调度 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 156 | 计算任务调度 | 按服务、批处理、训练选择调度方式 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 157 | 可观测性 | 连接指标、日志与追踪定位失败 | P04 / [L15](lessons/L15-deployment-and-observability.md) | 课程扩展 |
| 158 | 服务目标 SLO | 定义用户可感知目标、窗口与错误预算 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 159 | 备份与恢复 | 验证可恢复性并记录 RPO/RTO | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 160 | 故障响应 | 演练诊断、止损、回滚与复盘 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 161 | GPU 结构 | 解释执行单元、线程束与带宽 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 162 | 计算与访存瓶颈 | 结合算术强度分析性能上限 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 163 | 显存预算 | 分项核算权重、梯度、优化器、激活与缓存 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 164 | GPU 测量方法 | 设置预热、同步和计时边界 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 165 | 混合精度 | 验证数值、硬件支持与性能收益 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 166 | 量化 | 分别比较权重、激活和质量变化 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 167 | Prefill 与 Decode | 分别分析输入处理与逐 Token 生成 | P06 / [L22](lessons/L22-serving-benchmark.md) | 课程扩展 |
| 168 | KV Cache 管理 | 估算长度、并发与缓存增长 | P06 / [L22](lessons/L22-serving-benchmark.md) | 课程扩展 |
| 169 | 推理批处理 | 解释动态与连续批处理的等待取舍 | P06 / [L22](lessons/L22-serving-benchmark.md) | 课程扩展 |
| 170 | 推理引擎使用 | 记录引擎、模型、硬件与测试条件 | P06 / [L22](lessons/L22-serving-benchmark.md) | 课程扩展 |
| 171 | 推理性能指标 | 分别计算 TTFT、TPOT、总延迟和吞吐 | P06 / [L22](lessons/L22-serving-benchmark.md) | 有相关示范 |
| 172 | GPU 性能剖析 | 从轨迹定位算子、等待与传输 | P06 / [L21](lessons/L21-gpu-resource-accounting.md) | 课程扩展 |
| 173 | 数据加载优化 | 比较解码、预取、Worker 与设备传输 | P05 / [L20](lessons/L20-training-reproducibility.md) | 课程扩展 |
| 174 | 编译优化 | 报告图中断、编译与稳态收益 | P06 / [L23](lessons/L23-compiler-and-kernels.md) | 课程扩展 |
| 175 | 算子与 Attention 优化 | 解释融合和减少中间访存 | P06 / [L23](lessons/L23-compiler-and-kernels.md) | 课程扩展 |
| 176 | 自定义 Kernel | 验证小算子正确性与形状适用范围 | P06 / [L23](lessons/L23-compiler-and-kernels.md) | 课程扩展 |
| 177 | DDP | 解释副本、数据采样、同步与有效批量 | P06 / [L24](lessons/L24-distributed-training.md) | 课程扩展 |
| 178 | FSDP 与 ZeRO | 核算分片节省的状态与通信代价 | P06 / [L24](lessons/L24-distributed-training.md) | 课程扩展 |
| 179 | 模型并行 | 分析张量、流水线和上下文并行 | P06 / [L24](lessons/L24-distributed-training.md) | 课程扩展 |
| 180 | 训练恢复 | 恢复模型、优化器、随机状态与数据进度 | P05 / [L20](lessons/L20-training-reproducibility.md) | 课程扩展 |
| 181 | 凭据管理 | 避免密钥进入代码、提示和日志 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 课程扩展 |
| 182 | 提示注入防护 | 在程序侧约束不可信内容的权限 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 课程扩展 |
| 183 | 数据隐私管理 | 定义采集、访问、保留与删除 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 课程扩展 |
| 184 | 依赖与模型来源 | 记录许可证、来源和完整性 | P03 / [L11](lessons/L11-identity-approval-and-isolation.md) | 课程扩展 |
| 185 | 成本核算 | 计算每次成功任务的总资源成本 | P03 / [L12](lessons/L12-workflow-evaluation.md) | 课程扩展 |
| 186 | 技术可行性判断 | 比较规则、传统 ML 与大模型的收益 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 187 | 行业知识 | 解释业务流程、约束和错误代价 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 188 | 需求沟通 | 明确输入、输出、指标与验收样例 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 189 | 技术写作与英语 | 写可审查设计、实验与故障报告 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 190 | 团队协作 | 通过契约、审查与复现减少沟通歧义 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 191 | 论文阅读 | 辨认问题、假设、实验与结论限制 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 192 | 论文复现 | 控制数据、基线、预算并解释结果差距 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 193 | 研究记录 | 保留假设、配置、失败与对照 | P01 / [L04](lessons/L04-experiment-reports.md) | 课程扩展 |
| 194 | 项目可运行性 | 让他人按说明安装、运行和验证 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 有相关示范 |
| 195 | 项目基准测试 | 在相同负载与质量条件下公平比较 | P01 / [L04](lessons/L04-experiment-reports.md) | 有相关示范 |
| 196 | 个人贡献证据 | 用修改、设计与实验支持贡献描述 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 197 | 系统设计面试 | 解释容量、数据流、故障和取舍 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 198 | 编码面试 | 在时限内说明正确性、复杂度与边界 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 199 | 岗位匹配 | 将目标职责对应到可核查证据 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
| 200 | 简历与面试表达 | 说明问题、工作、判断、结果与限制 | P04 / [L16](lessons/L16-slo-and-portfolio.md) | 课程扩展 |
