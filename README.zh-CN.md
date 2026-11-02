# 电脑硬件检测与维修 Skill

[English](README.md)

这是一套供 AI Agent 使用的硬件维修 Skill，包含总入口和 8 个独立专项。你可以描述故障、提供清晰照片和测量读数，AI 会帮助选择下一项检查，并解释结果可以说明什么、还不能说明什么。

## 覆盖范围

- 台式机和笔记本的供电、自检、启动、显示及稳定性问题。
- 笔记本和手机的充电、电池、屏幕及其他部件。
- 电视、冰箱和其他家用电器的故障分诊与安全检查。
- 显卡识别、花屏、温度及供电问题。
- 内存、硬盘、风扇、电源和常见外设。
- 电容、电阻、二极管、MOS 管、电感和低压供电线路的板级排查。
- 万用表、示波器、可调直流电源、热成像设备、ESR/LCR 表和焊接工具的选择与使用。

Skill 以中文编写，面向中文使用者；会结合具体型号的维修手册与芯片数据手册进行判断。它不会仅凭蜂鸣或低阻就断定某个电容损坏。

## 使用方法

克隆或下载本仓库，将整个仓库目录复制到支持 Agent Skills 的 AI 工具的技能目录，并将目标目录命名为 `board-repair-guide`；保留根目录的 `SKILL.md` 和完整 `skills` 目录。即使宿主不支持原生 Skill 相互调用，总入口也会按相对路径读取对应专项。也可以将 `skills/` 下任意专项目录单独复制到技能目录；每个专项都包含自身所需的参考资料。按所用工具的说明刷新技能列表。之后描述设备、故障和现有工具，例如：

> 我的笔记本开机后黑屏，我有万用表。请一步一步指导我排查，每一步等我反馈结果后再继续。

进行板级维修时，最好提供准确的主板型号和版本、故障区域清晰照片、已有读数及维修资料。需要其他工具时，Skill 会说明用途和需要关注的规格。

## 安全与限制

本项目提供辅助指导，不能代替维修人员，也不保证诊断一定正确。结果取决于具体设备、仪器、读数和操作经验。测电阻、通断、二极管或电容前，应断开电源及电池并确认无残余电压。部分设备断电后仍可能有危险电荷；市电电源内部、显示器高压电路、损坏电池、燃气系统、密封制冷回路或无法确认隔离状态的设备，应交由专业人员处理。示波器接地和注压使用不当可能造成人身伤害或设备损坏，请遵循仪器和设备手册。

目前已检查 Skill 格式及引用文件，尚未通过全面的真实维修案例验证。欢迎提交有可靠型号依据和安全测试过程的改进。

## 许可证

MIT，详见 [LICENSE](LICENSE)。

## 专项技能

| Skill | 适用范围 |
| --- | --- |
| [desktop-repair](skills/desktop-repair/SKILL.md) | 台式电脑 |
| [laptop-repair](skills/laptop-repair/SKILL.md) | 笔记本电脑 |
| [motherboard-repair](skills/motherboard-repair/SKILL.md) | 电脑主板及低压板级电路 |
| [gpu-repair](skills/gpu-repair/SKILL.md) | 显卡 |
| [phone-repair](skills/phone-repair/SKILL.md) | 手机 |
| [tv-repair](skills/tv-repair/SKILL.md) | 电视 |
| [refrigerator-repair](skills/refrigerator-repair/SKILL.md) | 冰箱 |
| [appliance-repair](skills/appliance-repair/SKILL.md) | 其他家电 |
