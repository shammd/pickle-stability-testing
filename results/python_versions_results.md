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
Repeated serializations within each Python version produced identical hashes.
Python 3.12 and Python 3.13 generated the same hash.
Python 3.14 generated a different hash.

This indicates that pickle was deterministic within each version, but the serialized output wasn't fully reproducible across all tested Python versions.

## Conclusion
The same object can produce different pickle outputs when serialized using different Python versions.