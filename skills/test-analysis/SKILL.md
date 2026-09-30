---
name: test-analysis
description: Validate generated test case structures for required fields, duplicate identifiers, and input/output consistency.
license: MIT
---
# Test Analysis

## Inputs
Provide a list of generated test case objects.

## Behavior
Check required fields, object types, duplicate identifiers, non-empty expectations, and list structure. Report errors separately from review warnings.

## Outputs
Return `valid`, `errors`, `warnings`, and `count` fields.

## Limits
Structural validation does not execute tests and cannot prove behavioral correctness.
