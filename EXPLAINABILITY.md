# Explainability

## Inputs and Data Sources
The agent accepts source code as an explicit input and currently supports Python source text. Its primary data source is the caller-provided source itself; no external database, network service, or hidden dataset is consulted.
The input mechanism is a structured tool request containing source text, language, and optional generation controls. The analyzer parses the source with Python's AST module and records function names, parameters, annotations, branch counts, and source lines.

### Input Requirements
Source must be non-empty, syntactically valid Python, and accompanied by the supported language identifier. Generation limits are bounded by the tool contract, while an optional focus value restricts generation to matching function names.

## Decision and Reasoning
The decision process is deterministic: parse the source, identify functions, inspect their parameter lists and simple control-flow nodes, then map those observations to structured test categories. Baseline cases cover the callable surface, positive-value probes are created for parameterized functions, and an additional branch case is produced when an explicit conditional exists.
The reasoning for each generated case is stored in its rationale field, while provenance records the source line and the deterministic analysis method. No language model is required for generation and no generated claim is treated as proof of runtime correctness.

### Rules Applied
Case identifiers are stable for the same function/category combination. The validator rejects missing required fields, duplicate identifiers, invalid input objects, and empty expected-behavior text.

### Worked Example
For `def add(a, b): return a + b`, the analyzer identifies two parameters and no explicit branch. The generator therefore proposes a baseline case using zero values and a positive-value case using one values; these cases are proposals rather than executed tests.

## Limits and Constraints
The current implementation supports Python syntax analysis only and does not execute application code. Generic values such as zero and one may not satisfy domain-specific preconditions, so generated cases require review before adoption.
The agent does not access external services, install packages, infer hidden business requirements, or certify coverage. Runtime behavior, integration behavior, and domain semantics remain outside the deterministic analysis boundary.

### Failure Handling
Invalid Python syntax produces a clear validation error with the parser's message and line information. Unsupported languages are rejected rather than silently interpreted as Python.

### Expected Outputs
Successful generation returns analysis metadata, a list of structured cases, a count, and explicit limitations. Validation returns a boolean validity result plus separate errors and warnings.

### Tool-by-Tool Behavior
`analyze-code` parses Python and returns function structure; `generate-test-cases` derives deterministic case proposals; `validate-test-cases` checks the generated structure. Each tool validates its input before execution and returns structured data rather than a free-form success message.

### Provenance
Each generated case includes a source line and the fixed method label `deterministic-ast-analysis`. This provenance identifies how the proposal was derived and helps a reviewer trace it back to the source structure.
