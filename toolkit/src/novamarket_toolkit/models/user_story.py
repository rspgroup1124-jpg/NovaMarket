"""User Story domain model."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class UserStory:
    """
    Represent a User Story artifact.

    Parameters
    ----------
    actor:
        The role performing the action.
    action:
        The action the actor wants to perform.
    benefit:
        The value gained by performing the action.
    acceptance_criteria:
        Acceptance criteria for the story.
    notes:
        Optional implementation notes.
    """

    actor: str
    action: str
    benefit: str
    acceptance_criteria: tuple[str, ...] = field(default_factory=tuple)
    notes: str | None = None
