"""User Story artifact generator."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.models.user_story import UserStory


class UserStoryGenerator(BaseGenerator[UserStory]):
    """Generate a User Story from a domain model."""

    artifact_name = "user_story"

    def generate(self, data: UserStory) -> str:
        """
        Generate a formatted User Story.

        Parameters
        ----------
        data:
            User Story domain model.

        Returns
        -------
        str
            Generated User Story.
        """
        lines: list[str] = [
            "User Story",
            "",
            f"As a {data.actor},",
            f"I want to {data.action},",
            f"so that I can {data.benefit}.",
        ]

        if data.acceptance_criteria:
            lines.extend(
                [
                    "",
                    "Acceptance Criteria",
                    *self._generate_acceptance_criteria(data.acceptance_criteria),
                ]
            )

        if data.notes:
            lines.extend(
                [
                    "",
                    "Notes",
                    data.notes,
                ]
            )

        return "\n".join(lines)

    @staticmethod
    def _generate_acceptance_criteria(
        criteria: tuple[str, ...],
    ) -> list[str]:
        """
        Format acceptance criteria.

        Parameters
        ----------
        criteria:
            Acceptance criteria.

        Returns
        -------
        list[str]
            Formatted acceptance criteria.
        """
        return [f"- {criterion}" for criterion in criteria]
