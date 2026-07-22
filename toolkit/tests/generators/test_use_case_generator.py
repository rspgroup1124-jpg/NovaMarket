"""Tests for the UseCaseGenerator."""

from __future__ import annotations

from novamarket_toolkit.generators.artifacts.use_case import (
    UseCaseGenerator,
)
from novamarket_toolkit.models import UseCase


def test_generate_use_case() -> None:
    """Generate a complete Use Case."""
    generator = UseCaseGenerator()

    use_case = UseCase(
        title="Pay for Order",
        goal="Customer successfully pays for an order.",
        primary_actor="Customer",
        secondary_actors=(
            "Payment Gateway",
            "Notification Service",
        ),
        preconditions=(
            "Customer is authenticated",
            "Shopping cart is not empty",
        ),
        postconditions=(
            "Order status becomes Paid",
            "Receipt is generated",
        ),
        main_flow=(
            "Customer opens checkout.",
            "Customer enters payment details.",
            "System validates payment.",
            "Payment is authorized.",
            "Order status becomes Paid.",
        ),
        alternative_flows=(
            "Payment is declined.",
            "Network timeout.",
        ),
        notes="Requires active payment provider.",
    )

    result = generator.generate(use_case)

    expected = (
        "Use Case\n"
        "\n"
        "Title\n"
        "Pay for Order\n"
        "\n"
        "Goal\n"
        "Customer successfully pays for an order.\n"
        "\n"
        "Primary Actor\n"
        "Customer\n"
        "\n"
        "Secondary Actors\n"
        "- Payment Gateway\n"
        "- Notification Service\n"
        "\n"
        "Preconditions\n"
        "- Customer is authenticated\n"
        "- Shopping cart is not empty\n"
        "\n"
        "Main Flow\n"
        "1. Customer opens checkout.\n"
        "2. Customer enters payment details.\n"
        "3. System validates payment.\n"
        "4. Payment is authorized.\n"
        "5. Order status becomes Paid.\n"
        "\n"
        "Alternative Flows\n"
        "- Payment is declined.\n"
        "- Network timeout.\n"
        "\n"
        "Postconditions\n"
        "- Order status becomes Paid\n"
        "- Receipt is generated\n"
        "\n"
        "Notes\n"
        "Requires active payment provider."
    )

    assert result == expected


def test_generate_minimal_use_case() -> None:
    """Generate a Use Case with only required fields."""
    generator = UseCaseGenerator()

    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
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
        "User"
    )

    assert result == expected
