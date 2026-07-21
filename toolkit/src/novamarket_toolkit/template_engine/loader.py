"""Template loader for the NovaMarket Toolkit."""

from __future__ import annotations

from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound

from novamarket_toolkit.template_engine.constants import (
    DEFAULT_TEMPLATE_SUFFIX,
    TEMPLATES_PATH,
)
from novamarket_toolkit.template_engine.exceptions import TemplateNotFoundError


class TemplateLoader:
    """Load Jinja2 templates from the toolkit template directory."""

    def __init__(self) -> None:
        """
        Initialize the template loader.

        A single Jinja2 environment is created during initialization
        and reused for all template loading operations.
        """
        self._environment = self._create_environment()

    def load(self, template_name: str, locale: str) -> Template:
        """
        Load a template by name and locale.

        Parameters
        ----------
        template_name
            Logical template name without file extension.
        locale
            Locale directory (for example: "en", "ru", or "uk").

        Returns
        -------
        Template
            Loaded Jinja2 template.

        Raises
        ------
        TemplateNotFoundError
            If the requested template does not exist.
        """
        template_path = f"{locale}/" f"{template_name}" f"{DEFAULT_TEMPLATE_SUFFIX}"

        try:
            return self._environment.get_template(template_path)
        except TemplateNotFound as error:
            raise TemplateNotFoundError(f"Template '{template_path}' was not found.") from error

    @staticmethod
    def _create_environment() -> Environment:
        """
        Create the Jinja2 environment.

        Returns
        -------
        Environment
            Configured Jinja2 environment.
        """
        return Environment(
            loader=FileSystemLoader(TEMPLATES_PATH),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )
