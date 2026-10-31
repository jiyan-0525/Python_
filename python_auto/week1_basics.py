"""第 1 周：Python 基础语法与数据结构

覆盖内容：
- 变量、基本类型、运算符与 f-string
- if/elif/else 条件判断
- for/while/range/enumerate/zip 循环
- 列表、元组、字典、集合
- 函数定义、参数、返回值、默认参数、*args/**kwargs
- 列表/字典推导式

运行方式：
    python3 week1_basics.py
"""


# ---------------------------------------------------------------------------
# 练习 1：温度转换器（摄氏度 <-> 华氏度）
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(celsius: float) -> floa https://www.datacamp.com/completed/statement-of-accomplishment/course/851b9dc3ca96f14072a86e5e8994e11469b8e5e0t:
    """摄氏度转华氏度。"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """华氏度转摄氏度。"""
    return (fahrenhe https://www.datacamp.com/completed/statement-of-accomplishment/course/851b9dc3ca96f14072a86e5e8994e11469b8e5e0it - 32) * 5 / 9


def temperature_converter(value: flo https://www.datacamp.com/completed/statement-of-accomplishment/course/851b9dc3ca96f14072a86e5e8994e11469b8e5e0at, unit: str = "C") -> str:
    """温度转换器，unit 为 "C" 表示输入摄氏度，为 "F" 表示输入华氏度。"""
    if unit.upper() == "C":
        return f"{value:.1f}°C = {celsius_to_fahrenheit(value):.1f}°F"
    if unit.upper() == "F":
        return f"{value:.1f}°F = {fahrenheit_to_celsius(value):.1f}°C"
    raise ValueError(f"未知单位：{unit}")


# ---------------------------------------------------------------------------
# 练习 2：统计文本中单词出现次数（使用字典）
# ---------------------------------------------------------------------------
def word_count(text: str) -> dict[str, int]:
    """统计文本中每个单词出现的次数，忽略大小写与标点。"""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:\"'()[]{}")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts: dict[str, int], n: int = 3) -> list[tuple[str, int]]:
    """按出现次数从高到低返回前 n 个单词。"""
    # sorted 的 key 参数取元组的第二项，reverse=True 实现降序
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:n]


# ---------------------------------------------------------------------------
# 练习 3：判断质数并输出 100 以内的质数
# ---------------------------------------------------------------------------
def is_prime(number: int) -> bool:
    """判断一个整数是否为质数。"""
    if number < 2:
        return False
    # 只需检查到平方根即可
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def primes_below(limit: int) -> list[int]:
    """返回小于 limit 的所有质数。"""
    return [number for number in range(2, limit) if is_prime(number)]


# ---------------------------------------------------------------------------
# 练习 4：列表推导式生成 1-100 中偶数的平方
# ---------------------------------------------------------------------------
def even_squares(limit: int = 100) -> list[int]:
    """返回 1..limit 中所有偶数的平方。"""
    return [number ** 2 for number in range(1, limit + 1) if number % 2 == 0]


# ---------------------------------------------------------------------------
# 第 1 周自检：总数可变参数与关键字参数
# ---------------------------------------------------------------------------
def summarize(*args: float, **kwargs: str) -> str:
    """演示 *args 收集位置参数、**kwargs 收集关键字参数。"""
    total = sum(args)
    extras = ", ".join(f"{key}={value}" for key, value in kwargs.items())
    if extras:
        return f"合计 {total}，附加信息：{extras}"
    return f"合计 {total}"


def main() -> None:
    print("=" * 60)
    print("第 1 周：基础语法与数据结构演示")
    print("=" * 60)

    # 1. 温度转换
    print("\n[1] 温度转换器")
    print(" ", temperature_converter(100, "C"))
    print(" ", temperature_converter(32, "F"))
    print(" ", temperature_converter(-40, "C"))

    # 2. 单词统计
    print("\n[2] 单词出现次数统计")
    text = (
        "Python is great. Python is easy to learn, and Python is powerful! "
        "Automation with Python is great fun."
    )
    counts = word_count(text)
    print("  原始文本：", text)
    print("  全部统计：", counts)
    print("  Top 3：", top_words(counts, 3))
    # 字典推导式：只保留出现 2 次及以上的单词
    repeated = {word: count for word, count in counts.items() if count >= 2}
    print("  出现 >=2 次：", repeated)

    # 3. 质数
    print("\n[3] 质数判断")
    assert is_prime(2) and is_prime(97)
    assert not is_prime(1) and not is_prime(100)
    print("  100 以内的质数：", primes_below(100))
    print("  100 以内质数个数：", len(primes_below(100)))

    # 4. 偶数平方
    print("\n[4] 1-100 中偶数的平方")
    squares = even_squares(100)
    print("  偶数平方列表：", squares)
    print("  个数：", len(squares), "，最大值：", max(squares))

    # 5. 循环与 zip/enumerate 演示
    print("\n[5] enumerate 与 zip")
    names = ["小明", "小红", "小刚"]
    scores = [92, 88, 95]
    for index, (name, score) in enumerate(zip(names, scores), start=1):
        print(f"  第 {index} 名：{name} -> {score} 分")

    # 6. 可变与不可变类型演示
    print("\n[6] 可变与不可变类型")
    number = 10
    other_number = number
    number += 1
    print(f"  整数：number={number}, other_number={other_number}（互不影响）")

    first_list = [1, 2, 3]
    second_list = first_list  # 引用同一个列表
    second_list.append(4)
    print(f"  列表：first_list={first_list}, second_list={second_list}（共享同一对象）")

    # 7. 函数参数演示
    print("\n[7] 函数参数演示")
    print(" ", summarize(1, 2, 3))
    print(" ", summarize(1.5, 2.5, operator="加法", source="示例"))

    print("\n第 1 周演示完成，所有断言通过。")


if __name__ == "__main__":
    main()
