"""第 3 周：文件操作工具模块。

覆盖内容：
    - try / except / else / finally 的完整结构
    - 常见异常：FileNotFoundError、PermissionError、UnicodeDecodeError
    - pathlib 处理路径，以及批量重命名
    - logging 记录处理过程，而不是到处 print

这个模块被 demo.py 导入使用，也可以单独运行做一次自检：
    python3 -m week3_filetool.filetools
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

LOGGER = logging.getLogger(__name__)

ALREADY_NUMBERED = re.compile(r"_\d{3}$")


def safe_read(path: str | Path, encoding: str = "utf-8") -> str | None:
    """读取文本文件；出错时返回 None，而不是让程序崩溃。

    参数：
        path: 文件路径，str 或 Path 都行。
        encoding: 编码，中文文件建议 utf-8。

    返回：
        读取到的文本；任何可预期的错误都返回 None。
    """
    target = Path(path)
    try:
        content = target.read_text(encoding=encoding)
    except FileNotFoundError:
        LOGGER.error("文件不存在：%s", target)
        return None
    except IsADirectoryError:
        LOGGER.error("这是一个目录，不是文件：%s", target)
        return None
    except PermissionError:
        LOGGER.error("没有读取权限：%s", target)
        return None
    except UnicodeDecodeError as exc:
        LOGGER.error("编码不是 %s：%s（%s）", encoding, target, exc)
        return None
    else:
        LOGGER.info("读取成功：%s（%d 个字符）", target, len(content))
        return content
    finally:
        # 无论成功失败都会执行，适合放计数、关闭资源等收尾工作
        LOGGER.debug("safe_read 结束：%s", target)


def collect_targets(directory: str | Path, pattern: str = "*.txt") -> list[Path]:
    """列出待重命名文件，自动跳过已经带 _001 这类编号的文件。"""
    base = Path(directory)
    if not base.is_dir():
        raise NotADirectoryError(f"不是目录：{base}")
    return [
        item
        for item in sorted(base.glob(pattern))
        if item.is_file() and not ALREADY_NUMBERED.search(item.stem)
    ]


def batch_rename(
    directory: str | Path,
    pattern: str = "*.txt",
    dry_run: bool = False,
) -> list[tuple[Path, Path]]:
    """把目录里的文件批量改成 name_001.txt 形式。

    已经符合命名规则的文件会被跳过，所以重复执行是安全的（幂等）。

    参数：
        directory: 目标目录。
        pattern: 匹配模式，默认 *.txt。
        dry_run: 为 True 时只返回计划，不真正改磁盘。

    返回：
        [(旧路径, 新路径), ...]
    """
    base = Path(directory)
    targets = collect_targets(base, pattern=pattern)
    renamed: list[tuple[Path, Path]] = []
    for index, source in enumerate(targets, start=1):
        destination = source.with_name(f"{source.stem}_{index:03d}{source.suffix}")
        if destination.exists():
            LOGGER.warning("目标已存在，跳过：%s", destination)
            continue
        if not dry_run:
            source.rename(destination)
        renamed.append((source, destination))
        LOGGER.info(
            "%s %s -> %s",
            "计划" if dry_run else "已重命名",
            source.name,
            destination.name,
        )
    return renamed


def ensure_demo_files(directory: str | Path) -> list[Path]:
    """准备演示目录：清空后创建 a.txt / b.txt / c.txt。"""
    base = Path(directory)
    base.mkdir(parents=True, exist_ok=True)
    for item in base.glob("*.txt"):
        item.unlink()
    created: list[Path] = []
    for name in ("a.txt", "b.txt", "c.txt"):
        target = base / name
        target.write_text(f"{name} 的示例内容\n", encoding="utf-8")
        created.append(target)
    return created


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    demo_dir = Path(__file__).resolve().parent.parent / "data" / "rename_demo"
    ensure_demo_files(demo_dir)
    print(batch_rename(demo_dir))
