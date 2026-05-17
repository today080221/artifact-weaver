# ADR 0001：Python 优先的渲染核心

## 状态

M0 已接受。

## 决策

M0 使用 Python-only、标准库优先的渲染核心。不引入 Node、Bun、Vite、React、Vue、Slidev 或 Playwright。

## 背景

M0 需要先稳定产物契约、CLI、渲染清单、HTML 报告渲染器、文档护栏和执行护栏体系，而不是先进入前端工程。

## 影响

Python 核心不应依赖 Unity、Node、外部服务或私有下游项目。未来可以在后端边界之后添加可选渲染后端，并保持核心契约不变。
