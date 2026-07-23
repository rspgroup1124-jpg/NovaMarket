"""Validator for User Story domain models."""

from __future__ import annotations

from novamarket_toolkit.models.user_story import UserStory
from novamarket_toolkit.validators.base import BaseValidator
from novamarket_toolkit.validators.exceptions import ValidationError


class UserStoryValidator(BaseValidator[UserStory]):
    """Validate User Story domain models."""

    artifact_name = "user_story"

    def validate(self, data: UserStory) -> None:
        """
        Validate a User Story domain model.

        Parameters
        ----------
        data
            User Story to validate.

        Raises
        ------
        ValidationError
            If the model contains invalid data.
        """
        if not data.actor.strip():
            raise ValidationError("The 'actor' field must not be empty.")

        if not data.action.strip():
            raise ValidationError("The 'action' field must not be empty.")

        if not data.benefit.strip():
            raise ValidationError("The 'benefit' field must not be empty.")

        for criterion in data.acceptance_criteria:
            if not criterion.strip():
                raise ValidationError("Acceptance criteria must not contain empty items.")
