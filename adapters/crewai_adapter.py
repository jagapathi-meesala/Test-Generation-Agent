from .portable_adapter import PortableAdapter
class CrewAIAdapter(PortableAdapter):
    framework="crewai"
    def to_tool_definition(self, tool): return {"name":tool.name,"description":tool.purpose,"args_schema":tool.input_schema}
