"""第 3 周练习包：把文件处理函数拆成可复用的模块。

包内提供两个工具：
    - safe_read：读取文本文件，出错时返回 None 并记录日志
    - batch_rename：批量重命名文件，可重复执行

演示入口：
    python3 -m week3_filetool.demo
"""

from .filetools import batch_rename, ensure_demo_files, safe_read

__all__ = ["safe_read", "batch_rename", "ensure_demo_files"]
