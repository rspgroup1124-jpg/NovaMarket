"""BPMN Process artifact generator."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.models.bpmn import BPMNProcess
from novamarket_toolkit.template_engine import TemplateEngine


class BPMNGenerator(BaseGenerator[BPMNProcess]):
    """Generate a BPMN Process from a domain model."""

    artifact_name = "bpmn_process"

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

    def generate(self, data: BPMNProcess) -> str:
        """
        Generate a formatted BPMN Process.

        Parameters
        ----------
        data
            BPMN Process domain model.

        Returns
        -------
        str
            Generated BPMN Process.
        """
        context = {
            "process": data,
            "participants": list(data.participants),
            "lanes": list(data.lanes),
            "elements": list(data.elements),
            "sequence_flows": list(data.sequence_flows),
        }

        return self._template_engine.render(
            template_name=self.artifact_name,
            context=context,
        )
