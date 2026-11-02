# Computer Hardware Repair Skill

[中文说明](README.zh-CN.md)

A reusable AI agent skill for step-by-step diagnosis and repair of computer hardware. Describe the symptoms, share clear photos and report measurements; the assistant helps choose the next test and explains what the result can and cannot establish.

## What it covers

- Desktop and laptop power, POST, boot, display and stability problems.
- Laptop charging, batteries, displays, keyboards and cooling.
- Graphics cards: detection, display artifacts, temperatures and power circuits.
- Memory, storage, fans, power supplies and common peripherals.
- Board-level investigation of capacitors, resistors, diodes, MOSFETs, inductors and low-voltage power rails.
- Selecting and using multimeters, oscilloscopes, current-limited bench supplies, thermal cameras, ESR/LCR meters and soldering tools.

The skill is written in Chinese and is designed to guide a Chinese-speaking user. It uses device-specific service manuals and component datasheets when available, and does not treat continuity beeps or low resistance alone as proof of a failed capacitor.

## How to use

Clone or download this repository, then copy the repository directory into the skills directory of an agent that supports the Agent Skills format, naming the destination `board-repair-guide`. Keep `SKILL.md` and its `references` directory together. Follow your agent's instructions to refresh its skill list. Then describe the device, symptoms and tools you own, for example:

> My laptop powers on but shows no image. I have a multimeter. Help me diagnose it step by step and wait for my results before moving on.

For a board-level fault, supply the exact board model and revision, clear photographs of the relevant area, previous measurements, and any service documentation. The skill can recommend additional tools when needed and explain their purpose and required specifications.

## Safety and limitations

This is guidance for a human technician, not an autonomous repair tool or a guarantee of an accurate diagnosis. Results depend on the exact device, instrument, measurements and skill of the operator. Disconnect power and batteries and verify absence of voltage before resistance, continuity, diode or capacitance measurements. Some equipment retains hazardous energy after unplugging. Mains power supplies, high-voltage display circuits, damaged batteries and uncertain isolation require qualified service. Oscilloscope grounding and power injection can damage equipment or cause injury if used incorrectly; follow the instrument and device manuals.

The instructions have been checked for skill structure and linked files. They have not been validated against a comprehensive set of real-world repair cases. Contributions with verified model-specific evidence and safe test procedures are welcome.

## License

MIT. See [LICENSE](LICENSE).
