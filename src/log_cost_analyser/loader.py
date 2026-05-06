import json
from pathlib import Path

def load_jsonl(filepath: Path) -> list[dict]:
    """Load a JSONL file and return a list of parsed dicts.
    It will skip blank lines and raise json.JSONDecodeError on malformed lines."""

    logs = [] # Create initial empty array that will be returned

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                logs.append(json.loads(line))
    return logs