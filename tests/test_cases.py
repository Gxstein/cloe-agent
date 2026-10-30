import json

import pytest

from cloe_agent.cases import load_cases


def test_load_cases_trims_fields_and_preserves_expectations(tmp_path):
    case_file = tmp_path / "cases.jsonl"
    case_file.write_text(
        json.dumps(
            {
                "id": "  create-folder  ",
                "prompt": "  create a folder  ",
                "expected_contains": ["  Demo response  "],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    cases = load_cases(case_file)

    assert len(cases) == 1
    assert cases[0].case_id == "create-folder"
    assert cases[0].prompt == "create a folder"
    assert cases[0].expected_contains == ("Demo response",)


@pytest.mark.parametrize(
    ("content", "message"),
    [
        ("not-json\n", "line 1: invalid JSON"),
        ('{"id":"x","prompt":"p","expected_contains":[]}\n', "expected_contains"),
        (
            '{"id":"x","prompt":"p","expected_contains":["ok"]}\n'
            '{"id":"x","prompt":"p","expected_contains":["ok"]}\n',
            "duplicate case id",
        ),
        ("\n  \n", "contains no evaluation cases"),
    ],
)
def test_load_cases_rejects_invalid_input(tmp_path, content, message):
    case_file = tmp_path / "invalid.jsonl"
    case_file.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        load_cases(case_file)


def test_load_cases_reports_missing_file(tmp_path):
    with pytest.raises(ValueError, match="cannot read case file"):
        load_cases(tmp_path / "missing.jsonl")
