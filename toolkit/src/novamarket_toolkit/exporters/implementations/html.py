"""HTML artifact exporter."""

from __future__ import annotations

import html

from novamarket_toolkit.exporters.base import BaseExporter


class HtmlExporter(BaseExporter):
    """Export artifacts as HTML."""

    format_name = "html"

    def export(self, content: str) -> str:
        """
        Export content as HTML.

        Parameters
        ----------
        content
            Generated artifact.

        Returns
        -------
        str
            HTML representation of the artifact.
        """
        escaped = html.escape(content)

        return (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            '    <meta charset="UTF-8">\n'
            "    <title>NovaMarket Toolkit Export</title>\n"
            "</head>\n"
            "<body>\n"
            f"<pre>{escaped}</pre>\n"
            "</body>\n"
            "</html>\n"
        )
