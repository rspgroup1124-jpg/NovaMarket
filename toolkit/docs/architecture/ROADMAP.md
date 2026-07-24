# NovaMarket Toolkit Roadmap

## Purpose

This document defines the planned evolution of the NovaMarket Toolkit.

It describes the architectural direction of future development and the objectives of upcoming sprints.

The roadmap is a planning document rather than a commitment. It may evolve as the architecture matures, but every change should preserve the long-term vision of the project.

---

# Long-Term Vision

NovaMarket Toolkit aims to become a complete automation platform for Business and System Analysis.

The project will provide a unified pipeline capable of:

- validating domain models;
- generating analysis artifacts;
- rendering multiple output formats;
- importing existing documentation;
- exporting documentation to various targets;
- supporting extensibility through plugins.

Every subsystem must integrate into the existing layered architecture without breaking architectural consistency.

---

# Development Roadmap

## ✅ Sprint 1 — Project Infrastructure

Status: Completed

Main objective:

- Create the project structure.
- Configure the development environment.
- Prepare the Python package.

---

## ✅ Sprint 2 — Localization Framework

Status: Completed

Main objective:

- Localization loader.
- Translation service.
- Technical glossary.

---

## ✅ Sprint 3 — Template Engine

Status: Completed

Main objective:

- Jinja2 integration.
- Template rendering.
- Template management.

---

## ✅ Sprint 4 — Generator Framework

Status: Completed

Main objective:

- BaseGenerator.
- Registry.
- Factory.

---

## ✅ Sprint 5

Status: Completed

Main objective:

- User Story domain model.
- User Story generator.

---

## ✅ Sprint 6

Status: Completed

Main objective:

- Use Case domain model.
- Use Case generator.

---

## ✅ Sprint 7

Status: Completed

Main objective:

- BPMN domain model.

---

## ✅ Sprint 8

Status: Completed

Main objective:

- BPMN generator.
- Architecture documentation.

---

## ✅ Sprint 9 — Validator Framework

Status: Completed

Main objective:

- BaseValidator.
- ValidatorRegistry.
- ValidatorFactory.
- User Story Validator.
- Use Case Validator.
- BPMN Validator.
- Validator tests.
---

## ✅ Sprint 10 — Pipeline Framework

Status: Completed

Main objective:

Introduce a unified orchestration layer responsible for the complete artifact generation workflow.

Implemented components:

- Pipeline
- PipelineBuilder
- PipelineContext
- PipelineResult
- Pipeline Exceptions

Implemented responsibilities:

- orchestrate validation;
- orchestrate generation;
- centralize workflow execution;
- provide a single public API for artifact creation.

Additional improvements:

- integrated the Validator Framework;
- integrated the Generator Framework;
- introduced dependency injection through PipelineBuilder;
- added the public `Pipeline.generate()` API;
- preserved layered architecture and subsystem independence.

---

## Sprint 11 — Export Framework

Status: Planned

Main objective:

Introduce a common export infrastructure independent of generators.

Planned components:

- BaseExporter
- ExportRegistry
- ExportFactory

Initial exporters:

- Markdown Export
- HTML Export
- PDF Export

Responsibilities:

- export generated artifacts;
- support multiple output formats;
- isolate export logic from generators.

---

## Sprint 12 — Command Framework (CLI)

Status: Planned

Main objective:

Transform the Toolkit into a complete command-line application.

Planned commands:

- generate
- validate
- export
- list
- info
- version

Responsibilities:

- provide a user-friendly interface;
- invoke the Pipeline Framework;
- support localization.

---

## Sprint 13 — Plugin Framework

Status: Planned

Main objective:

Allow external packages to extend the Toolkit without modifying the core.

Planned components:

- PluginManager
- PluginLoader
- PluginRegistry

Responsibilities:

- discover plugins;
- register generators;
- register validators;
- register exporters.

This sprint establishes the Toolkit as an extensible platform.


---

## Sprint 14 — Analysis Artifact Framework

Status: Planned

Main objective:

Extend the Toolkit with professional Business and System Analysis artifacts.

Planned domain models:

- UML Use Case Diagram
- Sequence Diagram
- Class Diagram
- Activity Diagram

Planned generators:

- PlantUML Generator
- Mermaid Generator

Responsibilities:

- transform domain models into diagram definitions;
- support multiple diagram formats;
- integrate with the Pipeline Framework;
- reuse the existing Template Engine.

This sprint introduces the first diagram-oriented subsystem while preserving the layered architecture.

---

## Sprint 15 — API & Database Framework

Status: Planned

Main objective:

Provide automated generation of technical specifications for backend systems.

Planned domain models:

- REST API
- OpenAPI Specification
- Database Schema
- SQL Objects

Planned generators:

- OpenAPI Generator
- SQL DDL Generator
- PostgreSQL Generator

Planned exporters:

- YAML
- JSON
- SQL

Responsibilities:

- generate OpenAPI specifications;
- generate database schemas;
- generate SQL scripts;
- prepare artifacts suitable for implementation by development teams.

---

# Architecture Evolution

The Toolkit architecture is expected to evolve gradually.

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

Target architecture after Sprint 15:

```text
CLI
 │
 ▼
Pipeline
 │
 ├───────────────┐
 ▼               ▼
Validators    Generators
 │               │
 └──────┐   ┌────┘
        ▼   ▼
 Template Engine
        │
        ▼
Templates
        │
        ▼
Export Framework
        │
        ▼
Markdown
HTML
PDF
YAML
JSON
SQL
PlantUML
Mermaid
```

The architecture will remain modular, layered and extensible.

Each new subsystem should integrate with existing infrastructure instead of replacing it.

---

# Roadmap Maintenance

This roadmap is reviewed at the end of every sprint.

Whenever a sprint is completed:

- update its status;
- document architectural changes;
- add the next planned sprint if required;
- verify consistency with `PROJECT_STATE.md` and `ARCHITECTURE.md`.

The roadmap should always represent the current long-term development strategy of the NovaMarket Toolkit.
