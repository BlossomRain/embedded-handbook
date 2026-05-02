# 嵌入式与器件手册

电子器件、MCU 基础与常用技术主题整理。

建议仓库名：`embedded-handbook`

这个项目按“手册”方式整理内容，既适合本地查阅，也适合后续发布到 GitHub Pages。当前重点不是做复杂网站，而是先把器件资料、技术主题、配图和说明规范沉淀成一套长期可维护的资料库。

## 入口导航

| 入口 | 说明 | 文档 |
|---|---|---|
| 技术介绍 | GPIO、PWM、接口、时钟、信号等通用知识 | [打开](./content/technology-introduction/README.md) |
| 器件原理 | 常用器件的引脚、参数、使用方式与示意图 | [打开](./content/device-principles/README.md) |
| 规范文档 | 命名、主题页、SVG、笔记与部署规范 | [打开](./docs/PROJECT_NAMING.md) |

## 建议阅读顺序

| 场景 | 建议从这里开始 | 说明 |
|---|---|---|
| 想先补 MCU 基础 | [MCU Basics](./content/technology-introduction/mcu-basics/README.md) | 适合从 `GPIO`、项目结构、后续 `PWM / Interrupts / Timers` 逐步展开 |
| 想看波形与时序 | [Signals](./content/technology-introduction/signals/README.md) | 当前已开始整理 `PWM` 这类主题 |
| 想查器件引脚和参数 | [器件原理](./content/device-principles/README.md) | 适合快速进入具体器件页 |
| 想了解仓库规则 | [规范文档](./docs/PROJECT_NAMING.md) | 适合准备继续补文档或配图时先看 |

## 当前内容

### 技术主线

| 分类 | 当前状态 | 文档 |
|---|---|---|
| MCU Basics | 已开始整理 | [打开](./content/technology-introduction/mcu-basics/README.md) |
| Signals | 已开始整理 | [打开](./content/technology-introduction/signals/README.md) |
| Interfaces | 预留目录 | [打开](./content/technology-introduction/interfaces/README.md) |
| Analog | 预留目录 | [打开](./content/technology-introduction/analog/README.md) |
| Power | 预留目录 | [打开](./content/technology-introduction/power/README.md) |
| Design Notes | 预留目录 | [打开](./content/technology-introduction/design-notes/README.md) |

### 器件主线

| 分类 | 已收录示例 | 文档 |
|---|---|---|
| Timers | `NE555P` | [打开](./content/device-principles/timers/README.md) |
| Actuators | `SG90 Servo` | [打开](./content/device-principles/actuators/README.md) |
| Passive | 铝电解电容、陶瓷电容 | [打开](./content/device-principles/passive/README.md) |
| Opto | `5mm Round LED` | [打开](./content/device-principles/opto/README.md) |
| Transistors | `S9013` | [打开](./content/device-principles/transistors/README.md) |
| Logic | `CD4069` | [打开](./content/device-principles/logic/README.md) |
| Relays | `HK4100F / HK4101F` | [打开](./content/device-principles/relays/README.md) |
| Microphones | `VS9767S32 (CZN-15E)` | [打开](./content/device-principles/microphones/README.md) |
| Speakers | `GSPK2805TN-8R1.5W` | [打开](./content/device-principles/speakers/README.md) |

## 近期推荐入口

| 内容 | 类型 | 说明 | 文档 |
|---|---|---|---|
| GPIO | 技术主题页 | MCU 引脚结构、模式与项目对应关系 | [打开](./content/technology-introduction/mcu-basics/gpio/README.md) |
| GPIO 基础笔记 | 学习笔记 | 对 GPIO 结构和模式做更完整展开 | [打开](./content/technology-introduction/mcu-basics/02-gpio-basics.md) |
| PWM | 技术主题页 | 用 `1 MHz -> 2000 Hz` 例子说明周期、频率和占空比 | [打开](./content/technology-introduction/signals/pwm/README.md) |
| NE555P | 器件页 | 引脚图、参数和使用说明 | [打开](./content/device-principles/timers/ne555p/README.md) |
| SG90 Servo | 器件页 | 三线接法、控制脉宽与常见参数整理 | [打开](./content/device-principles/actuators/sg90-servo/README.md) |

## 仓库结构

```text
embedded-handbook/
├─ README.md
├─ content/
│  ├─ device-principles/        # 器件原理 / 器件说明
│  └─ technology-introduction/  # 技术介绍
├─ docs/                        # 命名、绘图、主题页、部署规范
├─ templates/                   # 模板与后续复用结构
└─ .nojekyll
```

## 维护原则

| 原则 | 说明 |
|---|---|
| 内容优先 | 先把资料和结构整理清楚，再考虑复杂前端 |
| 两条主线 | 技术主题与器件资料分开管理 |
| 相对路径 | 方便本地查阅与 GitHub Pages 发布 |
| 图文配合 | 器件和技术主题都尽量配表格与示意图 |
| 规范统一 | 后续新增文档和 SVG 按 `docs/` 中规范执行 |

## 规范与部署

| 类型 | 说明 | 文档 |
|---|---|---|
| 项目命名 | 仓库名、站点标题与对外描述 | [PROJECT_NAMING.md](./docs/PROJECT_NAMING.md) |
| GitHub Pages | 后续部署路线与建议 | [GITHUB_PAGES_DEPLOY.md](./docs/GITHUB_PAGES_DEPLOY.md) |
| 技术主题页 | `GPIO / PWM / I2C / SPI` 这类页面写法 | [TECH_TOPIC_STYLE.md](./docs/TECH_TOPIC_STYLE.md) |
| SVG 绘制 | 器件图与技术主题图的绘制规范 | [drawing-standard.md](./docs/drawing-standard.md) |
| 笔记风格 | 学习笔记、项目说明与阅读记录格式 | [NOTE_STYLE.md](./docs/NOTE_STYLE.md) |
| 资料来源 | 常用资料站点与整理方式 | [sources.md](./docs/sources.md) |

## Hub Entry

This knowledge project is managed through the workspace hub:

D:\workspace\workspace-hub\projects\embedded-device-notes\README.md

Use the hub view as the workspace-level entry for related projects, references, and future cross-project links.
