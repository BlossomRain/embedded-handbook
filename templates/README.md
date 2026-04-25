# 模板

用于新增器件时快速复制，保持资料册结构统一。

## 可用模板

| 模板 | 用途 | 路径 |
|---|---|---|
| 标准器件模板 | 适合大多数芯片、模块、分立器件整理 | [打开](./component/README.md) |

配套规范：

- [资料页与 SVG 绘制规范](../docs/drawing-standard.md)

## 新增器件建议步骤

1. 选择合适分类，例如 `timers`、`passive`、`power`
2. 新建器件目录，例如 `content/device-principles/timers/ne555p/`
3. 复制模板中的 `README.md` 和 `images/` 目录结构
4. 下载并放入厂家现成图片
5. 填写 `Pin 图与引脚说明`
6. 填写 `基本参数`
7. 填写 `使用方式`
8. 在对应分类页和首页目录中补充器件入口

## 命名建议

- 目录名用小写英文或型号，例如 `ne555p`、`stm32f103c8t6`
- 图片名简洁明确，例如：
  - `pinout.jpg`
  - `internal-diagram.jpg`
  - `application-example-1.jpg`
