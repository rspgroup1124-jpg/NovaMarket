"""Tests for the UseCase domain model."""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from novamarket_toolkit.models import UseCase


def test_create_use_case() -> None:
    """A UseCase instance is created correctly."""
    use_case = UseCase(
        title="Pay for Order",
        goal="Customer pays for an order.",
        primary_actor="Customer",
        secondary_actors=("Payment Gateway",),
        preconditions=("Customer is authenticated",),
        postconditions=("Order is paid",),
        main_flow=(
            "Customer opens checkout.",
            "Customer confirms payment.",
        ),
        alternative_flows=("Payment is declined.",),
        notes="Requires active payment provider.",
    )

    assert use_case.title == "Pay for Order"
    assert use_case.goal == "Customer pays for an order."
    assert use_case.primary_actor == "Customer"
    assert use_case.secondary_actors == ("Payment Gateway",)
    assert use_case.preconditions == ("Customer is authenticated",)
    assert use_case.postconditions == ("Order is paid",)
    assert use_case.main_flow == (
        "Customer opens checkout.",
        "Customer confirms payment.",
    )
    assert use_case.alternative_flows == ("Payment is declined.",)
    assert use_case.notes == "Requires active payment provider."


def test_default_values() -> None:
    """Optional fields use default values."""
    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
    )

    assert use_case.secondary_actors == ()
    assert use_case.preconditions == ()
    assert use_case.postconditions == ()
    assert use_case.main_flow == ()
    assert use_case.alternative_flows == ()
    assert use_case.notes is None


def test_use_case_is_immutable() -> None:
    """UseCase is immutable."""
    use_case = UseCase(
        title="Login",
        goal="User signs in.",
        primary_actor="User",
    )

    with pytest.raises(FrozenInstanceError):
        use_case.title = "Logout"
