from core.agent import TestGenerationAgent

def test_analyze_and_generate():
 src="def add(a, b):\n    if a > 0:\n        return a+b\n    return b\n"
 a=TestGenerationAgent()
 analysis=a.analyze(src)
 assert analysis["function_count"]==1
 assert analysis["functions"][0]["branch_count"]==1
 result=a.generate(src)
 assert result["count"]>=2
 assert all("provenance" in c for c in result["cases"])

def test_invalid_python():
 try: TestGenerationAgent().analyze("def broken(:")
 except ValueError as e: assert "invalid Python syntax" in str(e)
 else: raise AssertionError("expected ValueError")

def test_unsupported_language():
 try: TestGenerationAgent().generate("x", "javascript")
 except ValueError as e: assert "only language=python" in str(e)
 else: raise AssertionError("expected ValueError")
