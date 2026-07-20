"""Tests for the localization loader."""

from __future__ import annotations

import pytest

from novamarket_toolkit.i18n.exceptions import (
    GlossaryNotFoundError,
    InvalidLocalizationFileError,
    LocaleNotFoundError,
)
from novamarket_toolkit.i18n.loader import LocalizationLoader


def test_load_locale_returns_dictionary() -> None:
    """Locale loader should return a flattened dictionary."""

    loader = LocalizationLoader()

    translations = loader.load_locale("en")

    assert isinstance(translations, dict)
    assert translations["artifacts.user_story"] == "User Story"
    assert translations["fields.feature"] == "Feature"


def test_load_terms_returns_dictionary() -> None:
    """Glossary loader should return a dictionary."""

    loader = LocalizationLoader()

    terms = loader.load_terms()

    assert isinstance(terms, dict)
    assert terms["api"] == "API"
    assert terms["sql"] == "SQL"


def test_load_missing_locale_raises_exception() -> None:
    """Loading a missing locale should raise LocaleNotFoundError."""

    loader = LocalizationLoader()

    with pytest.raises(LocaleNotFoundError):
        loader.load_locale("does_not_exist")


def test_missing_glossary_raises_exception(tmp_path) -> None:
    """Missing glossary file should raise GlossaryNotFoundError."""

    loader = LocalizationLoader()

    original = loader._glossary_dir

    glossary_dir = tmp_path / "glossary"
    glossary_dir.mkdir()

    loader._glossary_dir = glossary_dir

    try:
        with pytest.raises(GlossaryNotFoundError):
            loader.load_terms()
    finally:
        loader._glossary_dir = original


def test_invalid_json_raises_exception(tmp_path) -> None:
    """Invalid JSON should raise InvalidLocalizationFileError."""

    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("not json", encoding="utf-8")

    loader = LocalizationLoader()

    with pytest.raises(InvalidLocalizationFileError):
        loader._read_json(invalid_file)
