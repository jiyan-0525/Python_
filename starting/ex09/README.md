# ft_package

A small sample Python package that provides a helper for counting how many
times an item appears in a list.

## Contents

- `ft_package/__init__.py` — exposes `count_in_list` and `__version__`
- `ft_package/core.py` — implementation of `count_in_list`
- `pyproject.toml` — package metadata and build configuration (PEP 517/621)
- `requirements.txt` — build dependencies
- `test.py` — small usage example
- `LICENSE` — MIT license

## Requirements

- Python 3.6 or newer
- `build` (installed from `requirements.txt`)

## Project structure

```text
ex09/
├── ft_package/
│   ├── __init__.py
│   └── core.py
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
└── test.py
```

## Build

Create and activate a virtual environment, install the build dependency, then
build the distribution archives:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m build
```

This creates both a source archive and a wheel in `dist/`:

```text
dist/ft_package-0.0.1.tar.gz
dist/ft_package-0.0.1-py3-none-any.whl
```

## Installation

Install from the built source archive:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Or install directly from the project directory:

```bash
pip install .
```

## Usage

```python
from ft_package import count_in_list

count_in_list(["toto", "tata", "toto"], "toto")  # 2
count_in_list(["toto", "tata", "toto"], "tutu")  # 0
```

## Test

After installing the package, run the example script:

```bash
python test.py
```

Expected output:

```text
2
0
```

## Uninstall

```bash
pip uninstall ft_package
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.
