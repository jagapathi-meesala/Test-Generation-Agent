from .analyzer import analyze_python
from .generator import generate_python_tests
from .validator import validate_cases

class TestGenerationAgent:
    """Framework-independent deterministic application service."""
    def analyze(self, source: str, language: str = "python") -> dict:
        if language != "python": raise ValueError("only language=python is supported")
        return analyze_python(source)

    def generate(self, source: str, language: str = "python", max_cases: int = 20, focus: str | None = None) -> dict:
        if language != "python": raise ValueError("only language=python is supported")
        return generate_python_tests(source,max_cases,focus)

    def validate(self, cases: list[dict]) -> dict:
        return validate_cases(cases)
