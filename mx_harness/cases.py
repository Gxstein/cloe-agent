"""Load and validate JSON Lines evaluation cases."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    prompt: str
    expected_contains: tuple[str, ...]


def _parse_case(value: Any, line_number: int) -> EvaluationCase:
    if not isinstance(value, dict):
        raise ValueError(f"line {line_number}: each case must be a JSON object")

    case_id = value.get("id")
    prompt = value.get("prompt")
    expected = value.get("expected_contains")

    if not isinstance(case_id, str) or not case_id.strip():
        raise ValueError(f"line {line_number}: 'id' must be a non-empty string")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError(f"line {line_number}: 'prompt' must be a non-empty string")
    if (
        not isinstance(expected, list)
        or not expected
        or any(not isinstance(item, str) or not item.strip() for item in expected)
    ):
        raise ValueError(
            f"line {line_number}: 'expected_contains' must be a non-empty list of strings"
        )

    return EvaluationCase(
        case_id=case_id.strip(),
        prompt=prompt.strip(),
        expected_contains=tuple(item.strip() for item in expected),
    )


def load_cases(path: Path) -> list[EvaluationCase]:
    cases: list[EvaluationCase] = []
    seen_ids: set[str] = set()

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ValueError(f"cannot read case file '{path}': {error}") from error

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"line {line_number}: invalid JSON: {error.msg}") from error
        case = _parse_case(value, line_number)
        if case.case_id in seen_ids:
            raise ValueError(f"line {line_number}: duplicate case id '{case.case_id}'")
        seen_ids.add(case.case_id)
        cases.append(case)

    if not cases:
        raise ValueError(f"case file '{path}' contains no evaluation cases")
    return cases
