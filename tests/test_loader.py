from pathlib import Path

from log_cost_analyser.loader import load_jsonl, load_directory

FIXTURES = Path(__file__).parent / "fixtures"

# Test the amount lof log "items" in logs, and that all log items are dicts
def test_load_jsonl_returns_list_of_dicts():
    logs = load_jsonl(FIXTURES / "clean_logs.jsonl")
    assert len(logs) == 5
    assert all(isinstance(log, dict) for log in logs)

#All fields are loaded in as they should
def test_load_jsonl_preserves_fields():
    logs = load_jsonl(FIXTURES / "clean_logs.jsonl")
    assert logs[0]["service"] == "auth-service"
    assert logs[1]["severity"] == "ERROR"

def test_load_jsonl_skips_blank_lines():
    logs = load_jsonl(FIXTURES / "messy_logs.jsonl")
    # Should be 2 valid lines
    assert len(logs) == 2

def test_load_directory_loads_multiple_paths(tmp_path):
    file1 = tmp_path / "a.jsonl"
    file2 = tmp_path / "b.jsonl"
    file1.write_text('{"service": "api", "message": "from file 1"}\n')
    file2.write_text('{"service": "worker", "message": "from file 2"}\n')

    logs = load_directory(tmp_path)
    assert len(logs) == 2
    assert logs[0]["service"] == "api"
    assert logs[1]["service"] == "worker"