---
name: board-repair-guide
description: 根据症状分诊台式电脑、笔记本、电脑主板、显卡、手机、电视、冰箱和其他家电的硬件维修，选择对应专项 Skill 并逐步指导检查。
---

# 硬件维修总入口

根据设备类型、准确型号和故障表现选择下列专项，先读取其 `SKILL.md`；多个部件都可能相关时组合读取。即使当前宿主不支持自动调用其他 Skill，也要直接读取下列相对路径的文件并按其流程工作；不要声称已调用未实际读取的 Skill。目录结构必须完整保留。无法判定类型时只问最影响下一步的少量问题。

| 场景 | 专项 |
| --- | --- |
| 台式电脑整机、POST、内存、启动 | [desktop-repair](skills/desktop-repair/SKILL.md) |
| 笔记本、充电、屏幕、散热 | [laptop-repair](skills/laptop-repair/SKILL.md) |
| 电脑主板、低压供电、元件 | [motherboard-repair](skills/motherboard-repair/SKILL.md) |
| 显卡不识别、花屏、供电 | [gpu-repair](skills/gpu-repair/SKILL.md) |
| 手机、充电、屏幕及板级问题 | [phone-repair](skills/phone-repair/SKILL.md) |
| 电视无图像、无声音或信号故障 | [tv-repair](skills/tv-repair/SKILL.md) |
| 冰箱制冷、结霜、漏水、噪声 | [refrigerator-repair](skills/refrigerator-repair/SKILL.md) |
| 洗衣机、空调、风扇等其他家电 | [appliance-repair](skills/appliance-repair/SKILL.md) |

## 使用原则

用中文按用户知识水平交流，先了解现象、故障经过、工具、维修经验和数据/食品等约束；根据一项或少量测量的实际结果推进。用户可以购买额外仪器，但先说明必要性、关键规格、替代方案与安全条件。明确每项测试目的、操作状态、测量位置、仪表设置、可能结果与局限；来源优先使用对应型号的官方手册或芯片数据手册，不捏造测点、参数与因果结论。不能依在板低阻或蜂鸣断定电容故障。

先识别市电、高压、带电电池、制冷剂、燃气及其他危险，再按专项安全边界处理。电阻、通断、二极管和电容测试前隔离所有电源并验证无电；接地、通电、焊接和注压须符合对应设备和工具手册。不同设备的进一步约束以专项为准。结尾记录已验证事实、候选、限制和验证结果。
