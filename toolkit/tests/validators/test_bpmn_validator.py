"""Tests for the BPMNValidator."""

from __future__ import annotations

import pytest

from novamarket_toolkit.models.bpmn import (
    BPMNActivity,
    BPMNEvent,
    BPMNProcess,
    Participant,
    SequenceFlow,
)
from novamarket_toolkit.validators.artifacts.bpmn import BPMNValidator
from novamarket_toolkit.validators.exceptions import ValidationError


def test_validate_valid_bpmn_process() -> None:
    """Accept a valid BPMN process."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
        documentation="Customer pays for an order.",
        participants=(
            Participant(
                id="participant_1",
                name="Customer",
            ),
        ),
        elements=(
            BPMNEvent(
                id="start",
                name="Start",
            ),
            BPMNActivity(
                id="pay",
                name="Pay Order",
            ),
        ),
        sequence_flows=(
            SequenceFlow(
                id="flow_1",
                source="start",
                target="pay",
            ),
        ),
    )

    validator.validate(process)


def test_validate_minimal_bpmn_process() -> None:
    """Accept a BPMN process containing only required fields."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
    )

    validator.validate(process)


def test_reject_empty_process_id() -> None:
    """Reject an empty process identifier."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="",
        name="Order Payment",
    )

    with pytest.raises(ValidationError):
        validator.validate(process)


def test_reject_empty_process_name() -> None:
    """Reject an empty process name."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="",
    )

    with pytest.raises(ValidationError):
        validator.validate(process)


def test_reject_duplicate_element_ids() -> None:
    """Reject duplicate BPMN element identifiers."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
        elements=(
            BPMNEvent(
                id="duplicate",
                name="Start",
            ),
            BPMNActivity(
                id="duplicate",
                name="Pay Order",
            ),
        ),
    )

    with pytest.raises(ValidationError):
        validator.validate(process)


def test_reject_unknown_sequence_flow_source() -> None:
    """Reject a sequence flow with an unknown source."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
        elements=(
            BPMNActivity(
                id="pay",
                name="Pay Order",
            ),
        ),
        sequence_flows=(
            SequenceFlow(
                id="flow_1",
                source="start",
                target="pay",
            ),
        ),
    )

    with pytest.raises(ValidationError):
        validator.validate(process)


def test_reject_unknown_sequence_flow_target() -> None:
    """Reject a sequence flow with an unknown target."""
    validator = BPMNValidator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
        elements=(
            BPMNEvent(
                id="start",
                name="Start",
            ),
        ),
        sequence_flows=(
            SequenceFlow(
                id="flow_1",
                source="start",
                target="pay",
            ),
        ),
    )

    with pytest.raises(ValidationError):
        validator.validate(process)
