# NovaMarket Toolkit — Project State

## Purpose

This document provides a concise snapshot of the current state of the NovaMarket Toolkit.

It is intended to help developers quickly understand:

- the current implementation status;
- the architectural state of the project;
- completed subsystems;
- the next planned development stage.

Unlike `CHANGELOG.md`, which records historical changes, this document always reflects the latest state of the project.

---

# Project Overview

NovaMarket Toolkit is a Python package that automates the generation of Business and System Analysis artifacts.

The project is developed incrementally using sprint-based development.

Every sprint introduces one complete subsystem while preserving architectural consistency.

The Toolkit follows a layered architecture and emphasizes:

- maintainability;
- extensibility;
- separation of responsibilities;
- immutable domain models;
- comprehensive automated testing.
---
# Current Status

Current Sprint:

**Sprint 12 — Command Framework (Completed)**

Project Status:

**Stable**

All implemented subsystems successfully pass:

- Black
- Ruff
- Pytest

Current test status:

- **100 tests passing**

Documentation is synchronized with the implementation.

Git history is organized using sprint-based commits.

The Toolkit now provides a complete command-line interface built on top of the existing architecture, exposing a unified entry point for generating, validating, exporting, and managing analysis artifacts while preserving the layered design of the project.

---

# Completed Subsystems

The following subsystems are fully implemented.

## Core Infrastructure

- Project structure
- Configuration
- CLI entry point
- Shared utilities

## Localization

- Localization Loader
- Translation Service
- Technical glossary
- Multi-language support

## Template Engine

- Template Loader
- Rendering Engine
- Template Exceptions

## Generator Framework

- BaseGenerator
- GeneratorRegistry
- GeneratorFactory

Implemented generators:

- User Story Generator
- Use Case Generator
- BPMN Generator

## Validator Framework

- BaseValidator
- ValidatorRegistry
- ValidatorFactory

Implemented validators:

- User Story Validator
- Use Case Validator
- BPMN Validator

## Pipeline Framework

- Pipeline
- PipelineBuilder
- PipelineContext
- PipelineResult
- Pipeline Exceptions

Implemented features:

- Validator orchestration
- Generator orchestration
- Public `Pipeline.generate()` API
- Dependency injection through PipelineBuilder

---

## Export Framework

- BaseExporter
- ExportRegistry
- ExportFactory
- Export Exceptions

Implemented features:

- Markdown export
- HTML export
- PDF export
- Multiple export format support
- Independent export infrastructure
-
---

# Command Framework (CLI)

Implemented components:

- Typer-based CLI
- Command registration
- Command package
- Command unit tests

Available commands:

- doctor
- generate
- validate
- export
- list
- info
- version

Implemented features:

- Unified command-line interface
- Modular command architecture
- Independent command implementations
- User-friendly help system
- Full CLI test coverage

---

# Current Architecture

The Toolkit currently follows a six-layer architecture.

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
Exporters
      │
      ▼
Template Engine
      │
      ▼
Templates
```

## Layer Responsibilities

### Domain Models

Represent immutable business objects.

They contain business data only and do not implement rendering or validation logic.

---

### Validator Framework

Validates domain models before artifact generation.

Responsibilities include:

- required field validation;
- empty collection checks;
- duplicate identifier detection;
- reference integrity validation;
- business rule validation.

Validators either complete successfully or raise a specialized validation exception.

---

### Generator Framework

Transforms validated domain models into rendering contexts.

Generators:

- contain business transformation logic;
- never access the file system directly;
- never render templates directly;
- communicate only with the Template Engine.

---

### Template Engine

Responsible for rendering templates.

The Template Engine:

- loads templates;
- prepares the rendering environment;
- renders artifacts using Jinja2;
- isolates presentation from business logic.

---

### Templates

Templates define presentation only.

They must not contain business logic.

All business decisions are performed before rendering.

---

# Project Structure

# Project Structure

The Toolkit is organized into independent subsystems.

```text
toolkit/
│
├── docs/
│   └── architecture/
│
├── src/
│   └── novamarket_toolkit/
│       ├── commands/
│       ├── exporters/
│       ├── generators/
│       ├── glossary/
│       ├── i18n/
│       ├── locales/
│       ├── models/
│       ├── pipeline/
│       ├── template_engine/
│       ├── templates/
│       ├── utils/
│       └── validators/
│
├── tests/
│   ├── commands/
│   ├── exporters/
│   ├── generators/
│   ├── pipeline/
│   └── validators/
│
├── CHANGELOG.md
├── README.md
└── pyproject.toml
```
---

# Current Quality Status

The project currently satisfies all established engineering quality standards.

## Code Quality

- Black formatting is enforced.
- Ruff linting passes successfully.
- Source code follows a consistent style.
- Public APIs are documented.

## Testing

The project includes both framework and artifact tests.

Implemented test categories include:

- domain model tests;
- framework tests;
- artifact generator tests;
- validator tests;
- integration tests.

All existing tests pass successfully.

## Documentation

The following engineering documents are maintained:

- `README.md`
- `CHANGELOG.md`
- `ARCHITECTURE.md`
- `ENGINEERING_GUIDELINES.md`
- `PROJECT_STATE.md`

Documentation is updated as part of every completed sprint.

---

# Current Metrics

Current implementation includes:

## Frameworks

- Localization Framework
- Template Engine
- Generator Framework
- Validator Framework
- Pipeline Framework
- Export Framework
- Command Framework

## Command-line Interface

Available commands:

- doctor
- generate
- validate
- export
- list
- info
- version

## Test Status

- 100 unit tests passing

## Artifact Generators

- User Story
- Use Case
- BPMN Process

## Artifact Validators

- User Story
- Use Case
- BPMN Process

---


## Architecture

- Layered Architecture
- Immutable Domain Models
- Registry/Factory Pattern
- Pipeline Orchestration
- Template-based Rendering
- Centralized Validation
- Dependency Injection
- Independent Export Infrastructure
- Command Framework (CLI)

---

# Next Sprint

**Sprint 13 — Plugin Framework**

The next subsystem will allow external packages to extend the Toolkit without modifying the core application.

The target architecture will become:

```text
Application / CLI
        │
        ▼
Command Framework
        │
        ▼
Plugin Framework
        │
        ▼
Pipeline
        │
        ├───────────────┐
        ▼               ▼
Validators        Generators
                        │
                        ▼
                 Template Engine
                        │
                        ▼
                   Templates
                        │
                        ▼
                 Export Framework
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    Markdown          HTML            PDF
```

The Plugin Framework will introduce a unified extension mechanism for discovering and registering generators, validators, exporters, and future Toolkit components while preserving the existing layered architecture.

---

# Long-Term Vision

The long-term objective is to build a complete automation platform for Business and System Analysis.

Planned future subsystems include:

- Command Framework (CLI)
- Import Framework
- OpenAPI Generator
- UML Generator
- SQL Generator
- PlantUML Generator
- BPMN XML Generator
- Plugin System

Every future subsystem will follow the architectural principles defined in:

- `ARCHITECTURE.md`
- `ENGINEERING_GUIDELINES.md`

---

# Document Maintenance

This document represents the current state of the project.

It should be reviewed and updated at the end of every completed sprint.

Whenever a new subsystem is introduced, the following sections should be revised:

- Current Status
- Completed Subsystems
- Current Architecture
- Current Metrics
- Next Sprint
- Long-Term Vision

This ensures that the document always reflects the latest state of the NovaMarket Toolkit.
