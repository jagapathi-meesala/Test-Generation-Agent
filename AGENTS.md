# Agent Instructions

## Architecture
Keep domain logic in `core/`, contracts in `contracts/`, tool entry points in `tools/`, skills in `skills/`, and portability boundaries in `adapters/`. Do not introduce framework-specific dependencies into the core.

## Development Rules
Use explicit types, deterministic transformations, input validation, and structured errors. Avoid arbitrary code execution and hidden network access.

## Testing Rules
Run the complete pytest suite after changes. Tests must cover normal inputs, invalid inputs, boundary cases, duplicate detection, documentation structure, registry behavior, and adapter serialization.

## Portability
Adapters translate framework-specific invocation formats into the framework-independent contract. An adapter may be exercised without installing the target framework; that is a compatibility test, not proof of full framework integration.
