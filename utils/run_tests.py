"""Small wrapper for running all the test scripts"""

from __future__ import annotations

import datetime as dt
import json
import os
import pickle
import platform
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "results" / "generated"
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}\b")

TEST_SCRIPTS = [
    "tests/test_complex_structures.py",
    "tests/test_edge_cases.py",
    "tests/test_python_versions.py",
]


def extract_hash_groups(output):
    groups = []
    current_group = None

    for line in output.splitlines():
        text = line.strip()
        if not text:
            continue

        if text.endswith(":") and not SHA256_PATTERN.fullmatch(text):
            current_group = {"name": text[:-1], "hashes": []}
            groups.append(current_group)
            continue

        found_hashes = SHA256_PATTERN.findall(text)
        if found_hashes:
            if current_group is None:
                current_group = {"name": "Unlabeled output", "hashes": []}
                groups.append(current_group)
            current_group["hashes"].extend(found_hashes)

    return groups


def run_script(script_name):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    result = subprocess.run(
        [sys.executable, script_name],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    output = result.stdout + result.stderr
    return {
        "script": script_name,
        "exit_code": result.returncode,
        "hashes": SHA256_PATTERN.findall(output),
        "hash_groups": extract_hash_groups(output),
        "output": output,
    }


def write_markdown_summary(result, path):
    lines = [
        "# Pickle Test Run Summary",
        "",
        "## Environment",
        "",
        f"- OS: {result['environment']['os']}",
        f"- Platform: `{result['environment']['platform']}`",
        f"- Python: `{result['environment']['python']}`",
        f"- Pickle default protocol: {result['environment']['pickle_default_protocol']}",
        f"- PYTHONHASHSEED: `{result['environment']['python_hash_seed']}`",
        "",
        "## Run Summary",
        "",
        "| Script | Completed | Hashes found |",
        "|---|---|---:|",
    ]

    for script_result in result["scripts"]:
        completed = "Yes" if script_result["exit_code"] == 0 else "No"
        lines.append(
            f"| {script_result['script']} | "
            f"{completed} | "
            f"{len(script_result['hashes'])} |"
        )

    lines.extend(["", "## Extracted Hashes", ""])
    for script_result in result["scripts"]:
        lines.append(f"### {script_result['script']}")
        for group in script_result["hash_groups"]:
            lines.append(f"#### {group['name']}")
            for value in group["hashes"]:
                lines.append(f"- `{value}`")
            lines.append("")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    environment = {
        "created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "os": platform.system(),
        "platform": platform.platform(),
        "python": sys.version,
        "python_short": f"{sys.version_info.major}.{sys.version_info.minor}",
        "pickle_default_protocol": pickle.DEFAULT_PROTOCOL,
        "pickle_highest_protocol": pickle.HIGHEST_PROTOCOL,
        "python_hash_seed": os.environ.get("PYTHONHASHSEED", "not set"),
    }

    script_results = [run_script(script) for script in TEST_SCRIPTS]
    result = {
        "environment": environment,
        "scripts": script_results,
    }

    name = (
        f"{environment['os'].lower()}-"
        f"python-{environment['python_short']}-"
        f"seed-{environment['python_hash_seed']}"
    )
    name = re.sub(r"[^a-zA-Z0-9_.-]+", "-", name).strip("-")

    json_path = OUTPUT_DIR / f"{name}.json"
    markdown_path = OUTPUT_DIR / f"{name}.md"

    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_markdown_summary(result, markdown_path)

    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")

    failed_scripts = [
        script["script"] for script in script_results if script["exit_code"] != 0
    ]
    if failed_scripts:
        print("Some scripts failed:", ", ".join(failed_scripts), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
