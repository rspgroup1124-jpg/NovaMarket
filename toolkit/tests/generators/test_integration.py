"""Integration tests for the generator framework."""

from __future__ import annotations

from novamarket_toolkit.generators.artifacts.user_story import (
    UserStoryGenerator,
)
from novamarket_toolkit.generators.factory import GeneratorFactory
from novamarket_toolkit.generators.registry import GeneratorRegistry
from novamarket_toolkit.models.user_story import UserStory


def test_factory_creates_user_story_generator() -> None:
    """Verify that the factory creates a registered generator."""
    registry = GeneratorRegistry()
    registry.register(UserStoryGenerator)

    factory = GeneratorFactory(registry)

    generator = factory.create("user_story")

    assert isinstance(generator, UserStoryGenerator)


def test_generate_user_story_via_factory() -> None:
    """Generate a User Story using the complete framework."""
    registry = GeneratorRegistry()
    registry.register(UserStoryGenerator)

    factory = GeneratorFactory(registry)
    generator = factory.create("user_story")

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
