from contracts.tool_contract import ToolContract

class AdapterRegistry:
    def __init__(self): self._adapters={}
    def register(self,name,adapter):
        if not name or name in self._adapters: raise ValueError("adapter name must be unique and non-empty")
        self._adapters[name]=adapter
    def get(self,name): return self._adapters[name]
    def names(self): return tuple(sorted(self._adapters))
