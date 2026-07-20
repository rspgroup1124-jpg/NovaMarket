"""Load localization resources for NovaMarket Toolkit."""

from __future__ import annotations

import json
from pathlib import Path

from novamarket_toolkit.i18n.exceptions import (
    GlossaryNotFoundError,
    InvalidLocalizationFileError,
    LocaleNotFoundError,
)


class LocalizationLoader:
    """Load localization files and the technical glossary."""

    def __init__(self) -> None:
        """Initialize paths to localization resources."""

        package_root = Path(__file__).resolve().parent.parent

        self._locales_dir = package_root / "locales"
        self._glossary_dir = package_root / "glossary"

    def load_locale(self, locale: str) -> dict[str, str]:
        """Load a localization dictionary."""

        file_path = self._locales_dir / f"{locale}.json"

        if not file_path.exists():
            raise LocaleNotFoundError(f"Locale '{locale}' was not found: {file_path}")

        return self._read_json(file_path)

    def load_terms(self) -> dict[str, str]:
        """Load the technical glossary."""

        file_path = self._glossary_dir / "terms.json"

        if not file_path.exists():
            raise GlossaryNotFoundError(f"Glossary was not found: {file_path}")

        return self._read_json(file_path)

    def _read_json(self, file_path: Path) -> dict[str, str]:
        """Read a JSON file and validate its structure."""

        try:
            with file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

        except json.JSONDecodeError as error:
            raise InvalidLocalizationFileError(f"Invalid JSON: {file_path}") from error

        if not isinstance(data, dict):
            raise InvalidLocalizationFileError(f"Root element must be a JSON object: {file_path}")

        if not all(isinstance(key, str) and isinstance(value, str) for key, value in data.items()):
            raise InvalidLocalizationFileError(
                f"JSON must contain only string keys and string values: {file_path}"
            )

        return data
