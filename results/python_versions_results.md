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

Our results show that the `pickle` module works consistently within the same Python version. Every time we serialized the same object, we got the same SHA256 hash.

When comparing different Python versions, Python 3.12 and 3.13 produced the same hash, while Python 3.14 produced a different one. This is likely because of changes made to the `pickle` module between versions.

We also used different development setups during testing. One team member used `uv`, while another used a standard Python installation. Since both setups produced the same hashes, we know that the difference comes from Python 3.14 itself and not from the tools used to manage the environment.

Overall, `pickle` gives reliable results within the same Python version, but the output may change when moving to a newer version.


## Conclusion
The results show that pickle was stable within each tested Python version, but not fully reproducible across all tested Python versions.