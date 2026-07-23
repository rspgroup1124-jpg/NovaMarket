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


### Current Features

- Localization subsystem
- Validator Framework
- Generator Framework
- Template Engine (Jinja2)
- Architecture documentation
- User Story generation
- Use Case generation
- BPMN Process generation
- User Story validation
- Use Case validation
- BPMN Process validation
- Unit tests
---

## 🏗 Architecture

The Toolkit follows a layered architecture.

```text
Domain Models
      │
      ▼
Generators
      │
      ▼
Template Engine
      │
      ▼
Jinja2 Templates
```

This separation keeps business logic independent from presentation and makes the framework easily extensible.
The architectural principles, engineering conventions and long-term design decisions are documented in `docs/architecture/ARCHITECTURE.md`.
---

## 🧪 Quality Assurance

The project includes:

- Unit tests
- Black formatting
- Ruff linting
- Immutable domain models
- Validator Framework
- Template-based artifact generation
- Architecture review
- Architecture documentation

## 🚀 Current Status
Completed:

- Project infrastructure
- Localization subsystem
- Validator Framework
- Generator framework
- Template engine
- User Story generator
- Use Case generator
- BPMN Process generator
- User Story validator
- Use Case validator
- BPMN validator
- Architecture documentation

The Toolkit now provides a scalable layered architecture for validating and generating Business/System Analyst artifacts. Its core components include Localization, Validator Framework, Generator Framework and the Template Engine, all documented through a formal architecture specification that captures engineering principles, architectural rules and long-term design decisions.
---

## 📅 Roadmap

- [x] Project infrastructure
- [x] Localization subsystem
- [x] Generator framework
- [x] Validator Framework
- [x] Template Engine
- [x] User Story generator
- [x] Use Case generator
- [x] BPMN Process generator
- [ ] UML generator
- [ ] OpenAPI generator
- [ ] SQL generator
- [ ] HTML export
- [ ] PDF export
- [ ] PlantUML export
- [ ] BPMN XML export
