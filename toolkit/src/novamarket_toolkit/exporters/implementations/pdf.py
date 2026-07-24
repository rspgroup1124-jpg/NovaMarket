"""PDF artifact exporter."""

from __future__ import annotations

from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from novamarket_toolkit.exporters.base import BaseExporter


class PdfExporter(BaseExporter):
    """Export artifacts as PDF."""

    format_name = "pdf"

    def export(self, content: str) -> bytes:
        """
        Export content as a PDF document.

        Parameters
        ----------
        content
            Generated artifact.

        Returns
        -------
        bytes
            PDF document as bytes.
        """
        buffer = BytesIO()

        document = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        story = []

        for line in content.splitlines():
            story.append(Paragraph(line, styles["BodyText"]))

        document.build(story)

        return buffer.getvalue()
