# Test Generation Agent

A framework-independent OpenGAP agent that deterministically analyzes supported Python source and produces structured test-case proposals. It does not execute supplied source code.

## Scope
- AST-based Python function and branch analysis
- Deterministic test-case generation
- Structural test-case validation
- Framework-neutral tool contracts and registry
- Portable adapter boundary for external runtimes

## Validation
The environment used for this build has Python 3.13.5 and pytest 9.0.2. The `opengap` executable is not installed, so official CLI validation cannot be claimed from this environment.

## Usage
Set `TEST_AGENT_LOG_LEVEL` and `TEST_AGENT_MAX_CASES` in the runtime environment, then invoke the core service or tool registry from Python. Generated tests are proposals and should be reviewed and executed in the target project.
