"""Tests for the UserStoryGenerator."""

from __future__ import annotations

from novamarket_toolkit.generators.artifacts.user_story import (
    UserStoryGenerator,
)
from novamarket_toolkit.models.user_story import UserStory


def test_generate_user_story() -> None:
    """Generate a complete User Story."""
    generator = UserStoryGenerator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
        acceptance_criteria=(
            "Payment succeeds",
            "Order status becomes Paid",
        ),
    )

    result = generator.generate(story)

    expected = (
        "User Story\n"
        "\n"
        "As a Customer,\n"
        "I want to pay for an order,\n"
        "so that I can complete the purchase.\n"
        "\n"
        "Acceptance Criteria\n"
        "- Payment succeeds\n"
        "- Order status becomes Paid"
    )

    assert result == expected


def test_generate_without_acceptance_criteria() -> None:
    """Do not render Acceptance Criteria when none are provided."""
    generator = UserStoryGenerator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
    )

    result = generator.generate(story)

    assert "Acceptance Criteria" not in result


def test_generate_with_notes() -> None:
    """Render Notes section when notes are provided."""
    generator = UserStoryGenerator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
        notes="Available in MVP",
    )

    result = generator.generate(story)

    assert "Notes" in result
    assert "Available in MVP" in result


def test_generate_without_notes() -> None:
    """Do not render Notes section when notes are not provided."""
    generator = UserStoryGenerator()

    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
    )

    result = generator.generate(story)

    assert "Notes" not in result
