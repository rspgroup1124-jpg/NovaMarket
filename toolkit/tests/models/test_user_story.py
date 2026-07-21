"""Tests for the UserStory domain model."""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from novamarket_toolkit.models.user_story import UserStory


def test_create_user_story() -> None:
    """Verify that a UserStory is created correctly."""
    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
        acceptance_criteria=(
            "Payment succeeds",
            "Order status becomes Paid",
        ),
        notes="Available in MVP",
    )

    assert story.actor == "Customer"
    assert story.action == "pay for an order"
    assert story.benefit == "complete the purchase"
    assert story.acceptance_criteria == (
        "Payment succeeds",
        "Order status becomes Paid",
    )
    assert story.notes == "Available in MVP"


def test_default_values() -> None:
    """Verify default values for optional fields."""
    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
    )

    assert story.acceptance_criteria == ()
    assert story.notes is None


def test_user_story_is_immutable() -> None:
    """Verify that UserStory instances are immutable."""
    story = UserStory(
        actor="Customer",
        action="pay for an order",
        benefit="complete the purchase",
    )

    with pytest.raises(FrozenInstanceError):
        story.actor = "Administrator"
