from contracts.tool_contract import ToolContract, ContractError
from core.agent import TestGenerationAgent
from contracts.schemas import ANALYZE_INPUT,GENERATE_INPUT,VALIDATE_INPUT


def _require(payload, keys):
    missing=[k for k in keys if k not in payload]
    if missing: raise ContractError("missing required fields: "+", ".join(missing))
    if payload.get("language","python")!="python": raise ContractError("only language=python is supported")


def build_registry():
    agent=TestGenerationAgent(); r={}
    r["analyze-code"]=ToolContract("analyze-code","Analyze Python function structure.",ANALYZE_INPUT,{"type":"object"},lambda p:_require(p,["source","language"]),lambda p:agent.analyze(p["source"],p["language"]))
    r["generate-test-cases"]=ToolContract("generate-test-cases","Generate deterministic structured test cases.",GENERATE_INPUT,{"type":"object"},lambda p:_require(p,["source","language"]),lambda p:agent.generate(p["source"],p["language"],p.get("max_cases",20),p.get("focus")))
    r["validate-test-cases"]=ToolContract("validate-test-cases","Validate generated test case structures.",VALIDATE_INPUT,{"type":"object"},lambda p:_require(p,["cases"]),lambda p:agent.validate(p["cases"]))
    return r

class ToolRegistry:
    def __init__(self): self._tools=build_registry()
    def names(self): return tuple(sorted(self._tools))
    def get(self,name): return self._tools[name]
    def execute(self,name,payload): return self.get(name).execute(payload)
