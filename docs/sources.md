# 常用电子器件资料来源

用于整理器件资料页、寻找 `pinout`、应用图、封装图和参数表。

## 来源优先级

建议固定按这个顺序找资料：

1. 厂家数据手册
2. 厂家官网产品页
3. 教学型器件网站
4. 自绘 SVG

说明：
- 参数、绝对额定值、脚位定义，优先信任数据手册
- 解释型图片、教学图、应用图，可以优先参考教学网站
- 如果网页图片风格不统一，就按规范自绘 SVG

## 1. 厂家数据手册站

适合查：
- `pinout`
- 封装图
- 内部框图
- 绝对额定值
- 推荐工作条件
- 典型应用电路

常用站点：

- TI: https://www.ti.com/
- ST: https://www.st.com/
- Nexperia: https://www.nexperia.com/
- onsemi: https://www.onsemi.com/
- Vishay: https://www.vishay.com/
- Nichicon: https://www.nichicon.com/en-us/
- Murata: https://www.murata.com/
- Infineon: https://www.infineon.com/
- Diodes Incorporated: https://www.diodes.com/

## 2. 教学型器件网站

适合查：
- 直观 `pinout`
- 极性和外观识别图
- 简化应用图
- 面向初学者的器件说明

常用站点：

- Components101: https://components101.com/
- EEPower: https://eepower.com/
- Build Electronic Circuits: https://www.build-electronic-circuits.com/
- Electronics Notes: https://www.electronics-notes.com/
- All About Circuits: https://www.allaboutcircuits.com/
- Circuit Digest: https://circuitdigest.com/

## 3. 搜索关键词建议

为了更快找到适合资料册的图和说明，建议直接搜：

- `<型号> pinout`
- `<型号> datasheet`
- `<器件类型> polarity`
- `<器件类型> marking`
- `<器件类型> application circuit`
- `<封装名> pinout`

示例：

- `CD4069 pinout`
- `S9013 transistor pinout`
- `5mm LED polarity`
- `ceramic capacitor marking`
- `TO-92 pinout`
- `electrolytic capacitor polarity`

## 4. 资料整理建议

推荐工作流：

1. 用数据手册确认参数和脚位
2. 用教学网站找更直观的解释图
3. 判断是否直接复用图片
4. 不适合直接复用时，再按规范绘制 SVG

## 5. 适合当前资料册的来源类型

最适合当前项目的来源组合：

- 参数和脚位：厂家数据手册
- 示意图和应用图：教学型网站
- 最终统一展示：本地 Markdown + SVG
