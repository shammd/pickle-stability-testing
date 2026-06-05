# Operating System Comparison Results

## Objective

The goal of this part was to compare pickle output across different operating systems and Python versions.

## Environments

The tests were executed on:

- Windows
- Linux
- macOS

Each operating system was tested with multiple Python versions.

## Evidence

Raw results are stored in:

```text
results/generated/
```

## Executed Test Cases

The operating system comparison included all project test cases:

- Nested dictionaries and lists
- Deeply nested structures
- Recursive lists
- Custom class objects
- Multiple objects of the same class
- Floating point values
- NaN value
- Infinity value
- Set object
- Python version comparison
- Tuple object
- Dictionary insertion order

## Analysis

The results were the same across Windows, Linux, and macOS. For each Python version, the hashes matched between the three operating systems, so we did not find any OS-specific differences in these tests.

There were differences between Python versions. Python 3.12 and 3.13 gave the same hashes, while Python 3.14 produced different hashes for several cases. This is probably because Python 3.14 used pickle default protocol 5, while Python 3.12 and 3.13 used default protocol 4.

The dictionary insertion order test also produced two different hashes on every operating system. This was not caused by the OS. It happened because the two dictionaries had the same keys and values, but were created in a different order.

Things that could affect the results include the Python version, pickle protocol, `PYTHONHASHSEED`, object construction order, and the exact runner environment used by GitHub Actions.
