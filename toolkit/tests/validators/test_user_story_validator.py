"""Tests for the UserStoryValidator."""

from __future__ import annotations

import pytest

from novamarket_toolkit.models.user_story import UserStory
from novamarket_toolkit.validators.artifacts.user_story import (
    UserStoryValidator,
)
from novamarket_toolkit.validators.exceptions import ValidationError


def test_validate_valid_user_story() -> None:
    """Accept a valid User Story."""
    validator = UserStoryValidator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
        acceptance_criteria=(
            "Payment succeeds",
            "Order status becomes Paid",
        ),
    )

    validator.validate(story)


def test_reject_empty_actor() -> None:
    """Reject an empty actor."""
    validator = UserStoryValidator()

    story = UserStory(
        actor="",
        action="pay for an order",
        benefit="complete the purchase",
    )

    with pytest.raises(ValidationError):
        validator.validate(story)


def test_reject_empty_action() -> None:
    """Reject an empty action."""
    validator = UserStoryValidator()

    story = UserStory(
        actor="Customer",
        action="",
        benefit="complete the purchase",
    )

    with pytest.raises(ValidationError):
        validator.validate(story)


def test_reject_empty_benefit() -> None:
    """Reject an empty benefit."""
    validator = UserStoryValidator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="",
    )

    with pytest.raises(ValidationError):
        validator.validate(story)


def test_reject_empty_acceptance_criterion() -> None:
    """Reject an empty acceptance criterion."""
    validator = UserStoryValidator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
        acceptance_criteria=(
            "Payment succeeds",
            "",
        ),
    )

    with pytest.raises(ValidationError):
        validator.validate(story)
