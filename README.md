# Pickle Stability Testing

## Project Goal

The goal of this project is to investigate whether Python pickle produces stable and reproducible output across different environments and data structures.

## How to Run

### Run all current tests with metadata

```bash
python utils/run_tests.py
```

This runs the existing test scripts, records environment metadata, and writes
JSON/Markdown output to `results/generated/`.

### Complex structures

```bash
python tests/test_complex_structures.py
```

### Edge cases

```bash
python tests/test_edge_cases.py
```

### Python version tests

```bash
py -3.12 -m uv run --python 3.12 python tests/test_python_versions.py

py -3.12 -m uv run --python 3.13 python tests/test_python_versions.py

py -3.12 -m uv run --python 3.14 python tests/test_python_versions.py
```

## Tested Environments

- Windows
- Linux
- macOS
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

## Test Categories

- Complex structures
- Recursive data structures
- Custom class objects
- Floating point values
- NaN values
- Infinity values
- Sets
- Tuples
- Dictionary insertion order
- Python version comparison

## Metrics

The project compares:

- SHA256 hashes of serialized pickle data
- Round-trip correctness after unpickling
