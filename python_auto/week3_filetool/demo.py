"""第 3 周：文件、异常、模块与包演示。

覆盖内容：
    - pathlib 与 os.path 的写法对比
    - safe_read：友好处理缺失文件、目录路径、编码错误
    - try / except / else / finally 的执行顺序
    - batch_rename：批量重命名并保证幂等
    - 模块、包、pip 与 venv 的基本用法

运行方式（在项目根目录执行）：
    python3 -m week3_filetool.demo
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

from .filetools import batch_rename, ensure_demo_files, safe_read

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RENAME_DIR = DATA_DIR / "rename_demo"


def setup_logging() -> None:
    """只显示警告及以上级别，避免演示输出被 INFO 淹没。"""
    logging.basicConfig(
        level=logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )


def setup_demo_environment() -> None:
    """保证演示用文本文件存在，不依赖其他脚本先运行。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    note = DATA_DIR / "note.txt"
    if not note.exists():
        note.write_text("第 3 周演示文本\n第二行\n", encoding="utf-8")


def demo_pathlib() -> None:
    print("\n[练习 1] pathlib 与 os.path")
    sample = DATA_DIR / "note.txt"
    print(f"  Path 拼路径     : {sample}")
    print(f"  os.path 拼路径  : {os.path.join(DATA_DIR, 'note.txt')}")
    print(f"  文件名          : {sample.name}")
    print(f"  后缀            : {sample.suffix}")
    print(f"  父目录名        : {sample.parent.name}")
    print(f"  是否存在        : {sample.exists()}")
    assert sample.name == "note.txt"
    assert sample.suffix == ".txt"
    assert sample.exists()


def demo_safe_read() -> None:
    print("\n[练习 2] safe_read：把异常变成可处理的返回值")
    content = safe_read(DATA_DIR / "note.txt")
    print(f"  正常读取        : {content!r}")
    assert content is not None

    missing = safe_read(DATA_DIR / "不存在.txt")
    print(f"  文件不存在      : {missing!r}")
    assert missing is None

    is_dir = safe_read(DATA_DIR)
    print(f"  传入目录路径    : {is_dir!r}")
    assert is_dir is None

    bad_encoding = safe_read(DATA_DIR / "note.txt", encoding="ascii")
    print(f"  编码用错        : {bad_encoding!r}")
    assert bad_encoding is None


def demo_exception_order() -> None:
    print("\n[练习 3] try / except / else / finally 的执行顺序")
    events: list[str] = []

    def parse(raw: str) -> int:
        try:
            value = int(raw)
        except ValueError:
            events.append("except")
            print("  不是整数，已捕获 ValueError")
            return 0
        else:
            events.append("else")
            print(f"  解析成功：{value}")
            return value
        finally:
            events.append("finally")
            print("  finally 一定执行")

    parse("42")
    assert events == ["else", "finally"]

    events.clear()
    parse("abc")
    assert events == ["except", "finally"]
    print("  结论：成功走 else，失败走 except，finally 永远收尾")


def demo_batch_rename() -> None:
    print("\n[练习 4] 批量重命名（先演练，再执行，再重复执行）")
    ensure_demo_files(RENAME_DIR)

    planned = batch_rename(RENAME_DIR, dry_run=True)
    print(f"  dry_run 计划 {len(planned)} 个文件，磁盘没有改：{sorted(p.name for p in RENAME_DIR.glob('*.txt'))}")
    assert len(planned) == 3
    assert (RENAME_DIR / "a.txt").exists()

    first = batch_rename(RENAME_DIR)
    print(f"  第一次真正重命名 {len(first)} 个文件：")
    for old, new in first:
        print(f"    {old.name} -> {new.name}")
    names = sorted(item.name for item in RENAME_DIR.glob("*.txt"))
    print(f"  目录现在是      : {names}")
    assert names == ["a_001.txt", "b_002.txt", "c_003.txt"]

    second = batch_rename(RENAME_DIR)
    print(f"  第二次重命名 {len(second)} 个文件（幂等，应为 0）")
    assert second == []


def demo_module_notes() -> None:
    print("\n[练习 5] 模块、包与依赖管理")
    print(f"  当前模块 __name__ = {__name__}")
    print("  demo.py 直接运行时 __name__ 是 __main__；被导入时才是 week3_filetool.demo")
    print("  创建虚拟环境：python3 -m venv .venv")
    print("  激活虚拟环境：source .venv/bin/activate")
    print("  安装依赖    ：pip install -r requirements.txt")
    print("  导出依赖    ：pip freeze > requirements.txt")


def main() -> None:
    setup_logging()
    setup_demo_environment()
    demo_pathlib()
    demo_safe_read()
    demo_exception_order()
    demo_batch_rename()
    demo_module_notes()
    print("\n第 3 周演示完成，所有断言通过。")


if __name__ == "__main__":
    main()
