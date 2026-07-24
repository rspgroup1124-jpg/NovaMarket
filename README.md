# NovaMarket

## 📖 About

**NovaMarket** is an educational project that simulates the development of a modern marketplace.

The project is designed to study the complete Business/System Analyst workflow — from business requirements to technical documentation, UML/BPMN diagrams, API specifications, data modeling, and documentation automation using Python.

---

## 🎯 Project Goals

- Build a professional Business/System Analyst portfolio.
- Practice modern system analysis techniques.
- Learn BPMN, UML and PlantUML.
- Design REST APIs.
- Model PostgreSQL databases.
- Automate analyst documentation using Python.

---

## 📂 Project Structure

```text
NovaMarket/
│
├── analysis/
├── diagrams/
├── docker/
├── docs/
├── engineering/
├── examples/
├── scripts/
├── toolkit/
└── README.md
```

---

## 🛠 Technologies

- Python 3.12+
- PostgreSQL
- Docker
- Jinja2
- Typer
- Pytest
- Ruff
- Black
- PlantUML
- Graphviz
- Git
- Markdown

---

## 🧰 NovaMarket Toolkit

The Toolkit is a Python package that automates the creation of common Business/System Analyst artifacts.

---

### Current Features

- Localization subsystem
- Template Engine (Jinja2)
- Generator Framework
- Validator Framework
- Pipeline Framework
- Export Framework
- User Story generation
- Use Case generation
- BPMN Process generation
- User Story validation
- Use Case validation
- BPMN Process validation
- Markdown export
- HTML export
- PDF export
- Unified artifact generation pipeline
- Public `Pipeline.generate()` API
- Unit tests
- Architecture documentation

---

## 🏗 Architecture

The Toolkit follows a layered architecture centered around the Pipeline Framework.

```text
Application / CLI
        │
        ▼
Pipeline
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
Jinja2 Templates
        │
        ▼
Generated Artifact
        │
        ▼
Export Framework
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
Markdown HTML    PDF
```

This layered architecture separates validation, generation, rendering, and export responsibilities while keeping each subsystem independent and easily extensible.

The architectural principles, engineering conventions, and long-term design decisions are documented in `docs/architecture/ARCHITECTURE.md`.

---

## 🧪 Quality Assurance

The project includes:

- Unit tests
- Black formatting
- Ruff linting
- Immutable domain models
- Validator Framework
- Generator Framework
- Pipeline Framework
- Export Framework
- Template-based artifact generation
- Architecture review
- Architecture documentation
---
## 🚀 Current Status

Completed:

- Project infrastructure
- Localization subsystem
- Template Engine
- Generator Framework
- Validator Framework
- Pipeline Framework
- Export Framework
- User Story generator
- Use Case generator
- BPMN Process generator
- User Story validator
- Use Case validator
- BPMN validator
- Markdown exporter
- HTML exporter
- PDF exporter
- Architecture documentation


The Toolkit now provides a scalable layered architecture for Business and System Analysis automation.

Its core subsystems include Localization, the Template Engine, the Generator Framework, the Validator Framework and the Pipeline Framework. Together they provide a unified workflow for validating and generating analysis artifacts while preserving subsystem independence and architectural consistency.

The Pipeline Framework serves as the single public entry point for artifact generation, coordinating validators and generators through a centralized orchestration layer.

---
## 📅 Roadmap

- [x] Project infrastructure
- [x] Localization subsystem
- [x] Template Engine
- [x] Generator Framework
- [x] Validator Framework
- [x] Pipeline Framework
- [x] Export Framework
- [x] User Story generator
- [x] Use Case generator
- [x] BPMN Process generator
- [x] HTML export
- [x] PDF export
- [ ] Command Framework (CLI)
- [ ] Plugin Framework
- [ ] Import Framework
- [ ] UML generator
- [ ] OpenAPI generator
- [ ] SQL generator
- [ ] PlantUML export
- [ ] BPMN XML export
