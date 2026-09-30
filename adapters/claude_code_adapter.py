from .portable_adapter import PortableAdapter
class ClaudeCodeAdapter(PortableAdapter):
    framework="claude-code"
    def to_instruction(self, tool): return f"Tool: {tool.name}\nPurpose: {tool.purpose}\nInput schema: {tool.input_schema}"
