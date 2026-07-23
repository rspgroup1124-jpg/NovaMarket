"""Validator for BPMN Process domain models."""

from __future__ import annotations

from novamarket_toolkit.models.bpmn import BPMNProcess
from novamarket_toolkit.validators.base import BaseValidator
from novamarket_toolkit.validators.exceptions import ValidationError


class BPMNValidator(BaseValidator[BPMNProcess]):
    """Validate BPMN Process domain models."""

    artifact_name = "bpmn_process"

    def validate(self, data: BPMNProcess) -> None:
        """
        Validate a BPMN Process domain model.

        Parameters
        ----------
        data
            BPMN Process to validate.

        Raises
        ------
        ValidationError
            If the model contains invalid data.
        """
        if not data.id.strip():
            raise ValidationError("The process 'id' field must not be empty.")

        if not data.name.strip():
            raise ValidationError("The process 'name' field must not be empty.")

        participant_ids: set[str] = set()
        lane_ids: set[str] = set()
        element_ids: set[str] = set()
        flow_ids: set[str] = set()

        for participant in data.participants:
            if not participant.id.strip():
                raise ValidationError("Participant 'id' must not be empty.")

            if not participant.name.strip():
                raise ValidationError("Participant 'name' must not be empty.")

            if participant.id in participant_ids:
                raise ValidationError(f"Duplicate participant id '{participant.id}'.")

            participant_ids.add(participant.id)

        for lane in data.lanes:
            if not lane.id.strip():
                raise ValidationError("Lane 'id' must not be empty.")

            if not lane.name.strip():
                raise ValidationError("Lane 'name' must not be empty.")

            if lane.id in lane_ids:
                raise ValidationError(f"Duplicate lane id '{lane.id}'.")

            lane_ids.add(lane.id)

        for element in data.elements:
            if not element.id.strip():
                raise ValidationError("Element 'id' must not be empty.")

            if not element.name.strip():
                raise ValidationError("Element 'name' must not be empty.")

            if element.id in element_ids:
                raise ValidationError(f"Duplicate element id '{element.id}'.")

            element_ids.add(element.id)

        for flow in data.sequence_flows:
            if not flow.id.strip():
                raise ValidationError("Sequence Flow 'id' must not be empty.")

            if flow.id in flow_ids:
                raise ValidationError(f"Duplicate sequence flow id '{flow.id}'.")

            flow_ids.add(flow.id)

            if flow.source not in element_ids:
                raise ValidationError(
                    f"Sequence Flow '{flow.id}' references " f"unknown source '{flow.source}'."
                )

            if flow.target not in element_ids:
                raise ValidationError(
                    f"Sequence Flow '{flow.id}' references " f"unknown target '{flow.target}'."
                )
