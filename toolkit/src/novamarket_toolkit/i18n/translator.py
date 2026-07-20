"""Translation service for NovaMarket Toolkit."""

from __future__ import annotations

from novamarket_toolkit.i18n.loader import LocalizationLoader


class TranslationService:
    """Provide localized text and technical terms."""

    def __init__(self, locale: str) -> None:
        """
        Initialize the translation service.

        Parameters
        ----------
        locale:
            Locale code (for example: "en", "ru", "uk").
        """

        self._loader = LocalizationLoader()
        self._locale_name = locale

        self._translations: dict[str, str] = self._loader.load_locale(locale)
        self._terms: dict[str, str] = self._loader.load_terms()

    @property
    def locale(self) -> str:
        """
        Return the current locale.

        Returns
        -------
        str
            Locale code.
        """

        return self._locale_name

    def text(self, key: str) -> str:
        """
        Return localized text.

        Parameters
        ----------
        key:
            Translation key.

        Returns
        -------
        str
            Localized text.

        Raises
        ------
        KeyError
            If the translation key does not exist.
        """

        return self._translations[key]

    def term(self, key: str) -> str:
        """
        Return a technical term.

        Parameters
        ----------
        key:
            Technical glossary key.

        Returns
        -------
        str
            Localized technical term.

        Raises
        ------
        KeyError
            If the glossary key does not exist.
        """

        return self._terms[key]

    def format(self, key: str, **kwargs: str) -> str:
        """
        Return formatted localized text.

        Parameters
        ----------
        key:
            Translation key.

        **kwargs:
            Values for string formatting.

        Returns
        -------
        str
            Formatted localized text.
        """

        return self.text(key).format(**kwargs)
