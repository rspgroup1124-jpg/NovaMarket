# NovaMarket Toolkit Engineering Guidelines

## Purpose

This document defines the engineering standards, architectural principles, development workflow and long-term conventions of the NovaMarket Toolkit.

Its purpose is to ensure that the Toolkit evolves in a consistent, maintainable and extensible manner regardless of the number of contributors involved in the project.

The guidelines described in this document apply to every sprint, every architectural decision and every implementation.

Whenever implementation details conflict with these guidelines, the guidelines take precedence.

---

# Project Vision

NovaMarket Toolkit is developed as if it were a production-ready framework maintained by a professional software engineering team.

Although the project has educational goals, all engineering decisions should satisfy the quality standards expected from long-term commercial software.

Every subsystem should be designed with future extensibility, maintainability and readability in mind.

The Toolkit is intended to become a modular platform for generating Business and System Analysis artifacts rather than a collection of independent scripts.

---

# Engineering Principles

Every architectural and implementation decision should follow the principles below.

## Single Responsibility Principle (SRP)

Every module, class and function should have one clearly defined responsibility.

Examples:

- Domain models represent business data.
- Validators verify model correctness.
- Generators prepare rendering context.
- The Template Engine renders templates.
- Templates define presentation only.

Responsibilities must never overlap.

---

## Open/Closed Principle (OCP)

The Toolkit should be open for extension while remaining closed for modification.

New functionality should be introduced by creating new components instead of changing existing infrastructure whenever possible.

Examples include:

- adding a new generator;
- adding a new validator;
- adding a new artifact type.

Infrastructure should remain stable as the project grows.

---

## Separation of Concerns

Business logic, validation, rendering and presentation must remain independent.

Each subsystem should communicate only through well-defined interfaces.

No subsystem should perform the responsibilities of another subsystem.

---

## Immutability by Default

Domain models are immutable.

Immutable objects simplify reasoning, reduce accidental side effects and make the Toolkit easier to test and maintain.

Whenever possible, immutable data structures should be preferred over mutable ones.

---

## Explicit over Implicit

The Toolkit favors explicit behavior over hidden or automatic behavior.

Dependencies should be visible.

Architectural decisions should be obvious from the code structure.

Magic behavior should be avoided.

---

## KISS

Keep every solution as simple as possible.

Complexity should only be introduced when there is a demonstrated need.

Readable code is preferred over clever code.

---

## DRY

Knowledge should have a single authoritative implementation.

Code duplication should be eliminated whenever practical without sacrificing readability.

---

## YAGNI

Features are implemented only when they become necessary.

The Toolkit intentionally avoids speculative functionality.

Future extensibility should be achieved through architecture rather than unused code.

---

# Core Philosophy

The Toolkit is developed according to the principle:

**Architecture first. Implementation second.**

Every subsystem follows the same lifecycle:

1. Analyze the existing architecture.
2. Define responsibilities.
3. Design the architecture.
4. Review the design.
5. Implement the solution.
6. Write tests.
7. Update documentation.

Implementation is never the starting point.

Good architecture reduces future complexity, improves maintainability and enables long-term evolution of the project.

---

# Long-Term Engineering Goal

The primary objective of the NovaMarket Toolkit is not simply to generate analyst artifacts.

Its long-term goal is to provide a modular, extensible and maintainable engineering platform that automates Business and System Analysis workflows while preserving clean architecture and predictable behavior.

Every new sprint should move the Toolkit closer to this objective without compromising existing architectural principles.

---

# Architecture Principles

The architecture of the NovaMarket Toolkit evolves incrementally.

Each sprint introduces one well-defined subsystem that integrates naturally into the existing architecture without breaking previous design decisions.

Architectural consistency always has higher priority than implementation speed.

Every architectural decision must satisfy the following requirements:

- preserve modularity;
- improve maintainability;
- support future extensibility;
- avoid unnecessary coupling;
- minimize duplication.

Whenever multiple solutions exist, the simplest scalable solution should be preferred.

---

# Layered Architecture

The Toolkit follows a layered architecture.

Each layer has a single responsibility and communicates only with adjacent layers.

Current architecture:

```text
Domain Models
      │
      ▼
Validators
      │
      ▼
Generators
      │
      ▼
Template Engine
      │
      ▼
Templates
```

Layer responsibilities:

## Domain Models

Represent immutable business data.

Domain models never:

- perform rendering;
- perform validation;
- access templates;
- access the file system.

---

## Validators

Verify that domain models satisfy all business and structural rules before generation.

Validators:

- perform validation only;
- never modify models;
- never generate artifacts;
- never render templates.

Validation failures are reported through specialized exceptions.

---

## Generators

Transform validated domain models into rendering contexts.

Generators:

- never validate data;
- never access templates directly;
- never use Jinja2 directly;
- never perform file operations.

Generators communicate only with the Template Engine.

---

## Template Engine

Responsible for rendering templates.

The Template Engine:

- locates templates;
- prepares the Jinja environment;
- renders output;
- hides rendering implementation from generators.

Generators remain independent from the rendering engine.

---

## Templates

Templates define presentation only.

Templates must not contain business rules or validation logic.

Presentation and business logic must always remain separated.

---

# Project Structure Rules

The directory structure is considered part of the architecture.

New subsystems should follow the existing organizational style whenever possible.

Framework-style subsystems should use the following structure:

```text
framework/
│
├── __init__.py
├── base.py
├── exceptions.py
├── registry.py
├── factory.py
│
└── artifacts/
    ├── __init__.py
    ├── ...
```

This convention is currently used by:

- Generator Framework
- Validator Framework

Future frameworks should reuse the same organization whenever appropriate.

---

# Framework Design Rules

Infrastructure components should remain generic.

Concrete artifact implementations belong only inside the `artifacts` package.

Infrastructure modules must never contain artifact-specific logic.

Every framework should consist of:

- abstract base class;
- registry;
- factory;
- exceptions;
- concrete implementations.

This keeps every subsystem predictable and easy to extend.

---

# Dependency Rules

Dependencies always point downward through the architecture.

Allowed dependency flow:

```text
Domain Models

↓

Validators

↓

Generators

↓

Template Engine

↓

Templates
```

Higher layers must not depend on lower implementation details.

Examples:

- Validators know Domain Models.
- Generators know Domain Models and Template Engine.
- Templates know nothing about Python classes.

This prevents circular dependencies and preserves architectural clarity.

---

# Extension Strategy

The Toolkit grows primarily through extension rather than modification.

Typical examples include:

- adding a new artifact generator;
- adding a new validator;
- adding a new domain model;
- adding a new template.

Existing infrastructure should require little or no modification when introducing new functionality.

This approach minimizes regression risk and supports long-term maintenance.

---

# Architectural Consistency

Consistency is considered an architectural feature.

New components should match the naming conventions, directory structure and design patterns already used throughout the Toolkit.

Whenever possible, similar responsibilities should have similar implementations.

Developers should be able to predict the location and behavior of new components based on existing architecture.

Predictability improves readability, maintainability and onboarding for future contributors.

---

# Development Workflow

Every sprint follows the same engineering workflow.

No stage should be skipped.

```text
Planning
    │
    ▼
Architecture Design
    │
    ▼
Implementation
    │
    ▼
Unit Tests
    │
    ▼
Integration Tests (when applicable)
    │
    ▼
Architecture Review
    │
    ▼
ARCHITECTURE.md
    │
    ▼
CHANGELOG.md
    │
    ▼
README.md
    │
    ▼
Black
    │
    ▼
Ruff
    │
    ▼
Pytest
    │
    ▼
Git Status
    │
    ▼
Git Commit
    │
    ▼
Git Tag
    │
    ▼
Git Push
```

Each sprint is considered complete only after every stage has been successfully finished.

---

# Development Process

Every architectural change follows the same sequence.

1. Analyze the existing architecture.
2. Discuss possible solutions.
3. Compare alternatives.
4. Select the most scalable approach.
5. Design the architecture.
6. Implement the solution.
7. Write tests.
8. Update documentation.
9. Perform quality checks.
10. Commit the completed work.

Implementation is never the first step.

---

# Coding Standards

The Toolkit follows strict coding conventions.

## Complete Files

When modifying source code, complete files should be preferred over partial snippets.

Large structural changes should replace the entire file rather than isolated fragments.

This minimizes merge errors and improves readability.

---

## Large Files

If a file is too large to fit into a single response, it should be divided into multiple consecutive parts.

Each part must:

- preserve the correct order;
- clearly indicate continuation;
- result in a complete file when combined.

---

## File Creation

Before creating a new file:

1. Navigate to the correct project directory.
2. Verify the directory structure.
3. Create the file.
4. Verify that the file exists.
5. Only then add its contents.

The existence of files or directories must never be assumed.

---

## Directory Verification

Before introducing new files or architectural changes, verify the current project structure.

Typical commands include:

```powershell
Get-ChildItem
```

or

```powershell
Get-ChildItem -Recurse
```

Existing architecture must always be confirmed before modification.

---

## Command Line First

PowerShell is the preferred interface for project operations.

Typical operations include:

- directory creation;
- file creation;
- file renaming;
- file removal;
- Git commands;
- Black;
- Ruff;
- Pytest.

The graphical interface should only be used when command-line execution is impractical.

---

# Architecture Before Code

Before proposing any implementation, the current codebase must be analyzed.

The following assumptions are prohibited:

- assuming directory structures;
- assuming existing files;
- assuming existing classes;
- assuming implementation details from memory.

If information is missing, the existing project structure or relevant source files should be reviewed first.

Architectural decisions must always be based on the current state of the project.

---

# Design Decision Process

Whenever multiple implementation approaches exist, the following process should be used:

1. Analyze the problem.
2. Identify possible solutions.
3. Evaluate long-term consequences.
4. Select the most maintainable architecture.
5. Implement the chosen solution.

Architectural discussion always precedes implementation.

---

# Scalability Rule

Before accepting any implementation, consider its impact on future development.

The guiding question is:

> Will this decision still be appropriate five to ten sprints from now?

If the answer is uncertain, a more scalable design should be considered.

Long-term maintainability has higher priority than short-term convenience.

---

# Testing Strategy

Every new subsystem must include automated tests.

Framework components should normally be covered by:

- base class tests;
- registry tests;
- factory tests;
- implementation tests.

Business components should include artifact-specific tests.

Integration tests should be added whenever interaction between multiple subsystems becomes significant.

---

# Quality Gates

Before any commit, the following commands must complete successfully:

```powershell
black --check src tests
```

```powershell
ruff check src tests
```

```powershell
pytest
```

A sprint is not considered complete until all quality checks pass successfully.

---

# Documentation Rules

Documentation is treated as part of the product.

Documentation changes are reviewed with the same level of attention as source code.

After completing a sprint, documentation must be updated in the following order:

1. `ARCHITECTURE.md`
2. `CHANGELOG.md`
3. `README.md`

This order ensures that architectural decisions are documented before implementation summaries and project overviews.

---

# Git Workflow

Every completed sprint follows the same Git workflow.

Before committing:

```powershell
git status
```

Create a descriptive commit:

```powershell
git add .
git commit -m "Sprint X: <short description>"
```

Create a version tag:

```powershell
git tag sprint-X
```

Push commits:

```powershell
git push
```

Push tags:

```powershell
git push --tags
```

Each sprint should correspond to one logical Git milestone.

---

# Versioning

Development follows a sprint-based versioning strategy.

Every completed sprint represents a stable architectural checkpoint.

Each checkpoint should satisfy the following conditions:

- implementation completed;
- tests passing;
- documentation updated;
- architecture reviewed;
- Git tag created.

This allows any historical version of the Toolkit to be restored reliably.

---

# Definition of Done

A sprint is considered complete only if all of the following conditions are satisfied.

## Architecture

- Responsibilities are clearly defined.
- Architecture follows existing design principles.
- No unnecessary coupling has been introduced.

## Implementation

- Source code is complete.
- Public APIs are documented.
- Naming conventions are consistent.

## Testing

- Unit tests pass.
- Integration tests pass (when applicable).
- Existing functionality remains unaffected.

## Documentation

- `ARCHITECTURE.md` updated.
- `CHANGELOG.md` updated.
- `README.md` updated.

## Quality

- Black passes.
- Ruff passes.
- Pytest passes.

## Version Control

- Changes committed.
- Git tag created.
- Repository synchronized with GitHub.

Only after completing every item above can a sprint be marked as finished.

---

# Architecture Evolution

The Toolkit has been developed incrementally through focused engineering sprints.

## Sprint 1

Project foundation.

## Sprint 2

Project structure and Localization subsystem prepared.

## Sprint 3

Localization Framework implemented.

## Sprint 4

Generator Framework introduced.

## Sprint 5

Template Engine implemented.

## Sprint 6

User Story Generator implemented.

## Sprint 7

Use Case Generator implemented.

## Sprint 8

BPMN domain model and BPMN Generator implemented.

Architecture documentation introduced.

## Sprint 9

Validator Framework implemented.

The architecture now follows the complete processing pipeline:

```text
Domain Models
      │
      ▼
Validators
      │
      ▼
Generators
      │
      ▼
Template Engine
      │
      ▼
Templates
```

The Toolkit now contains four independent core subsystems:

- Localization
- Validator Framework
- Generator Framework
- Template Engine

---

# Long-Term Roadmap

Future development should continue by extending the existing architecture rather than redesigning it.

Potential future subsystems include:

- Pipeline Framework
- Export Framework
- Import Framework
- OpenAPI Generator
- UML Generator
- SQL Generator
- PlantUML Generator
- BPMN XML Generator
- HTML Export
- PDF Export

Every new subsystem should follow the architectural principles defined in this document.

---

# Engineering Checklist

Before starting any new sprint, verify the following:

- Existing architecture has been reviewed.
- Current project structure has been verified.
- Similar implementations have been studied.
- Responsibilities are clearly defined.
- Extension points have been identified.

Before writing code:

- Architecture has been discussed.
- Alternatives have been evaluated.
- The chosen solution supports long-term maintenance.

Before completing a sprint:

- Tests pass.
- Documentation is updated.
- Code quality checks pass.
- Git history is clean.
- Sprint tag has been created.

---

# Guiding Principle

Every engineering decision should support the long-term evolution of the Toolkit.

The project is developed as if it were intended to be maintained by a professional software engineering team for many years.

Short-term convenience must never compromise architectural quality, maintainability or extensibility.

When in doubt, choose the solution that improves clarity, consistency and long-term sustainability.

---

# Final Statement

NovaMarket Toolkit is more than an educational project.

It is an engineering platform built to demonstrate professional software architecture, disciplined development practices and systematic Business/System Analysis automation.

Every sprint should strengthen these foundations while preserving the architectural integrity of the project.
