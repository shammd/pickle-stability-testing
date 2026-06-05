# Person 1 – Python Version Testing

## Environment

- Python 3.12
- Python 3.13
- Python 3.14
- Windows

## Objective
Determine whether the same object produces identical pickle output across different Python versions.

## Results
| Python Version | Hash |
|---------------|------|
| 3.12 | 8e43502463b1b94aac0e1d1bc761e4391b100230e8d00d229216d22535425644 |
| 3.13 | 8e43502463b1b94aac0e1d1bc761e4391b100230e8d00d229216d22535425644 |
| 3.14 | ab8d65928aaaa339fdc4a6962b6160b4e8fee051d123d6e30ded962b2f574468 |

## Analysis

Repeated serializations within each Python version produced identical SHA256 hashes. This means that pickle behaved deterministically when the same object was serialized more than once in the same Python environment.

Python 3.12 and Python 3.13 generated the same hash, which means the pickle byte stream was identical between those two versions. Python 3.14 generated a different hash for the same object. This suggests that the pickle output can change between Python versions, even when the input object stays the same.

## Conclusion
The results show that pickle was stable within each tested Python version, but not fully reproducible across all tested Python versions.