# Changelog

All notable changes to the NovaMarket Toolkit are documented in this file.

The project follows an iterative sprint-based development process.

---

## Sprint 8

### Added

- Added the `BPMNProcess` domain model and related BPMN entities.
- Added the `BPMNGenerator`.
- Added the `bpmn_process.md.j2` template.
- Added unit tests for the `BPMNProcess` domain model.
- Added unit tests for the `BPMNGenerator`.
- Added the initial architecture documentation (`docs/architecture/ARCHITECTURE.md`).


### Architecture

- Established the architecture documentation for the Toolkit.
- Introduced `ARCHITECTURE.md` as the primary architecture reference.
- Introduced Architecture Rules (AR) as the primary engineering standard.
- Documented the design principles governing the Toolkit architecture.
- Formalized layer responsibilities and the architecture evolution workflow.
- Confirmed compliance with the Open/Closed Principle (OCP) by adding the BPMN generator without modifying the existing generator infrastructure.
---

## Sprint 7

### Added

- Added the `UseCase` domain model.
- Added the `UseCaseGenerator`.
- Added the `use_case.md.j2` Jinja2 template.
- Added unit tests for the `UseCase` model.
- Added unit tests for the `UseCaseGenerator`.
- Added integration tests for the generator framework.

### Architecture

- Confirmed the extensibility of the generator framework by adding a second artifact generator without modifying the core infrastructure.
- Introduced AR-003: generators reference templates using logical template names.

---

## Sprint 6

### Added

- Introduced the `TemplateEngine`.
- Added the `TemplateLoader`.
- Added support for Jinja2 templates.
- Added the template directory structure (`templates/en`, `templates/ru`, `templates/uk`).
- Migrated `UserStoryGenerator` to the template engine.

### Architecture

- Separated business logic from presentation.
- Introduced logical template names and centralized template loading.
- Established AR-001: generated artifacts do not end with a trailing newline.

---

## Sprint 5

### Added

- Implemented the first production-ready `UserStoryGenerator`.
- Added the initial generator integration tests.
- Improved the generator framework.

### Architecture

- Completed the first end-to-end generation pipeline from domain model to generated artifact.

---

## Sprint 4

### Added

- Implemented the generator framework.
- Added `BaseGenerator`.
- Added `GeneratorRegistry`.
- Added `GeneratorFactory`.

### Architecture

- Established a pluggable generator architecture.

---

## Sprint 3

### Added

- Implemented the localization subsystem.
- Added `LocalizationLoader`.
- Added `TranslationService`.
- Added glossary support.
- Added English, Ukrainian and Russian locale files.

### Architecture

- Technical terminology is language-independent.
- User-facing text is localized.

---

## Sprint 2

### Added

- Expanded the Toolkit package structure.
- Added project configuration.
- Added testing infrastructure.
- Added code quality tools (Black, Ruff, Pytest).

### Architecture

- Established the development workflow and project conventions.

---

## Sprint 1

### Added

- Created the initial NovaMarket Toolkit project.
- Configured Python packaging.
- Created the initial CLI entry point.
- Prepared the project structure for future development.
