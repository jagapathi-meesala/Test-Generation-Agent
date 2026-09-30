from dataclasses import dataclass
from typing import Any, Callable


class ContractError(ValueError):
    """Raised when tool input or output violates a contract."""


@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: dict[str, Any]
    output_schema: dict[str, Any]
    validator: Callable[[dict[str, Any]], None]
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def validate_input(self, payload: dict[str, Any]) -> None:
        if not isinstance(payload, dict):
            raise ContractError("tool input must be an object")
        self.validator(payload)

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.validate_input(payload)
        result = self.executor(payload)
        if not isinstance(result, dict):
            raise ContractError("tool output must be an object")
        return result
