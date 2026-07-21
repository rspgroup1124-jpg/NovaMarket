"""Template rendering engine for the NovaMarket Toolkit."""

from __future__ import annotations

from typing import Any

from jinja2 import TemplateError

from novamarket_toolkit.template_engine.exceptions import (
    TemplateRenderError,
)
from novamarket_toolkit.template_engine.loader import TemplateLoader


class TemplateEngine:
    """Render toolkit artifacts using Jinja2 templates."""

    def __init__(
        self,
        locale: str,
        loader: TemplateLoader | None = None,
    ) -> None:
        """
        Initialize the template engine.

        Parameters
        ----------
        locale
            Template locale.
        loader
            Template loader instance. If omitted, a default
            ``TemplateLoader`` is created.
        """
        self._locale = locale
        self._loader = loader or TemplateLoader()

    @property
    def locale(self) -> str:
        """
        Return the configured locale.

        Returns
        -------
        str
            Current template locale.
        """
        return self._locale

    def render(
        self,
        template_name: str,
        context: dict[str, Any],
    ) -> str:
        """
        Render a template using the provided context.

        Parameters
        ----------
        template_name
            Logical template name.
        context
            Template rendering context.

        Returns
        -------
        str
            Rendered template.

        Raises
        ------
        TemplateRenderError
            If template rendering fails.
        """
        template = self._loader.load(
            template_name=template_name,
            locale=self._locale,
        )

        try:
            return template.render(**context).rstrip("\n")
        except TemplateError as error:
            raise TemplateRenderError(f"Failed to render template '{template_name}'.") from error
