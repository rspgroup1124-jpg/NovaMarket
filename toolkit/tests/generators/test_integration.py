"""Integration tests for the generator framework."""

from __future__ import annotations

from novamarket_toolkit.generators.artifacts.use_case import (
    UseCaseGenerator,
)
from novamarket_toolkit.generators.artifacts.user_story import (
    UserStoryGenerator,
)
from novamarket_toolkit.generators.factory import GeneratorFactory
from novamarket_toolkit.generators.registry import GeneratorRegistry
from novamarket_toolkit.models import UseCase, UserStory


def test_factory_creates_user_story_generator() -> None:
    """Verify that the factory creates a User Story generator."""
    registry = GeneratorRegistry()
    registry.register(UserStoryGenerator)

    factory = GeneratorFactory(registry)

    generator = factory.create("user_story")

    assert isinstance(generator, UserStoryGenerator)


def test_factory_creates_use_case_generator() -> None:
    """Verify that the factory creates a Use Case generator."""
    registry = GeneratorRegistry()
    registry.register(UseCaseGenerator)

    factory = GeneratorFactory(registry)

    generator = factory.create("use_case")

    assert isinstance(generator, UseCaseGenerator)


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


def test_generate_use_case_via_factory() -> None:
    """Generate a Use Case using the complete framework."""
    registry = GeneratorRegistry()
    registry.register(UseCaseGenerator)

    factory = GeneratorFactory(registry)
    generator = factory.create("use_case")

    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
        main_flow=(
            "User enters credentials.",
            "System validates credentials.",
            "System grants access.",
        ),
    )

    result = generator.generate(use_case)

    expected = (
        "Use Case\n"
        "\n"
        "Title\n"
        "Login\n"
        "\n"
        "Goal\n"
        "User signs in.\n"
        "\n"
        "Primary Actor\n"
        "User\n"
        "\n"
        "Main Flow\n"
        "1. User enters credentials.\n"
        "2. System validates credentials.\n"
        "3. System grants access."
    )

    assert result == expected
