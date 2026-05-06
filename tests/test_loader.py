from pathlib import Path

from log_cost_analyser.loader import load_jsonl

FIXTURES = Path(__file__).parent / "fixtures"

# Test the amount lof log "items" in logs, and that all log items are dicts
def test_load_jsonl_returns_list_of_dicts():
    logs = load_jsonl(FIXTURES / "clean_logs.jsonl")
    assert len(logs) == 5
    assert all(isinstance(log, dict) for log in logs)

def test_load_jsonl_preserves_fields():
    logs = load_jsonl(FIXTURES / "clean_logs.jsonl")
    assert logs[0]["service"] == "auth-service"
    assert logs[1]["severity"] == "ERROR"