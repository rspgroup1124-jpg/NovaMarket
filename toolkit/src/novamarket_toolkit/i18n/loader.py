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
        """Initialize loader paths."""

        package_root = Path(__file__).resolve().parent.parent

        self._locale_dir = package_root / "locales"
        self._glossary_dir = package_root / "glossary"

    def load_locale(self, locale: str) -> dict[str, str]:
        """
        Load a locale JSON file.

        Parameters
        ----------
        locale:
            Locale name (for example: "en", "ru", "uk").

        Returns
        -------
        dict[str, str]
            Flattened localization dictionary.
        """

        file_path = self._locale_dir / f"{locale}.json"

        if not file_path.exists():
            raise LocaleNotFoundError(f"Locale '{locale}' was not found: {file_path}")

        return self._read_json(file_path)

    def load_terms(self) -> dict[str, str]:
        """
        Load the technical glossary.

        Returns
        -------
        dict[str, str]
            Flattened glossary dictionary.
        """

        file_path = self._glossary_dir / "terms.json"

        if not file_path.exists():
            raise GlossaryNotFoundError(f"Glossary was not found: {file_path}")

        return self._read_json(file_path)

    def _read_json(self, file_path: Path) -> dict[str, str]:
        """
        Read and validate a JSON localization file.

        Parameters
        ----------
        file_path:
            Path to the JSON file.

        Returns
        -------
        dict[str, str]
            Flattened localization dictionary.
        """

        try:
            with file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

        except json.JSONDecodeError as error:
            raise InvalidLocalizationFileError(f"Invalid JSON: {file_path}") from error

        if not isinstance(data, dict):
            raise InvalidLocalizationFileError(f"Root element must be an object: {file_path}")

        flattened: dict[str, str] = {}

        self._flatten_dict(
            data=data,
            result=flattened,
            file_path=file_path,
        )

        return flattened

    def _flatten_dict(
        self,
        data: dict[object, object],
        result: dict[str, str],
        file_path: Path,
        prefix: str = "",
    ) -> None:
        """
        Flatten a nested localization dictionary.

        Parameters
        ----------
        data:
            Source dictionary.

        result:
            Destination dictionary.

        file_path:
            Source JSON path.

        prefix:
            Current key prefix.

        Raises
        ------
        InvalidLocalizationFileError
            If the JSON structure is invalid.
        """

        for key, value in data.items():
            if not isinstance(key, str):
                raise InvalidLocalizationFileError(f"All keys must be strings: {file_path}")

            full_key = f"{prefix}.{key}" if prefix else key

            if isinstance(value, str):
                result[full_key] = value

            elif isinstance(value, dict):
                self._flatten_dict(
                    data=value,
                    result=result,
                    file_path=file_path,
                    prefix=full_key,
                )

            else:
                raise InvalidLocalizationFileError(
                    "Localization values must be either strings " f"or nested objects: {file_path}"
                )
