"""第 2 周：文件、CSV、JSON 与函数进阶

覆盖内容：
    - open() 与 with 语句、编码与换行符
    - 逐行读取文本、写入文本文件
    - csv 模块：reader / writer / DictReader / DictWriter
    - json 模块：load / dump 与中文编码
    - *args / **kwargs、作用域、lambda 与 sorted(key=)
    - 列表推导式与字典推导式

运行方式：
    python3 week2_files.py
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_ROWS = [
    {"姓名": "张伟", "城市": "北京", "销售额": "1200", "日期": "2026-10-01"},
    {"姓名": "李娜", "城市": "上海", "销售额": "1800", "日期": "2026-10-02"},
    {"姓名": "王强", "城市": "广州", "销售额": "950", "日期": "2026-10-03"},
    {"姓名": "陈杰", "城市": "北京", "销售额": "2100", "日期": "2026-10-04"},
    {"姓名": "刘洋", "城市": "深圳", "销售额": "1500", "日期": "2026-10-05"},
    {"姓名": "赵敏", "城市": "上海", "销售额": "1650", "日期": "2026-10-06"},
    {"姓名": "孙磊", "城市": "杭州", "销售额": "780", "日期": "2026-10-07"},
    {"姓名": "周静", "城市": "成都", "销售额": "1320", "日期": "2026-10-08"},
]

NOTE_TEXT = [
    "Python automation makes daily work easier.",
    "Automation scripts read files, clean data, and call APIs.",
    "With python and a good automation plan, repetitive tasks disappear.",
    "Python automation is not magic, it is pure python practice.",
]


# ---------------------------------------------------------------------------
# 工具函数：准备目录与示例输入
# ---------------------------------------------------------------------------
def ensure_dir(path: Path) -> None:
    """确保目录存在；parents=True 会一并创建缺失的上级目录。"""
    path.mkdir(parents=True, exist_ok=True)


def ensure_input_csv() -> Path:
    """每次运行都重写 data/input.csv，保证演示数据稳定可复现。"""
    ensure_dir(DATA_DIR)
    path = DATA_DIR / "input.csv"
    fieldnames = ["姓名", "城市", "销售额", "日期"]
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(INPUT_ROWS)
    return path


# ---------------------------------------------------------------------------
# 练习 1：with 语句与文本文件读写
# ---------------------------------------------------------------------------
def demo_open_with() -> None:
    """用 with 打开文件，退出时自动关闭，即使中途出错也不会泄漏句柄。"""
    path = DATA_DIR / "open_demo.txt"
    lines = ["第一行：自动化从文件开始。", "第二行：记得使用 utf-8。", "第三行：with 会自动关闭文件。"]

    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")

    with open(path, "r", encoding="utf-8") as handle:
        content = handle.read()

    assert content.splitlines() == lines
    print(f"[练习 1] 写入并读回 {path.name}，共 {len(lines)} 行")


def demo_read_lines() -> None:
    """按行读取：readlines 保留换行符，splitlines 更干净。"""
    path = DATA_DIR / "note.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(NOTE_TEXT) + "\n")

    with open(path, "r", encoding="utf-8") as handle:
        raw_lines = handle.readlines()

    lines = [line.strip() for line in raw_lines]
    assert len(lines) == 4
    print(f"[练习 2] 读取 {path.name}，第 1 行：{lines[0]}")


# ---------------------------------------------------------------------------
# 练习 3：CSV 读取、按列排序并写出
# ---------------------------------------------------------------------------
def demo_csv_sort() -> list[dict[str, str]]:
    """读取 input.csv，按销售额降序写出 output.csv（带排名）。"""
    input_path = DATA_DIR / "input.csv"
    output_path = DATA_DIR / "output.csv"

    with open(input_path, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    rows.sort(key=lambda row: int(row["销售额"]), reverse=True)

    fieldnames = ["排名", "姓名", "城市", "销售额", "日期"]
    with open(output_path, "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            writer.writerow({"排名": index, **row})

    with open(output_path, "r", encoding="utf-8-sig", newline="") as handle:
        written = list(csv.DictReader(handle))

    assert written[0]["排名"] == "1"
    assert written[0]["姓名"] == "陈杰"
    assert written[-1]["姓名"] == "孙磊"
    print(f"[练习 3] 已写出 {output_path.name}，第一名：{written[0]['姓名']} {written[0]['销售额']}")
    return rows


# ---------------------------------------------------------------------------
# 练习 4：CSV 与 JSON 互转
# ---------------------------------------------------------------------------
def demo_csv_json(rows: list[dict[str, str]]) -> None:
    """把排序后的记录写成 JSON，再读回来并还原成 CSV。"""
    json_path = DATA_DIR / "records.json"
    roundtrip_path = DATA_DIR / "roundtrip.csv"

    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)

    with open(json_path, "r", encoding="utf-8") as handle:
        loaded = json.load(handle)

    assert loaded == rows

    fieldnames = ["姓名", "城市", "销售额", "日期"]
    with open(roundtrip_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(loaded)

    with open(roundtrip_path, "r", encoding="utf-8", newline="") as handle:
        back = list(csv.DictReader(handle))

    assert back == rows
    print(f"[练习 4] JSON 往返完成，共 {len(loaded)} 条记录")


# ---------------------------------------------------------------------------
# 练习 5：*args / **kwargs、作用域与 lambda
# ---------------------------------------------------------------------------
MULTIPLIER = 2


def demo_args_kwargs_scope() -> None:
    """演示局部变量与全局变量、可变参数和排序用的 lambda。"""

    def summarize(*args: float, **kwargs: str) -> str:
        total = sum(args)
        labeled = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        return f"合计 {total}（{labeled}）"

    def local_shadow() -> int:
        multiplier = 10
        return multiplier

    message = summarize(1.5, 2.5, 3.0, 单位="小时", 状态="完成")
    pairs = [("b", 2), ("a", 3), ("c", 1)]
    ordered = sorted(pairs, key=lambda item: item[1])

    assert "合计 7.0" in message
    assert MULTIPLIER == 2
    assert local_shadow() == 10
    assert ordered == [("c", 1), ("b", 2), ("a", 3)]
    print(f"[练习 5] {message}；lambda 排序结果：{ordered}")


# ---------------------------------------------------------------------------
# 练习 6：列表推导式与字典推导式
# ---------------------------------------------------------------------------
def demo_comprehensions() -> None:
    """推导式让“生成新集合”的意图更清晰。"""
    squares = [number * number for number in range(1, 11) if number % 2 == 0]
    word_lengths = {word: len(word) for word in ["python", "csv", "json", "自动化"]}

    assert squares == [4, 16, 36, 64, 100]
    assert word_lengths["python"] == 6
    print(f"[练习 6] 偶数平方：{squares}；单词长度：{word_lengths}")


# ---------------------------------------------------------------------------
# 练习 7：统计文本词频并返回 Top 10
# ---------------------------------------------------------------------------
def word_count(path: Path) -> list[tuple[str, int]]:
    """统计文件中单词出现次数，返回按次数降序、同次数按字母升序的前 10 名。"""
    text = path.read_text(encoding="utf-8").lower()
    words = re.findall(r"[a-z']+", text)

    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:10]


def demo_word_count() -> None:
    """对 note.txt 做词频统计，Top 10 结果写入控制台。"""
    path = DATA_DIR / "note.txt"
    top = word_count(path)

    assert top[0][1] == 4
    top_words = {word for word, count in top if count == 4}
    assert top_words == {"automation", "python"}

    print("[练习 7] Top 10 高频词：")
    for rank, (word, count) in enumerate(top, start=1):
        print(f"    {rank:>2}. {word:<12} {count}")


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main() -> None:
    ensure_dir(DATA_DIR)
    ensure_input_csv()

    demo_open_with()
    demo_read_lines()
    sorted_rows = demo_csv_sort()
    demo_csv_json(sorted_rows)
    demo_args_kwargs_scope()
    demo_comprehensions()
    demo_word_count()

    print("第 2 周演示完成，所有断言通过。")


if __name__ == "__main__":
    main()
