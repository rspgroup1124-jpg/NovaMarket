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
- Template Engine (Jinja2)
- Generator Framework
- User Story generation
- Use Case generation
- Unit and integration tests

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

---

## 🧪 Quality Assurance

The project includes:

- Unit tests
- Integration tests
- Black formatting
- Ruff linting
- Immutable domain models
- Template-based artifact generation

---

## 🚀 Current Status

Completed:

- Project infrastructure
- Localization subsystem
- Generator framework
- Template engine
- User Story generator
- Use Case generator

The Toolkit is now ready to support additional artifact generators without changes to the core architecture.

---

## 📅 Roadmap

- [x] Project infrastructure
- [x] Localization subsystem
- [x] Generator framework
- [x] Template Engine
- [x] User Story generator
- [x] Use Case generator
- [ ] BPMN generator
- [ ] UML generator
- [ ] OpenAPI generator
- [ ] SQL generator
- [ ] HTML export
- [ ] PDF export
