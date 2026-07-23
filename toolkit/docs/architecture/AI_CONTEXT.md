# AI Context

## Purpose

This document provides the essential context required to continue the development of the NovaMarket Toolkit in a new AI conversation.

It is intended to minimize the amount of repeated explanations while ensuring that architectural consistency, engineering practices and project conventions are preserved.

This document complements:

- `ARCHITECTURE.md`
- `ENGINEERING_GUIDELINES.md`
- `PROJECT_STATE.md`
- `CHANGELOG.md`

It does not replace them.

---

# Project Identity

Project name:

**NovaMarket Toolkit**

Project type:

Educational open-source Python toolkit.

Primary goal:

Automate the creation of Business and System Analysis artifacts while demonstrating professional software architecture and engineering practices.

Target users:

- Business Analysts
- System Analysts
- Solution Designers
- Students
- Portfolio reviewers

Programming language:

Python 3.12+

Development approach:

Sprint-based incremental development.

---

# Engineering Context

The Toolkit follows a layered architecture.

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

Current core subsystems:

- Localization
- Template Engine
- Generator Framework
- Validator Framework

Implemented artifacts:

- User Story
- Use Case
- BPMN Process

All domain models are immutable.

Framework-style subsystems follow the same structure:

```text
framework/
│
├── base.py
├── exceptions.py
├── registry.py
├── factory.py
│
└── artifacts/
```

Architectural consistency has higher priority than implementation speed.

---

# Engineering Principles

Every implementation should follow:

- SOLID
- DRY
- KISS
- YAGNI

General principles:

- Architecture before implementation.
- Design before coding.
- Discussion before implementation.
- Documentation after implementation.
- Quality before commit.

The project grows by extending existing architecture rather than redesigning it.

---

# Collaboration Rules

When assisting with this project, always follow these rules.

## Architecture First

Before proposing code:

- analyze the current architecture;
- understand existing components;
- preserve consistency.

Never assume project structure from memory.

If information is missing, request the relevant file or directory structure before continuing.

---

## Complete Files

Provide complete files whenever significant changes are required.

Avoid responses such as:

```python
...
```

or

```python
# Remaining code unchanged
```

Every provided file should be complete and self-contained.

---

## File Creation Workflow

Before creating a file:

1. Navigate to the correct directory.
2. Verify the directory exists.
3. Create the file.
4. Verify the file was created.
5. Only then provide its contents.

PowerShell is preferred over graphical tools whenever possible.

---

## Development Workflow

Every sprint follows the same sequence:

```text
Planning

↓

Architecture Design

↓

Implementation

↓

Unit Tests

↓

Integration Tests

↓

Architecture Review

↓

ARCHITECTURE.md

↓

CHANGELOG.md

↓

README.md

↓

Black

↓

Ruff

↓

Pytest

↓

Git Status

↓

Commit

↓

Tag

↓

Push
```

No step should be skipped.

---

## Documentation Policy

Documentation is part of the product.

Every architectural decision must eventually be reflected in documentation.

Documentation update order:

1. ARCHITECTURE.md
2. CHANGELOG.md
3. README.md

---

## Quality Requirements

Before completing a sprint:

- Black passes.
- Ruff passes.
- Pytest passes.
- Documentation updated.
- Architecture reviewed.

---

# Conversation Bootstrap

When starting a new conversation, use a prompt similar to the following.

---

Continue the development of **NovaMarket Toolkit**.

The project follows the documentation located in:

- `docs/architecture/ARCHITECTURE.md`
- `docs/architecture/ENGINEERING_GUIDELINES.md`
- `docs/architecture/PROJECT_STATE.md`

Before proposing any implementation:

- analyze the existing architecture;
- do not assume files or directories;
- request missing source files when necessary;
- preserve architectural consistency.

Follow the established sprint workflow.

Provide complete files instead of partial snippets whenever practical.

Use PowerShell commands for project operations whenever possible.

Treat the Toolkit as a long-term production-quality engineering project.

---

# Long-Term Objective

NovaMarket Toolkit is intended to evolve into a complete automation platform for Business and System Analysis.

Future development should continue by introducing independent, well-structured subsystems while preserving the existing layered architecture.

Every new subsystem should strengthen the architecture rather than complicate it.
