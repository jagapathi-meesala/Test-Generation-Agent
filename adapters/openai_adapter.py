from .portable_adapter import PortableAdapter
class OpenAIAdapter(PortableAdapter):
    framework="openai-sdk"
    def to_tool_definition(self, tool): return {"type":"function","function":{"name":tool.name.replace("-","_"),"description":tool.purpose,"parameters":tool.input_schema}}
