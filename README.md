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

The Toolkit follows a layered architecture composed of independent frameworks centered around the Pipeline Framework.

```text
Application / CLI
        │
        ▼
Command Framework
        │
        ▼
Pipeline Framework
        │
        ├────────────────────────┐
        ▼                        ▼
Validator Framework      Generator Framework
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
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
      Markdown                 HTML                   PDF
```

The Command Framework provides the public command-line interface for interacting with the Toolkit.

The Pipeline Framework orchestrates validation, artifact generation, template rendering, and export workflows while keeping the individual frameworks independent.

This layered architecture minimizes coupling, simplifies testing, and allows new frameworks and plugins to be added without affecting existing subsystems.

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
- Command Framework
- User Story generator
- Use Case generator
- BPMN Process generator
- User Story validator
- Use Case validator
- BPMN validator
- Markdown exporter
- HTML exporter
- PDF exporter
- Command-line interface
- Architecture documentation

The Toolkit now provides a scalable layered architecture for Business and System Analysis automation.

Its core subsystems include the Localization Framework, Template Engine, Generator Framework, Validator Framework, Pipeline Framework, Export Framework, and Command Framework. Together they provide a unified workflow for validating, generating, exporting, and managing analysis artifacts while preserving subsystem independence and architectural consistency.

The Command Framework serves as the public entry point for interacting with the Toolkit through a unified command-line interface.

The Pipeline Framework remains the central orchestration layer responsible for coordinating validation, artifact generation, and export workflows.

---

# 📅 Roadmap

- [x] Project infrastructure
- [x] Localization subsystem
- [x] Template Engine
- [x] Generator Framework
- [x] Validator Framework
- [x] Pipeline Framework
- [x] Export Framework
- [x] Command Framework (CLI)
- [x] User Story generator
- [x] Use Case generator
- [x] BPMN Process generator
- [x] HTML export
- [x] PDF export
- [ ] Plugin Framework
- [ ] Import Framework
- [ ] UML generator
- [ ] OpenAPI generator
- [ ] SQL generator
- [ ] PlantUML export
- [ ] BPMN XML export
