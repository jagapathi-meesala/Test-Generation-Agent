import pytest
from core.registry import ToolRegistry
from contracts.tool_contract import ContractError

def test_dynamic_registry():
 r=ToolRegistry()
 assert r.names()==("analyze-code","generate-test-cases","validate-test-cases")
 out=r.execute("analyze-code",{"source":"def f(x): return x","language":"python"})
 assert out["function_count"]==1

def test_registry_rejects_missing_input():
 with pytest.raises(ContractError): ToolRegistry().execute("analyze-code",{"language":"python"})
