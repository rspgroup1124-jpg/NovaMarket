"""Domain model for a Use Case."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UseCase:
    """
    Represent a Use Case domain model.

    Parameters
    ----------
    title
        Use Case title.
    goal
        Business goal of the Use Case.
    primary_actor
        Main actor initiating the Use Case.
    secondary_actors
        Supporting actors participating in the Use Case.
    preconditions
        Conditions that must be satisfied before execution.
    postconditions
        Conditions that are true after successful completion.
    main_flow
        Main success scenario.
    alternative_flows
        Alternative execution scenarios.
    notes
        Optional implementation or business notes.
    """

    title: str
    goal: str
    primary_actor: str
    secondary_actors: tuple[str, ...] = ()
    preconditions: tuple[str, ...] = ()
    postconditions: tuple[str, ...] = ()
    main_flow: tuple[str, ...] = ()
    alternative_flows: tuple[str, ...] = ()
    notes: str | None = None
