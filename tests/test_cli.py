import json
import sys

from cloe_agent.cli import main


def test_cli_writes_json_report_and_returns_success(tmp_path, monkeypatch, capsys):
    cases = tmp_path / "cases.jsonl"
    cases.write_text(
        json.dumps(
            {"id": "demo", "prompt": "hello", "expected_contains": ["Demo response"]}
        )
        + "\n",
        encoding="utf-8",
    )
    report = tmp_path / "output" / "report.json"
    monkeypatch.setattr(
        sys,
        "argv",
        ["cloe-agent", "run", str(cases), "--output", str(report)],
    )

    exit_code = main()

    assert exit_code == 0
    assert "PASS demo" in capsys.readouterr().out
    assert json.loads(report.read_text(encoding="utf-8"))["summary"]["passed"] == 1


def test_cli_returns_failure_for_failed_expectation(tmp_path, monkeypatch, capsys):
    cases = tmp_path / "cases.jsonl"
    cases.write_text(
        json.dumps(
            {"id": "demo", "prompt": "hello", "expected_contains": ["folder created"]}
        )
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sys, "argv", ["cloe-agent", "run", str(cases)])

    exit_code = main()

    assert exit_code == 1
    assert "FAIL demo" in capsys.readouterr().out
