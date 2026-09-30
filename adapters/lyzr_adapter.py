from .portable_adapter import PortableAdapter
class LyzrAdapter(PortableAdapter):
    framework="lyzr"
    def to_tool_definition(self, tool): return {"name":tool.name,"description":tool.purpose,"input_schema":tool.input_schema}
