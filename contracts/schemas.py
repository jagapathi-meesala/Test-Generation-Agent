TOOL_NAMES = ("analyze-code", "generate-test-cases", "validate-test-cases")

ANALYZE_INPUT = {
    "type": "object",
    "properties": {"source": {"type": "string", "minLength": 1}, "language": {"type": "string", "enum": ["python"]}},
    "required": ["source", "language"],
    "additionalProperties": False,
}

GENERATE_INPUT = {
    "type": "object",
    "properties": {
        "source": {"type": "string", "minLength": 1},
        "language": {"type": "string", "enum": ["python"]},
        "max_cases": {"type": "integer", "minimum": 1, "maximum": 100},
        "focus": {"type": "string", "minLength": 1},
    },
    "required": ["source", "language"],
    "additionalProperties": False,
}

VALIDATE_INPUT = {
    "type": "object",
    "properties": {"cases": {"type": "array", "items": {"type": "object"}}},
    "required": ["cases"],
    "additionalProperties": False,
}
