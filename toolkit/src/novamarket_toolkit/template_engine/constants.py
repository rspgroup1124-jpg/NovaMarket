"""Constants used by the template engine."""

from __future__ import annotations

from pathlib import Path

TEMPLATES_DIRECTORY = "templates"

DEFAULT_TEMPLATE_SUFFIX = ".md.j2"

DEFAULT_ENCODING = "utf-8"

PACKAGE_DIRECTORY = Path(__file__).resolve().parent

TEMPLATES_PATH = PACKAGE_DIRECTORY / TEMPLATES_DIRECTORY
