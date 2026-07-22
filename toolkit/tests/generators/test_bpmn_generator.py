"""Tests for the BPMNGenerator."""

from __future__ import annotations

from novamarket_toolkit.generators.artifacts.bpmn import BPMNGenerator
from novamarket_toolkit.models.bpmn import (
    BPMNActivity,
    BPMNEvent,
    BPMNProcess,
    Participant,
    SequenceFlow,
)


def test_generate_bpmn_process() -> None:
    """Generate a complete BPMN process."""
    generator = BPMNGenerator()

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

    result = generator.generate(process)

    expected = (
        "Process: Order Payment\n"
        "Description:\n"
        "Customer pays for an order.\n"
        "\n"
        "Participants:\n"
        "- Customer\n"
        "\n"
        "Lanes:\n"
        "- None\n"
        "\n"
        "Elements:\n"
        "- start (event): Start\n"
        "- pay (activity): Pay Order\n"
        "\n"
        "Sequence Flows:\n"
        "- start -> pay"
    )

    assert result == expected


def test_generate_without_participants() -> None:
    """Render placeholder when no participants exist."""
    generator = BPMNGenerator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
    )

    result = generator.generate(process)

    assert "Participants:" in result
    assert "- None" in result


def test_generate_without_lanes() -> None:
    """Render placeholder when no lanes exist."""
    generator = BPMNGenerator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
    )

    result = generator.generate(process)

    assert "Lanes:" in result
    assert "- None" in result


def test_generate_without_sequence_flows() -> None:
    """Render placeholder when no sequence flows exist."""
    generator = BPMNGenerator()

    process = BPMNProcess(
        id="process_1",
        name="Order Payment",
    )

    result = generator.generate(process)

    assert "Sequence Flows:" in result
    assert "- None" in result
