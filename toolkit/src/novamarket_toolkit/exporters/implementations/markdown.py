"""Markdown artifact exporter."""

from __future__ import annotations

from novamarket_toolkit.exporters.base import BaseExporter


class MarkdownExporter(BaseExporter):
    """Export artifacts as Markdown."""

    format_name = "markdown"

    def export(self, content: str) -> str:
        """
        Export content as Markdown.

        Parameters
        ----------
        content
            Generated artifact.

        Returns
        -------
        str
            Markdown representation of the artifact.
        """
        return content
