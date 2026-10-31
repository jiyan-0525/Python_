# Python 自动化学习路线（按周计划）

> 目标：从零基础逐步过渡到能独立编写可靠的自动化脚本，最终完成一个「定时抓取 API → 清洗数据 → 导出 Excel → 发送通知/记录日志」的完整项目。
> 建议投入：每周 8–10 小时（工作日每天 1 小时 + 周末 2–3 小时）。

---

## 阶段总览

| 周次 | 主题 | 核心产出 |
| --- | --- | --- |
| 第 1–2 周 | Python 基础语法与数据结构 | 若干基础练习脚本 |
| 第 3 周 | 文件、异常、模块与环境管理 | 可复用的文件处理小工具 |
| 第 4 周 | 网络请求与 API 调用 | 能调用公开 API 并保存 JSON |
| 第 5–6 周 | 综合自动化项目 | 完整可运行的自动化流水线 |
| 第 7 周 | 数据处理与测试 | pandas 分析 + pytest 测试 |
| 第 8 周 | 工程化与交付 | 类型注解、Git、命令行参数、部署 |

---

## 第 1 周：Python 基础语法与数据结构

**本周目标**：能读懂并写出包含变量、条件、循环、列表、字典、函数的脚本。

**知识点**
- 变量、数据类型（int / float / str / bool）
- 运算符与字符串格式化（f-string）
- 条件语句 `if / elif / else`
- 循环 `for`、`while`，`range()`、`enumerate()`、`zip()`
- 列表、元组、字典、集合的常用操作
- 函数定义、参数、返回值、默认参数

**练习 / 项目任务**
1. 写一个温度转换器（摄氏度 ↔ 华氏度）。
2. 统计一段文本中每个单词出现的次数（`dict`）。
3. 写函数判断一个数是否为质数，并输出 100 以内的所有质数。
4. 用列表推导式生成 1–100 中所有偶数的平方。

**产出物**
- `week1_basics.py`：包含以上练习的可运行脚本。

**自检标准**
- 能解释可变类型与不可变类型的区别。
- 能不查资料写出一个带默认参数的函数。

---

## 第 2 周：文件读写与函数进阶

**本周目标**：掌握文本/CSV/JSON 文件读写，并能组织多函数脚本。

**知识点**
- `open()`、`with` 上下文管理器、编码 `utf-8`
- 读取/写入文本文件（`read`、`readlines`、`write`）
- `csv` 模块：`csv.reader` / `csv.writer` / `DictReader` / `DictWriter`
- `json` 模块：`json.load` / `json.dump`
- 函数进阶：`*args`、`**kwargs`、作用域、lambda、sorted 的 key 参数
- 列表推导式、字典推导式

**练习 / 项目任务**
1. 读取 `input.csv`，按某一列排序后写入 `output.csv`。
2. 把 CSV 转成 JSON，再把 JSON 转回 CSV。
3. 写一个 `word_count(path)` 函数，返回出现频率最高的 10 个单词。

**产出物**
- `week2_files.py`
- `data/` 目录下的示例输入输出文件。

**自检标准**
- 能解释 `with open(...)` 相比手动 `close()` 的好处。
- 能处理带中文的 CSV 文件而不乱码。

---

## 第 3 周：异常处理、路径操作与模块化

**本周目标**：写出健壮的文件处理工具，并能用虚拟环境管理依赖。

**知识点**
- `try / except / else / finally`、常见异常类型
- 自定义异常、`raise`
- `pathlib.Path`：路径拼接、遍历、创建目录
- `os.path` 与 `pathlib` 的对比
- 模块与包、`if __name__ == "__main__"`
- 虚拟环境 `venv`、`pip install`、`requirements.txt`

**练习 / 项目任务**
1. 写一个批量重命名脚本：把目录下所有 `.txt` 文件按 `name_001.txt` 规则重命名，并跳过已处理的文件。
2. 写一个 `safe_read(path)`，文件不存在或编码错误时返回友好提示而不是崩溃。
3. 创建虚拟环境，安装 `requests`，生成 `requirements.txt`。

**产出物**
- `week3_filetool/` 包目录（含 `__init__.py`、工具函数、示例）。
- `requirements.txt`

**自检标准**
- 能区分 `FileNotFoundError`、`PermissionError`、`UnicodeDecodeError`。
- 能在新环境中根据 `requirements.txt` 还原依赖。

---

## 第 4 周：网络请求与 API 调用

**本周目标**：能用 `requests` 调用公开 API，处理 JSON 响应并保存结果。

**知识点**
- HTTP 基础：GET/POST、状态码、请求头、查询参数
- `requests.get()`、`params`、`headers`、`timeout`
- 响应处理：`response.status_code`、`response.json()`
- 分页请求与限流（`time.sleep`、退避重试）
- API Key 的安全管理（环境变量 `os.environ`）
- 基础错误处理与日志 `logging`

**练习 / 项目任务**
1. 调用一个公开 API（如天气、汇率、GitHub 用户），打印关键字段。
2. 读取环境变量中的 API Key，不把密钥写进代码。
3. 把返回结果保存为带时间戳的 JSON 文件。
4. 加入重试逻辑：请求失败时最多重试 3 次。

**产出物**
- `week4_api.py`
- `.env.example`（示例配置，不含真实密钥）
- `logs/` 目录下的一次运行日志

**自检标准**
- 能解释为什么不能把 API Key 提交到 Git。
- 能区分 4xx 与 5xx 错误并给出不同处理策略。

---

## 第 5–6 周：综合自动化项目

**本周目标**：独立完成一个端到端自动化项目，并拆分成可维护的模块。

**项目流程**
```
定时触发
  → 调用公开 API（带重试与超时）
  → 清洗/筛选数据
  → 写入 Excel（或 CSV）
  → 发送邮件通知 / 记录运行日志
  → 异常时告警并保留现场数据
```

**知识点**
- 项目结构划分：`config`、`fetch`、`clean`、`export`、`notify`
- `openpyxl` 或 `pandas.to_excel` 写 Excel
- `smtplib` + `email` 发送邮件（或用 webhook 通知）
- 配置文件管理（`config.json` / `.env`）
- 日志分级与文件轮转（`logging.handlers`）
- 定时运行：`cron` 或 `schedule` 库

**任务拆解**
1. 设计目录结构与配置文件。
2. 实现 `fetch_data()`：调用 API，失败重试，返回结构化数据。
3. 实现 `clean_data()`：去重、过滤、字段转换。
4. 实现 `export_excel()`：写入带日期的工作表，避免覆盖历史数据。
5. 实现 `notify()`：发送成功/失败邮件或 webhook。
6. 串联主流程 `main.py`，加入日志与异常兜底。
7. 配置定时任务并连续运行 3 天验证稳定性。

**产出物**
- 完整项目目录 `auto_project/`
- `README.md`：运行方式、配置说明
- 连续 3 天的运行日志与至少 3 份输出 Excel

**自检标准**
- API 挂掉或超时时，脚本不会崩溃且会留下告警。
- 每次运行产物可追溯（文件名含时间戳，日志含请求耗时）。

---

## 第 7 周：数据处理与测试

**本周目标**：用 pandas 做数据分析，并用 pytest 为核心函数写测试。

**知识点**
- pandas：`DataFrame`、`read_csv`、筛选、分组 `groupby`、聚合
- 数据清洗：缺失值、类型转换、去重
- pytest：`assert`、测试函数命名、`fixture`、参数化
- `unittest.mock` 模拟网络请求
- 覆盖率工具 `pytest-cov`

**练习 / 项目任务**
1. 用 pandas 读取一周的抓取数据，输出每日汇总报表。
2. 为 `clean_data()` 和 `export_excel()` 编写单元测试。
3. 用 mock 模拟 API 返回，测试 `fetch_data()` 的重试逻辑。
4. 运行覆盖率报告，核心逻辑覆盖率 ≥ 70%。

**产出物**
- `tests/` 目录
- `report_weekly.xlsx` 或汇总图表
- 覆盖率报告

**自检标准**
- 测试不依赖真实网络即可运行。
- 能解释为什么测试要覆盖失败路径。

---

## 第 8 周：工程化与交付

**本周目标**：让项目达到「可交接、可维护、可部署」的水平。

**知识点**
- 类型注解（`typing`）、`mypy` 基础检查
- `argparse` 或 `click` 编写命令行参数
- Git 基础：分支、提交规范、`.gitignore`
- 代码格式化：`black`、`ruff`
- 部署方式：服务器 `cron`、Docker 基础、GitHub Actions 定时任务

**任务拆解**
1. 为公开函数加类型注解并跑 `mypy`。
2. 用 `argparse` 支持 `--date`、`--dry-run` 等参数。
3. 整理 Git 历史，添加 `.gitignore`（排除 `.env`、日志、输出文件）。
4. 用 `ruff`/`black` 统一代码风格。
5. 选择一种方式部署并验证定时运行。

**产出物**
- 带类型注解与 CLI 的最终版本
- 规范化的 Git 仓库
- 一份部署说明（`DEPLOY.md`）

**自检标准**
- 他人按 README 可在 15 分钟内跑通项目。
- 敏感信息未进入版本库。

---

## 学习建议

- **每天动手**：看 30 分钟、写 30 分钟，比只看不写有效得多。
- **小步提交**：每个练习完成即用 Git 提交，保留成长轨迹。
- **遇到报错先读栈**：从最后一行往前看，定位自己的代码行。
- **善用官方文档**：Python 官方文档、`requests`、`pandas`、`pytest` 文档优先。
- **每周复盘**：记录「学会了什么 / 卡在哪里 / 下周重点」。

---

## 推荐资源

- Python 官方教程：https://docs.python.org/zh-cn/3/tutorial/
- Requests 文档：https://requests.readthedocs.io/
- pandas 文档：https://pandas.pydata.org/docs/
- pytest 文档：https://docs.pytest.org/
- Real Python 教程：https://realpython.com/
