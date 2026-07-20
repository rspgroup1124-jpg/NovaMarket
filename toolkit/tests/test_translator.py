"""Tests for the translation service."""

from __future__ import annotations

import pytest

from novamarket_toolkit.i18n import TranslationService


def test_locale_property_returns_locale() -> None:
    """Locale property should return the selected locale."""

    translator = TranslationService("en")

    assert translator.locale == "en"


def test_text_returns_translation() -> None:
    """Text should return a localized string."""

    translator = TranslationService("en")

    assert translator.text("artifacts.user_story") == "User Story"
    assert translator.text("fields.feature") == "Feature"


def test_term_returns_glossary_term() -> None:
    """Term should return a glossary value."""

    translator = TranslationService("en")

    assert translator.term("api") == "API"
    assert translator.term("sql") == "SQL"


def test_format_returns_formatted_string() -> None:
    """Format should substitute placeholders."""

    translator = TranslationService("en")

    translator._translations["messages.greeting"] = "Hello, {name}!"

    assert (
        translator.format(
            "messages.greeting",
            name="NovaMarket",
        )
        == "Hello, NovaMarket!"
    )


def test_text_raises_key_error_for_unknown_key() -> None:
    """Unknown translation key should raise KeyError."""

    translator = TranslationService("en")

    with pytest.raises(KeyError):
        translator.text("unknown.key")


def test_term_raises_key_error_for_unknown_key() -> None:
    """Unknown glossary key should raise KeyError."""

    translator = TranslationService("en")

    with pytest.raises(KeyError):
        translator.term("unknown.term")
