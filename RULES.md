# Rules

## Deterministic Rules
1. Inputs must satisfy the declared tool schemas before processing.
2. Supported Python function definitions are analyzed structurally; source code is parsed with Python's AST and is never executed.
3. Generated cases are derived from explicit parameters, return annotations when available, simple branch conditions, and user-provided focus values.
4. Duplicate cases are rejected by normalized case identity.
5. Unsupported syntax or ambiguous requirements are reported as limitations rather than guessed.
6. The agent never uses `eval`, `exec`, subprocess execution, or dynamic imports on supplied source code.

## Output Rules
Every generated test case has an identifier, target, category, inputs, expected behavior, rationale, and provenance. Validation reports errors separately from warnings so callers can distinguish invalid data from review recommendations.
