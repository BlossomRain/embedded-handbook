# GitHub Pages 部署说明

本文用于说明当前仓库后续发布到 GitHub Pages 的建议方式。

当前项目还处于以 Markdown 为主的整理阶段，所以部署策略优先考虑：

- 结构稳定
- 可逐步演进
- 先能上线，再考虑更复杂的站点框架

## 1. 当前项目情况

当前仓库已经具备适合静态发布的基本条件：

| 项目 | 当前状态 | 说明 |
|---|---|---|
| 主内容 | Markdown | 适合继续沉淀目录和文档结构 |
| 图片资源 | 相对路径引用 | 有利于本地查看和线上部署 |
| 目录结构 | 已分 `content/` 与 `docs/` | 便于后续继续扩展 |
| 图示资源 | 本地 `SVG / PNG` | 可直接作为静态资源发布 |

## 2. 推荐发布路线

当前推荐采用“两阶段路线”。

### 2.1 第一阶段

先继续维护当前仓库结构，不急着引入复杂前端框架。

目标：

- 把首页、目录页、主题页、器件页内容补齐
- 保持全部资源都使用相对路径
- 让仓库本身已经具备“可读手册”的结构

### 2.2 第二阶段

内容积累到一定程度后，再选择正式的站点生成方式。

推荐优先级：

1. `MkDocs`
2. `VitePress`
3. GitHub Pages 直接发布静态目录

当前最稳妥的建议是：

- 先完成内容沉淀
- 再接 `MkDocs` 或 `VitePress`
- 最后通过 GitHub Actions 发布到 GitHub Pages

## 3. 为什么不建议现在直接硬上复杂前端

原因很简单：

- 当前最重要的是把内容结构做稳
- 目录、命名、图片规范还在继续完善
- 如果太早绑定前端框架，后续容易为了站点结构反过来迁就内容

所以当前原则是：

- 内容优先
- Markdown 优先
- 部署方式后置

## 4. GitHub Pages 建议方案

结合 GitHub 官方当前支持方式，后续建议优先使用：

- GitHub Actions 发布 Pages

而不是一开始就依赖旧式“固定分支目录”思路。

原因：

- 更灵活
- 后续切换到 `MkDocs`、`VitePress` 更顺
- 发布产物和源文件可分离

## 5. 建议的未来目录演进

如果后续接入静态站点生成器，建议保留当前内容目录不变，只额外补一个站点目录或配置文件。

例如：

```text
embedded-handbook/
├─ README.md
├─ content/
├─ docs/
├─ templates/
├─ site/                  # 可选，生成后的静态文件目录
├─ mkdocs.yml             # 如果选 MkDocs
└─ .github/
   └─ workflows/
      └─ deploy-pages.yml
```

这样可以保证：

- 内容文件不需要大迁移
- 主题页路径关系尽量稳定
- 本地查阅和在线查阅都能兼容

## 6. 当前阶段必须遵守的约束

为了以后顺利上线 GitHub Pages，当前写内容时建议继续保持：

1. 所有图片和文档都使用相对路径
2. 不依赖本地绝对路径
3. 不把资料只放在 IDE 可见、网页不可见的位置
4. Markdown 页尽量都有清晰标题和目录入口
5. 自绘 SVG 尽量用稳定画布尺寸和统一版式

## 7. 后续真正部署时的执行步骤

建议按下面顺序推进：

1. 先确定仓库名为 `embedded-handbook`
2. 补齐首页和主要分类页入口
3. 选定最终站点方案：`MkDocs` 或 `VitePress`
4. 增加 GitHub Pages 工作流
5. 在仓库设置里启用 GitHub Pages
6. 验证首页、图片、相对路径和目录跳转

## 8. 当前建议结论

对这个项目，当前最合适的结论是：

- 现在先不急着做复杂网站
- 继续按 Markdown 手册方式完善内容
- 仓库名固定为 `embedded-handbook`
- 后续上线时优先使用 GitHub Actions 发布 GitHub Pages

## 9. 参考资料

以下为 GitHub 官方文档：

- GitHub Pages 创建站点：
  https://docs.github.com/pages/getting-started-with-github-pages/creating-a-github-pages-site
- GitHub Pages 配置发布源：
  https://docs.github.com/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- 使用自定义 GitHub Actions 工作流部署 Pages：
  https://docs.github.com/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
