# NovaMarket Toolkit Architecture

## Purpose

This document describes the architectural principles, design decisions and long-term conventions of the NovaMarket Toolkit.

Its purpose is to ensure that the project evolves consistently while remaining easy to understand, maintain and extend.

The architecture is intended to support long-term development rather than individual implementation details. Every new component should follow the principles defined in this document.

---

# Design Principles

The Toolkit is designed according to a small set of fundamental engineering principles. These principles guide every architectural decision made throughout the project.

## Layered Architecture

The system is organized into independent layers.

Each layer has a single responsibility and communicates only with adjacent layers.

Business logic is isolated from presentation and infrastructure.

---

## Open/Closed Principle (OCP)

The architecture should be open for extension but closed for modification.

New artifact generators should be added by introducing new components rather than changing existing infrastructure.

---

## Single Responsibility Principle (SRP)

Every class should have one well-defined responsibility.

Domain models describe data.

Generators prepare rendering context.

The template engine renders templates.

Templates define presentation only.

---

## Immutability by Default

Domain models are immutable.

Immutable objects simplify reasoning, improve reliability and reduce accidental side effects.

---

## Separation of Business Logic and Presentation

Business rules belong to Python code.

Presentation belongs to Jinja templates.

Templates should never become responsible for business logic.

---

---

# Validator Framework

## Purpose

The Validator Framework is responsible for verifying domain models before artifact generation.

Validators ensure that input data satisfies structural and business requirements, allowing generators to assume that every received model is valid.

Validation is intentionally implemented as a separate architectural layer and does not perform any artifact generation.

---

## Architecture

The Generator, Validator, and Export Frameworks follow the same architectural principles.

Every implementation inherits from its corresponding base class.

Framework components are registered through dedicated registries and instantiated through factories.

This shared architecture keeps all extensible subsystems consistent, predictable, and easy to maintain.

```text
                 Base Component
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 BaseValidator   BaseGenerator   BaseExporter
        │              │              │
        ▼              ▼              ▼
   Validators     Generators      Exporters
```

---

## Responsibilities

Validators are responsible for:

- verifying required fields;
- validating empty strings;
- validating collections;
- checking duplicate identifiers;
- verifying reference integrity;
- ensuring model consistency before generation.

Validators never:

- render templates;
- generate artifacts;
- access the file system;
- communicate with the Template Engine.

---


## Validation Workflow

The validation process is performed before artifact generation.

After a successful validation, the generated artifact may be exported to one of the supported output formats.

```text
Domain Model
      │
      ▼
Validator
      │
      ▼
Generator
      │
      ▼
Template Engine
      │
      ▼
Generated Artifact
      │
      ▼
Exporter
      │
      ▼
Exported Output
```

Generators may therefore assume that every incoming model has already passed validation.

Exporters may assume that every incoming artifact has already been successfully generated.
---

## Extensibility

Adding a new validator requires only three steps:

1. Create a validator inheriting from `BaseValidator`.
2. Register it in `ValidatorRegistry`.
3. Instantiate it through `ValidatorFactory`.

Existing infrastructure does not require modification, satisfying the Open/Closed Principle.

---

## Current Validators

The Toolkit currently provides validators for:

- User Story
- Use Case
- BPMN Process

Additional validators should follow the same architectural conventions.

## KISS (Keep It Simple, Stupid)

The architecture favors simple and explicit solutions.

Additional abstraction is introduced only when it provides measurable value.

---

## YAGNI (You Aren't Gonna Need It)

Features are implemented only when they become necessary.

Potential future extensions are documented but are not implemented prematurely.

---

## Explicit over Implicit

The Toolkit favors explicit behavior.

Registration, configuration and dependencies should remain understandable without hidden magic whenever practical.

---

# System Architecture

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

The Command Framework provides the public entry point for interacting with the Toolkit.

The Pipeline Framework orchestrates the complete artifact lifecycle by coordinating validation, generation, template rendering, and export.

Each framework has a single responsibility and communicates only through well-defined public interfaces.

This layered architecture minimizes coupling, simplifies testing, and allows every subsystem to evolve independently.

---

# Layer Responsibilities

| Framework | Responsibility |
|-----------|----------------|
| Application / CLI | Public entry point for users and external integrations. |
| Command Framework | Register and dispatch command-line operations. |
| Pipeline Framework | Coordinate validation, generation, and export workflows. |
| Validator Framework | Validate domain models before generation. |
| Generator Framework | Produce artifacts from validated domain models. |
| Template Engine | Load and render Jinja2 templates. |
| Templates | Define artifact presentation and structure. |
| Export Framework | Export generated artifacts to supported output formats. |

---

# Layer Responsibilities

| Layer | Responsibility |
|--------|----------------|
| Application / CLI | Entry point for users and external integrations. |
| Pipeline | Orchestrate validation and artifact generation. |
| Validators | Validate domain models before generation. |
| Generators | Transform validated domain models into template contexts or generated artifacts. |
| Template Engine | Load and render templates. |
| Templates | Define the final presentation of generated artifacts. |

---

## General

### AR-001

| Property | Value |
|----------|-------|
| **Since** | Sprint 6 |
| **Status** | Active |
| **Related Principle** | Separation of Business Logic and Presentation |

**Rule**

Generated artifacts must not end with a trailing newline.

**Rationale**

Artifact formatting must remain deterministic regardless of the rendering backend or operating system.

---

### AR-002

| Property | Value |
|----------|-------|
| **Since** | Sprint 7 |
| **Status** | Active |
| **Related Principle** | Immutability by Default |

**Rule**

All domain models must:

- use `@dataclass(frozen=True)`;
- use `slots=True`;
- store collections as immutable tuples;
- contain no business logic.

**Rationale**

Immutable domain models simplify reasoning, improve reliability and reduce unintended side effects.

---

## Generators

### AR-003

| Property | Value |
|----------|-------|
| **Since** | Sprint 7 |
| **Status** | Active |
| **Related Principle** | Layered Architecture |

**Rule**

`artifact_name` stores the logical template name rather than the physical template filename.

Example:

```python
artifact_name = "user_story"
```

instead of

```python
artifact_name = "user_story.md.j2"
```

**Rationale**

Generators remain independent of template storage details while the template engine manages file resolution.

---
## Domain Models

### AR-004

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Single Responsibility Principle |

**Rule**

Domain models describe business entities only.

They must not contain generation logic, rendering logic, validation workflows or infrastructure dependencies.

**Rationale**

Keeping domain models free from implementation concerns allows them to remain reusable across generators, exporters and future integrations.

---

### AR-005

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Layered Architecture |

**Rule**

Relationships between business entities must be expressed through composition whenever practical.

Large monolithic models should be avoided.

**Rationale**

Composition improves readability, reuse and long-term extensibility of the domain model.

---

### AR-006

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Immutability by Default |

**Rule**

Collections exposed by domain models remain immutable throughout the domain layer.

Mutable collections may only be created temporarily while preparing rendering context.

**Rationale**

Immutability guarantees predictable behavior while allowing generators to adapt data to template engines when necessary.

---## Generators

### AR-007

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Single Responsibility Principle |

**Rule**

Generators are responsible only for transforming domain models into rendering contexts.

They must not contain business rules, localization logic or template loading logic.

**Rationale**

Keeping generators focused on context preparation makes them easier to test and allows rendering infrastructure to evolve independently.

---

### AR-008

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Separation of Business Logic and Presentation |

**Rule**

Generators communicate with templates exclusively through context dictionaries.

Templates must never access external services or infrastructure directly.

**Rationale**

A clear contract between generators and templates improves maintainability and keeps presentation independent from implementation details.

---

### AR-009

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Open/Closed Principle (OCP) |

**Rule**

Adding a new artifact generator must not require modifications to existing generators or infrastructure components.

New functionality should be introduced by adding new domain models, templates and generators.

**Rationale**

This preserves extensibility while minimizing regression risk.

---

### AR-010

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | Explicit over Implicit |

**Rule**

Every generator must define a unique logical `artifact_name`.

The value represents the artifact type rather than the template filename.

**Rationale**

Logical identifiers decouple generators from the physical template structure and simplify future changes to template storage.

---

### AR-011

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Related Principle** | KISS |

**Rule**

Generators should perform only minimal data adaptation required by the template engine.

Typical transformations include converting immutable tuples into temporary lists for rendering.

**Rationale**

Keeping generators lightweight prevents business logic from migrating into the presentation layer while avoiding unnecessary abstractions.

---## Template Engine

### AR-012

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Separation of Business Logic and Presentation |

**Rule**

The Template Engine is the only component responsible for rendering templates.

Generators must never render templates directly.

**Rationale**

Centralizing rendering behavior guarantees consistent template processing and isolates presentation infrastructure from business components.

---

### AR-013

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Layered Architecture |

**Rule**

Template loading must be centralized in a dedicated loader component.

Generators must never access the filesystem directly.

**Rationale**

Centralized template loading simplifies maintenance, testing and future support for alternative template sources.

---

### AR-014

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Explicit over Implicit |

**Rule**

Templates are identified by logical names rather than physical filenames.

The mapping between logical names and template files is managed exclusively by the Template Engine.

**Rationale**

This decouples business components from storage details and allows template organization to evolve without affecting generators.

---

### AR-015

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | KISS |

**Rule**

Templates should contain presentation logic only.

Complex business decisions, calculations and conditional workflows belong in Python code.

**Rationale**

Keeping templates declarative improves readability, simplifies localization and reduces duplication.

---

### AR-016

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Evolving |
| **Related Principle** | Open/Closed Principle (OCP) |

**Rule**

The Template Engine should remain extensible without requiring changes to existing generators.

Support for new template formats or rendering backends should be introduced by extending the rendering infrastructure.

**Rationale**

This allows the Toolkit to support additional output formats while preserving compatibility with existing generators.

---## Localization

### AR-017

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Separation of Business Logic and Presentation |
| **Verified By** | LocalizationLoader, TranslationService |

**Rule**

Localization is responsible only for translating user-facing text.

Business logic must remain language-independent.

**Rationale**

Keeping localization independent from business logic prevents duplicated implementations across languages.

---

### AR-018

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Explicit over Implicit |
| **Verified By** | TranslationService |

**Rule**

Technical terminology must remain language-independent.

Only descriptive text may be localized.

**Rationale**

Technical consistency improves documentation quality and reduces ambiguity across supported languages.

---

### AR-019

| Property | Value |
|----------|-------|
| **Since** | Sprint 8 |
| **Status** | Active |
| **Stability** | Stable |
| **Related Principle** | Layered Architecture |

**Rule**

Localization files must remain independent from generators and domain models.

Generators request translations through the localization subsystem rather than accessing locale resources directly.

**Rationale**

Centralizing localization prevents duplication and keeps generators independent from language implementation details.

---## Future Architecture

The following capabilities have been identified as potential future extensions.

They are intentionally not implemented yet in accordance with the YAGNI principle.

Implementation of these features should not require redesign of the existing architecture.

| Planned Capability | Status |
|--------------------|--------|
| UML Generator | Planned |
| OpenAPI Generator | Planned |
| SQL Generator | Planned |
| HTML Export | Planned |
| PDF Export | Planned |
| PlantUML Export | Planned |
| BPMN XML Export | Planned |
| Plugin Architecture | Under Evaluation |
| Automatic Generator Registration | Under Evaluation |

---

## Architecture Evolution

The NovaMarket Toolkit follows an iterative architecture evolution process.

Architectural changes are introduced gradually through development sprints.

Every significant architectural decision follows the same workflow:

1. Sprint Planning
2. Architecture Design
3. Implementation
4. Unit Testing
5. Integration Testing
6. Architecture Review
7. Documentation Update
8. Code Formatting
9. Static Analysis
10. Git Commit
11. GitHub Push
12. Git Tag (for releases only)

Only architectural decisions that have been validated through implementation and testing are added to this document.

This document serves as the primary source of architectural knowledge for the NovaMarket Toolkit.

Architecture Rules (AR) define mandatory engineering conventions.

Future Architecture sections document possible directions without committing the project to premature implementation.

The architecture evolves incrementally while preserving stability, maintainability and extensibility.---

## Document Status

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Created | Sprint 8 |
| Last Updated | Sprint 8 |
| Maintained During | Architecture Review |
