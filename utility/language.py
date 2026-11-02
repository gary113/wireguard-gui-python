"""
Interface language support.

The language can be changed at runtime from the main window and the choice
is stored with QSettings, so it is restored the next time wgp starts.

Adding a new language only requires:

1. Adding its code and native name to SUPPORTED_LANGUAGES below.
2. Dropping the matching .qm files in the translations directory, for
   instance wgp_<code>.qm (application strings) and qt_<code>.qm,
   qtbase_<code>.qm (strings of the standard Qt widgets).
"""

from PyQt6.QtCore import QLocale, QSettings, QTranslator

from utility.functions import PROJECT_DIRECTORY

TRANSLATIONS_DIRECTORY = PROJECT_DIRECTORY / "translations"

# Language code shown in the language menu -> name displayed to the user.
# The names are written in their own language on purpose.
SUPPORTED_LANGUAGES = {
    "en": "English",
    "zh_CN": "中文",
}

# Pseudo language meaning "use the language of the system".
SYSTEM_LANGUAGE = "system"

# Language used when the system language is not supported.
DEFAULT_LANGUAGE = "en"

_SETTINGS_ORGANIZATION = "wireguard-gui-python"
_SETTINGS_APPLICATION = "wgp"
_SETTINGS_LANGUAGE_KEY = "interface/language"

_installed_translators = []


def language_choices():
    """Languages of the language menu, as (code, display name) pairs.

    The first entry is the SYSTEM_LANGUAGE pseudo language, whose display
    name is None: the view is in charge of showing a localized label.
    """
    return [(SYSTEM_LANGUAGE, None)] + list(SUPPORTED_LANGUAGES.items())


def detect_system_language() -> str:
    """Resolve the system locale to a supported language code."""
    locale = QLocale.system().name()  # e.g. "zh_CN", "en_US", "C"

    if locale in SUPPORTED_LANGUAGES:
        return locale

    language = locale.split("_")[0].lower()
    for code in SUPPORTED_LANGUAGES:
        if code.split("_")[0].lower() == language:
            return code

    return DEFAULT_LANGUAGE


def resolve_language(language: str) -> str:
    """Turn a stored preference into a supported language code."""
    if language in SUPPORTED_LANGUAGES:
        return language
    if language == SYSTEM_LANGUAGE:
        return detect_system_language()
    return DEFAULT_LANGUAGE


def get_saved_language() -> str:
    """Return the language preference stored by the user."""
    value = _settings().value(_SETTINGS_LANGUAGE_KEY, SYSTEM_LANGUAGE)

    if value == SYSTEM_LANGUAGE:
        return SYSTEM_LANGUAGE
    if isinstance(value, str) and value in SUPPORTED_LANGUAGES:
        return value

    return SYSTEM_LANGUAGE


def save_language(language: str) -> None:
    """Store the language preference chosen by the user."""
    _settings().setValue(_SETTINGS_LANGUAGE_KEY, language)


def install_language(app, language: str) -> str:
    """Install the translations of a language on a QApplication.

    Translators installed by a previous call are removed first, so this
    function is used both at startup and when the user switches language
    at runtime. It returns the language code that was actually installed.
    """
    global _installed_translators

    language = resolve_language(language)

    for translator in _installed_translators:
        app.removeTranslator(translator)
    _installed_translators = []

    for translation_file in sorted(TRANSLATIONS_DIRECTORY.glob(f"*_{language}.qm")):
        translator = QTranslator(app)

        if translator.load(str(translation_file)):
            app.installTranslator(translator)
            _installed_translators.append(translator)

    return language


def _settings() -> QSettings:
    return QSettings(
        QSettings.Format.IniFormat,
        QSettings.Scope.UserScope,
        _SETTINGS_ORGANIZATION,
        _SETTINGS_APPLICATION,
    )
