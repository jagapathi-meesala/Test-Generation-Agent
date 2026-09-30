from adapters.openai_adapter import OpenAIAdapter
from adapters.crewai_adapter import CrewAIAdapter
from adapters.claude_code_adapter import ClaudeCodeAdapter
from adapters.lyzr_adapter import LyzrAdapter
from core.registry import ToolRegistry

def test_framework_boundaries():
 tools=ToolRegistry(); tool=tools.get("generate-test-cases")
 assert OpenAIAdapter().to_tool_definition(tool)["function"]["name"]=="generate_test_cases"
 assert CrewAIAdapter().to_tool_definition(tool)["name"]==tool.name
 assert tool.name in ClaudeCodeAdapter().to_instruction(tool)
 assert LyzrAdapter().to_tool_definition(tool)["name"]==tool.name
