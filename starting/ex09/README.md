# ft_package

A sample Python package that provides utility functions for list operations.

## Installation

Install directly from the built distribution:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Or install from source:

```bash
pip install .
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

## Functions

### `count_in_list(lst, item)`

Counts the number of occurrences of `item` in the list `lst`.

- **Parameters:**
  - `lst` (`list`): The list to search in.
  - `item`: The element to count.
- **Returns:** `int` — the count of occurrences.

## License

MIT
