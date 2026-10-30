"""Run cases and evaluate simple response expectations."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from time import perf_counter

from .cases import EvaluationCase
from .providers import Provider


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    passed: bool
    response: str
    latency_ms: float
    missing_expectations: tuple[str, ...]


def evaluate_case(case: EvaluationCase, provider: Provider) -> CaseResult:
    started = perf_counter()
    response = provider.generate(case.prompt)
    latency_ms = (perf_counter() - started) * 1000
    normalized_response = response.casefold()
    missing = tuple(
        expected
        for expected in case.expected_contains
        if expected.casefold() not in normalized_response
    )
    return CaseResult(
        case_id=case.case_id,
        passed=not missing,
        response=response,
        latency_ms=round(latency_ms, 3),
        missing_expectations=missing,
    )


def run_cases(cases: list[EvaluationCase], provider: Provider) -> list[CaseResult]:
    return [evaluate_case(case, provider) for case in cases]


def report_dict(results: list[CaseResult]) -> dict[str, object]:
    passed = sum(result.passed for result in results)
    return {
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": len(results) - passed,
            "pass_rate": round(passed / len(results), 4) if results else 0.0,
        },
        "results": [asdict(result) for result in results],
    }
