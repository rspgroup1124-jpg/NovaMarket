"""Domain models for BPMN processes."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ElementType(StrEnum):
    """Supported BPMN element types."""

    EVENT = "event"
    ACTIVITY = "activity"
    GATEWAY = "gateway"
    DATA_OBJECT = "data_object"
    ARTIFACT = "artifact"


class EventType(StrEnum):
    """Supported BPMN event types."""

    START = "start"
    INTERMEDIATE = "intermediate"
    END = "end"


class GatewayType(StrEnum):
    """Supported BPMN gateway types."""

    EXCLUSIVE = "exclusive"
    PARALLEL = "parallel"
    INCLUSIVE = "inclusive"
    EVENT_BASED = "event_based"
    COMPLEX = "complex"


class ActivityType(StrEnum):
    """Supported BPMN activity types."""

    TASK = "task"
    SUB_PROCESS = "sub_process"


@dataclass(frozen=True, slots=True)
class BPMNEntity:
    """
    Base class for BPMN entities.

    Parameters
    ----------
    id:
        Unique entity identifier.
    name:
        Human-readable entity name.
    documentation:
        Optional documentation text.
    """

    id: str
    name: str
    documentation: str | None = None


@dataclass(frozen=True, slots=True)
class BPMNElement(BPMNEntity):
    """
    Base class for BPMN flow elements.

    Parameters
    ----------
    element_type:
        BPMN element category.
    """

    element_type: ElementType = field(init=False)


@dataclass(frozen=True, slots=True)
class BPMNEvent(BPMNElement):
    """
    BPMN event.

    Parameters
    ----------
    event_type:
        Type of BPMN event.
    """

    element_type: ElementType = field(
        init=False,
        default=ElementType.EVENT,
    )
    event_type: EventType = EventType.INTERMEDIATE


@dataclass(frozen=True, slots=True)
class BPMNActivity(BPMNElement):
    """
    BPMN activity.

    Parameters
    ----------
    activity_type:
        Type of BPMN activity.
    """

    element_type: ElementType = field(
        init=False,
        default=ElementType.ACTIVITY,
    )
    activity_type: ActivityType = ActivityType.TASK


@dataclass(frozen=True, slots=True)
class BPMNGateway(BPMNElement):
    """
    BPMN gateway.

    Parameters
    ----------
    gateway_type:
        Gateway behavior.
    """

    element_type: ElementType = field(
        init=False,
        default=ElementType.GATEWAY,
    )
    gateway_type: GatewayType = GatewayType.EXCLUSIVE


@dataclass(frozen=True, slots=True)
class BPMNDataObject(BPMNElement):
    """BPMN data object."""

    element_type: ElementType = field(
        init=False,
        default=ElementType.DATA_OBJECT,
    )


@dataclass(frozen=True, slots=True)
class BPMNArtifact(BPMNElement):
    """BPMN artifact."""

    element_type: ElementType = field(
        init=False,
        default=ElementType.ARTIFACT,
    )


@dataclass(frozen=True, slots=True)
class BPMNConnection:
    """
    Base class for BPMN connections.

    Parameters
    ----------
    id:
        Unique connection identifier.
    source:
        Identifier of the source element.
    target:
        Identifier of the target element.
    """

    id: str
    source: str
    target: str


@dataclass(frozen=True, slots=True)
class SequenceFlow(BPMNConnection):
    """
    BPMN sequence flow.

    Parameters
    ----------
    condition:
        Optional condition expression.
    """

    condition: str | None = None


@dataclass(frozen=True, slots=True)
class Participant(BPMNEntity):
    """BPMN participant (pool)."""


@dataclass(frozen=True, slots=True)
class Lane(BPMNEntity):
    """
    BPMN lane.

    Parameters
    ----------
    element_ids:
        Identifiers of BPMN elements assigned to the lane.
    """

    element_ids: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class BPMNProcess(BPMNEntity):
    """
    Root BPMN process model.

    Parameters
    ----------
    participants:
        Process participants.
    lanes:
        Process lanes.
    elements:
        BPMN flow elements.
    sequence_flows:
        Sequence flows connecting BPMN elements.
    """

    participants: tuple[Participant, ...] = ()
    lanes: tuple[Lane, ...] = ()
    elements: tuple[BPMNElement, ...] = ()
    sequence_flows: tuple[SequenceFlow, ...] = ()
