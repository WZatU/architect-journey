# 一分钟记忆地图

## 这是什么

这是你的 Principal Architect 实战训练仓库。EAIC 是主训练系统，`robot_cpp` 是已经存在的
第一个小项目。

## 只记住一条主链

```text
用户建 Project
→ 上传 Submission
→ 系统 Validation
→ Scheduler 预留资源 Reservation
→ 下发 Deployment
→ 机器人执行 Run
→ 收集 Result
→ Billing 记账
```

## 只记住四条工程原则

1. PostgreSQL 是业务事实来源；缓存丢了也不能丢事实。
2. 每个外部命令都有幂等键；重复到达不能产生第二次业务效果。
3. 数据库事务只保证本服务内一致性；跨服务使用 Outbox、事件和补偿。
4. 每一步必须可追踪：`trace_id` 串请求，业务 ID 串审计，Ledger 串费用。

## 现在进度

- 已有：机器人 CSV → C++ 数据 → 速度/加速度统计 → JSON。
- 当前：建立仓库、路线、架构和任务底座。
- 下一件事：`P0-03` 建立 ADR/RFC 模板，然后进入 `P1-01` 最小 API。

## 每次回来怎么继续

1. 看本页。
2. 打开 [`BACKLOG.md`](BACKLOG.md)，找到第一个未完成任务。
3. 只做一个纵向切片，运行验收命令。
4. 更新本页“现在进度”和对应任务状态。

