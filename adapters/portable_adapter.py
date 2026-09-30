from typing import Any
from core.agent import TestGenerationAgent

class PortableAdapter:
    """Minimal framework-neutral invocation boundary."""
    def __init__(self, agent: TestGenerationAgent | None = None): self.agent=agent or TestGenerationAgent()
    def invoke(self, request: dict[str,Any]) -> dict[str,Any]:
        action=request.get("action")
        if action=="analyze": return self.agent.analyze(request["source"],request.get("language","python"))
        if action=="generate": return self.agent.generate(request["source"],request.get("language","python"),request.get("max_cases",20),request.get("focus"))
        if action=="validate": return self.agent.validate(request["cases"])
        raise ValueError("unsupported action")
