# 有依赖顺序的执行任务

状态标记：`[ ]` 未开始，`[~]` 进行中，`[x]` 已完成。每项任务以“演示 + 自动测试 +
文档 + 失败实验”验收。不要同时开超过两个任务。

## P0：仓库与学习底座（第 1 周）

- [x] **P0-01 盘点现有项目**：识别 `robot_cpp`、Python 版本、测试数据与构建产物。
- [x] **P0-02 建立路线和架构基线**：README、记忆地图、12 月路线、EAIC 架构。
- [ ] **P0-03 文档模板**：增加 ADR、RFC、事故复盘、Runbook、威胁模型模板。
- [ ] **P0-04 自动质量门**：C++/Python CI、格式检查、单元测试、依赖扫描。
- [ ] **P0-05 开发环境**：Dev Container 或一键脚本，记录工具版本和新手操作。

验收：新电脑只看 README 就能构建、测试；GitHub 默认分支必须通过 CI。

## P1：最小 Control Plane（第 2–4 周）

- [ ] **P1-01 系统骨架**：FastAPI、配置、健康检查、结构化错误、依赖注入。
- [ ] **P1-02 数据库基础**：PostgreSQL、迁移、连接池、事务与索引实验。
- [ ] **P1-03 身份认证**：本地 OIDC Provider、Token 验证、用户/租户映射。
- [ ] **P1-04 权限模型**：Owner/Developer/Viewer RBAC，默认拒绝。
- [ ] **P1-05 Project API**：创建、读取、列表、归档；OpenAPI 与契约测试。
- [ ] **P1-06 Submission API**：创建上传、提交、查询状态；幂等键。
- [ ] **P1-07 对象存储**：MinIO 预签名上传、SHA-256、大小/类型限制、清理任务。
- [ ] **P1-08 审计日志**：actor/action/resource/before/after/trace_id，防敏感字段泄露。

验收：两个租户互不可见；相同幂等键请求 100 次只创建一个 Submission；文件有完整性哈希。

## P2：异步 Validation（第 5–7 周）

- [ ] **P2-01 Outbox**：业务写入和待发布 Event 同一事务。
- [ ] **P2-02 Broker**：NATS JetStream、本地持久化、ACK/重投递/DLQ。
- [ ] **P2-03 Validation Worker**：租约、心跳、超时、版本化报告。
- [ ] **P2-04 消费幂等**：Inbox/Event ID 去重，结果唯一约束。
- [ ] **P2-05 重试策略**：指数退避、抖动、最大次数、不可重试错误分类。
- [ ] **P2-06 失败恢复实验**：在 DB commit 前后、ACK 前后杀进程并记录结果。

验收：重复 Event、Worker 重启、Broker 延迟都不会生成两个 Validation 业务结果。

## P3：Scheduler、Run 与 Result（第 8–12 周）

- [ ] **P3-01 Robot/Capability 模型**：设备、能力、在线状态、租户归属。
- [ ] **P3-02 Reservation**：候选选择、并发预留、租约过期和公平性。
- [ ] **P3-03 Deployment**：版本化 Bundle、签名、下发与回执。
- [ ] **P3-04 Simulator Agent**：模拟机器人领取命令、执行和报告状态。
- [ ] **P3-05 Run 状态机**：CAS 状态迁移、取消、超时、Lost 判定。
- [ ] **P3-06 Result 上传**：Manifest、分片/断点续传、哈希校验。
- [ ] **P3-07 端到端 CLI**：一条命令演示 Submission 到 Result。
- [ ] **P3-08 本地容器环境**：Compose 启动 API/DB/Broker/MinIO/Worker/Simulator。
- [ ] **P3-09 CI/CD**：测试、镜像、SBOM、漏洞扫描、暂存环境、回滚。
- [ ] **P3-10 云部署**：IaC、Secret 管理、TLS、备份与恢复手册。

验收：并发请求不会把同一机器人分给两个 Run；服务重启后 Run 可恢复或进入明确终态。

## P4：平台可信度（第 4–6 月）

- [ ] **P4-01 Domain Model 与服务边界评审**。
- [ ] **P4-02 Command/Event Schema Registry 与向后兼容测试**。
- [ ] **P4-03 缓存策略**：权威源、TTL、失效、击穿/雪崩实验。
- [ ] **P4-04 多租户数据库隔离**：应用校验 + PostgreSQL RLS 双层防护。
- [ ] **P4-05 Billing Ledger**：预估、预留、入账、冲正；禁止覆盖历史。
- [ ] **P4-06 正向审计**：Submission → Billing 的完整证据链。
- [ ] **P4-07 反向审计**：账单金额 → Run → Result → Event → actor。
- [ ] **P4-08 OpenTelemetry**：统一 Logs/Metrics/Traces 和敏感数据规则。
- [ ] **P4-09 SLO/告警/Runbook**：错误预算、症状告警、处置步骤。
- [ ] **P4-10 备份恢复**：数据库 PITR、对象版本、季度恢复演练。

验收：任选账单行可反查所有因果；Schema N-1 客户端仍工作；恢复演练满足 RPO/RTO。

## P5：Robot Edge 平台（第 7–9 月）

- [ ] **P5-01 Robot Agent 架构与 Adapter 接口**。
- [ ] **P5-02 设备身份**：制造注册、短期证书、轮换、吊销、mTLS。
- [ ] **P5-03 ROS 2 Bridge**：Topic/Service/Action 映射与 QoS 决策表。
- [ ] **P5-04 时间和坐标**：NTP/PTP 偏差、frame_id、单位和校准版本。
- [ ] **P5-05 Telemetry 管线**：批处理、压缩、背压、保留策略。
- [ ] **P5-06 Video**：媒体走对象/流服务，事件只传引用和时间范围。
- [ ] **P5-07 Edge WAL**：断网缓存、顺序、去重、配额与数据补传。
- [ ] **P5-08 Safety Controller**：本地强制限位、急停和云端不可绕过。
- [ ] **P5-09 用户代码沙箱**：签名、最小权限、CPU/内存/网络限制。
- [ ] **P5-10 OTA/Fleet**：灰度、健康门、回滚、兼容矩阵。
- [ ] **P5-11 仿真与真实差距报告**：噪声、时延、动力学和 Safety Case。

验收：拔网线仍安全完成/中止；恢复后不重放物理动作，只补传带序号的事实。

## P6：Principal 级证据（第 10–12 月）

- [ ] **P6-01 工作负载模型**：租户、Submission 大小、Run 时长、遥测速率。
- [ ] **P6-02 容量与排队模型**：Little's Law、利用率、尾延迟、扩容阈值。
- [ ] **P6-03 压测与瓶颈剖析**：CPU、内存、网络、锁、连接池、IO。
- [ ] **P6-04 Cost Model**：每 Run 的计算/存储/传输/观测成本和毛利敏感性。
- [ ] **P6-05 Threat Model**：资产、信任边界、STRIDE、缓解与残余风险。
- [ ] **P6-06 数据治理**：分类、血缘、保留、删除、区域和访问审计。
- [ ] **P6-07 Build vs Buy 评估**：身份、消息、观测、视频、Fleet。
- [ ] **P6-08 故障注入矩阵**：DB、Broker、S3、网络、时钟、磁盘、证书。
- [ ] **P6-09 Game Day 与事故复盘**：角色、时间线、客户影响、系统性行动。
- [ ] **P6-10 ADR/RFC 集**：至少 10 个有替代方案和后果的决策。
- [ ] **P6-11 三年技术战略**：10×增长、平台边界、团队拓扑、预算和风险。
- [ ] **P6-12 Portfolio 演示**：架构讲解、现场失败恢复、正反向审计。

验收：针对模糊商业目标，能给出带数字、风险、负责人和里程碑的技术路线。

## 每一个任务的固定完成定义

- 功能路径和至少一个失败路径有自动测试；
- README 能让另一人复现；
- 记录 Owner、输入、输出、状态、存储、重试、去重、审计；
- 有可观察证据（日志、指标或 Trace），且不泄露 Secret/PII；
- 对用户可见的 API/Event 变更有版本和兼容说明；
- 更新 [`MEMORY_MAP.md`](MEMORY_MAP.md) 的当前进度。

