"""Validator for Use Case domain models."""

from __future__ import annotations

from novamarket_toolkit.models.use_case import UseCase
from novamarket_toolkit.validators.base import BaseValidator
from novamarket_toolkit.validators.exceptions import ValidationError


class UseCaseValidator(BaseValidator[UseCase]):
    """Validate Use Case domain models."""

    artifact_name = "use_case"

    def validate(self, data: UseCase) -> None:
        """
        Validate a Use Case domain model.

        Parameters
        ----------
        data
            Use Case to validate.

        Raises
        ------
        ValidationError
            If the model contains invalid data.
        """
        if not data.title.strip():
            raise ValidationError("The 'title' field must not be empty.")

        if not data.goal.strip():
            raise ValidationError("The 'goal' field must not be empty.")

        if not data.primary_actor.strip():
            raise ValidationError("The 'primary_actor' field must not be empty.")

        for actor in data.secondary_actors:
            if not actor.strip():
                raise ValidationError("Secondary actors must not contain empty items.")

        for precondition in data.preconditions:
            if not precondition.strip():
                raise ValidationError("Preconditions must not contain empty items.")

        for postcondition in data.postconditions:
            if not postcondition.strip():
                raise ValidationError("Postconditions must not contain empty items.")

        for step in data.main_flow:
            if not step.strip():
                raise ValidationError("Main flow must not contain empty items.")

        for step in data.alternative_flows:
            if not step.strip():
                raise ValidationError("Alternative flows must not contain empty items.")
