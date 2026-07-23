"""Tests for the UseCaseValidator."""

from __future__ import annotations

import pytest

from novamarket_toolkit.models import UseCase
from novamarket_toolkit.validators.artifacts.use_case import (
    UseCaseValidator,
)
from novamarket_toolkit.validators.exceptions import ValidationError


def test_validate_valid_use_case() -> None:
    """Accept a valid Use Case."""
    validator = UseCaseValidator()

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

    validator.validate(use_case)


def test_validate_minimal_use_case() -> None:
    """Accept a Use Case containing only required fields."""
    validator = UseCaseValidator()

    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
    )

    validator.validate(use_case)


def test_reject_empty_title() -> None:
    """Reject an empty title."""
    validator = UseCaseValidator()

    use_case = UseCase(
        title="",
        goal="User signs in.",
        primary_actor="User",
    )

    with pytest.raises(ValidationError):
        validator.validate(use_case)


def test_reject_empty_goal() -> None:
    """Reject an empty goal."""
    validator = UseCaseValidator()

    use_case = UseCase(
        title="Login",
        goal="",
        primary_actor="User",
    )

    with pytest.raises(ValidationError):
        validator.validate(use_case)


def test_reject_empty_primary_actor() -> None:
    """Reject an empty primary actor."""
    validator = UseCaseValidator()

    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="",
    )

    with pytest.raises(ValidationError):
        validator.validate(use_case)


def test_reject_empty_main_flow_step() -> None:
    """Reject an empty main flow step."""
    validator = UseCaseValidator()

    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
        main_flow=(
            "User opens the login page.",
            "",
        ),
    )

    with pytest.raises(ValidationError):
        validator.validate(use_case)
