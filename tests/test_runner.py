from cloe_agent.cases import EvaluationCase
from cloe_agent.providers import EchoProvider
from cloe_agent.runner import evaluate_case, report_dict, run_cases


def test_evaluate_case_matches_expectations_without_case_sensitivity():
    case = EvaluationCase("greeting", "hello", ("DEMO RESPONSE", "hello"))

    result = evaluate_case(case, EchoProvider())

    assert result.passed
    assert result.missing_expectations == ()
    assert result.response == "Demo response: hello"
    assert result.latency_ms >= 0


def test_evaluate_case_reports_missing_expectations():
    case = EvaluationCase("missing", "hello", ("folder created",))

    result = evaluate_case(case, EchoProvider())

    assert not result.passed
    assert result.missing_expectations == ("folder created",)


def test_report_dict_summarizes_results():
    results = run_cases(
        [
            EvaluationCase("pass", "hello", ("Demo response",)),
            EvaluationCase("fail", "hello", ("folder created",)),
        ],
        EchoProvider(),
    )

    report = report_dict(results)

    assert report["summary"] == {
        "total": 2,
        "passed": 1,
        "failed": 1,
        "pass_rate": 0.5,
    }
    assert [item["case_id"] for item in report["results"]] == ["pass", "fail"]


def test_report_dict_handles_empty_results():
    assert report_dict([])["summary"]["pass_rate"] == 0.0
