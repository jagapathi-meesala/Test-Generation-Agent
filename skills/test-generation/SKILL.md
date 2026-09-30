---
name: test-generation
description: Generate deterministic, structured test cases from supported Python source code without executing the source.
license: MIT
---
# Test Generation

Analyze Python source using AST structure and create baseline, positive-value, and explicit-branch test proposals when applicable.

## Inputs
Provide source text, language `python`, an optional maximum case count, and an optional function-name focus.

## Behavior
The skill parses source structure, identifies functions and simple branches, then produces cases with rationale and source-line provenance. It never executes supplied code.

## Outputs
Return analysis metadata, structured test cases, counts, and explicit limitations.

## Invalid Inputs
Reject empty source, invalid Python syntax, unsupported languages, and invalid case-count ranges.
