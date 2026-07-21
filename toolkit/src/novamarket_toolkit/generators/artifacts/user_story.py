"""User Story artifact generator."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.models.user_story import UserStory
from novamarket_toolkit.template_engine import TemplateEngine


class UserStoryGenerator(BaseGenerator[UserStory]):
    """Generate a User Story from a domain model."""

    artifact_name = "user_story"

    def __init__(
        self,
        locale: str = "en",
        template_engine: TemplateEngine | None = None,
    ) -> None:
        """
        Initialize the generator.

        Parameters
        ----------
        locale
            Template locale.
        template_engine
            Template engine instance. If omitted, a default
            TemplateEngine is created.
        """
        self._template_engine = template_engine or TemplateEngine(locale=locale)

    def generate(self, data: UserStory) -> str:
        """
        Generate a formatted User Story.

        Parameters
        ----------
        data
            User Story domain model.

        Returns
        -------
        str
            Generated User Story.
        """
        context = {
            "role": data.actor,
            "goal": data.action,
            "benefit": data.benefit,
            "acceptance_criteria": list(data.acceptance_criteria),
            "notes": data.notes,
        }

        return self._template_engine.render(
            template_name=self.artifact_name,
            context=context,
        )
