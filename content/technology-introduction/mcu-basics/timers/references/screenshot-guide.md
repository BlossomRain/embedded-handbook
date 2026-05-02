# Timers 截图建议清单

本文用于指导 `STM32F103 Timers` 这一章去哪里截图，以及截图后建议使用什么关键字文件名。

你的工作流可以继续保持很简单：

1. 去官方文档或 ST wiki 截图
2. 先把图片放到仓库根目录 `images/`
3. 文件名里带上这里建议的关键字
4. 我再帮你重命名并移动到正确目录

## 1. 优先截图来源

### 1.1 RM0008

最重要的来源：

- `RM0008 Reference Manual`
- 重点看：
  - `General-purpose timers (TIM2 to TIM5)`
  - `Advanced-control timers (TIM1 and TIM8)`
  - `Basic timers (TIM6 and TIM7)`

适合截：

- 定时器总框图
- 计数时序图
- 输出比较相关图
- 输入捕获相关图

### 1.2 AN4776

适合截：

- 更像教学资料的定时器结构图
- 计数、比较、捕获工作方式图
- PWM、单脉冲、输入捕获等模式示意

### 1.3 ST Wiki

适合截：

- 比较直观的入门图
- 如果 PDF 图过密，可以先截 wiki 里的概念图

## 2. 建议优先截的图片

### 2.1 定时器整体框图

建议关键字文件名：

```text
timer-block
```

建议最终位置：

```text
content/technology-introduction/mcu-basics/timers/images/structure/stm32f103-timer-block-diagram.png
```

这张图最重要，优先级最高。

它应该能看出：

- `TIMxCLK`
- 预分频器
- 计数器
- 自动重装
- 捕获/比较单元
- 输出或触发路径

### 2.2 计数时序图

建议关键字文件名：

```text
timer-counter-timing
```

建议最终位置：

```text
content/technology-introduction/mcu-basics/timers/images/timing/timer-counter-timing.png
```

这张图适合说明：

- `PSC`
- `CNT`
- `ARR`
- 更新事件

### 2.3 PWM 模式图

建议关键字文件名：

```text
pwm-mode
```

建议最终位置：

```text
content/technology-introduction/mcu-basics/timers/images/structure/timer-pwm-mode.png
```

这张图和 `signals/pwm` 那页会互相呼应。

### 2.4 输入捕获图

建议关键字文件名：

```text
input-capture
```

建议最终位置：

```text
content/technology-introduction/mcu-basics/timers/images/timing/timer-input-capture.png
```

重点是能看出：

- 外部边沿到来
- `CNT` 当前值被锁存到 `CCR`

### 2.5 输出比较图

建议关键字文件名：

```text
output-compare
```

建议最终位置：

```text
content/technology-introduction/mcu-basics/timers/images/timing/timer-output-compare.png
```

重点是能看出：

- `CNT == CCR` 时事件发生
- 输出动作或中断如何出现

## 3. 截图建议

### 3.1 优先截“结构清楚”的图

不一定要截最大最全的那一张，优先选：

- 标签清楚
- 没有太多重复路径
- 适合嵌入 Markdown 页面

### 3.2 尽量避免

- 一整页 PDF 全截，字太小
- 太多寄存器位细节挤在一张图里
- 带过多背景阴影或扫描痕迹的图

### 3.3 如果一张图太复杂

建议拆成两张：

- 一张结构图
- 一张时序图

## 4. 放到根目录 images/ 时的建议命名

你先放到仓库根目录 `images/` 时，可以直接这样起名：

- `timer-block.png`
- `timer-counter-timing.png`
- `pwm-mode.png`
- `input-capture.png`
- `output-compare.png`

如果同类图有多个版本，可以加编号：

- `timer-block-1.png`
- `timer-block-2.png`

## 5. 后续我会帮你做什么

等你把图放到根目录 `images/` 后，我会帮你：

1. 检查有没有原理性错误
2. 判断哪张图更适合正文
3. 重命名
4. 移动到 `timers/images/` 下合适目录
5. 更新 Markdown 引用
