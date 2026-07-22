"""Use Case artifact generator."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.models.use_case import UseCase
from novamarket_toolkit.template_engine import TemplateEngine


class UseCaseGenerator(BaseGenerator[UseCase]):
    """Generate a Use Case from a domain model."""

    artifact_name = "use_case"

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

    def generate(self, data: UseCase) -> str:
        """
        Generate a formatted Use Case.

        Parameters
        ----------
        data
            Use Case domain model.

        Returns
        -------
        str
            Generated Use Case.
        """
        context = {
            "title": data.title,
            "goal": data.goal,
            "primary_actor": data.primary_actor,
            "secondary_actors": list(data.secondary_actors),
            "preconditions": list(data.preconditions),
            "postconditions": list(data.postconditions),
            "main_flow": list(data.main_flow),
            "alternative_flows": list(data.alternative_flows),
            "notes": data.notes,
        }

        return self._template_engine.render(
            template_name=self.artifact_name,
            context=context,
        )
