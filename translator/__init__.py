
from .googletrans import GoogleTranslator
from .libretranslate import LibreTranslate
from .translators import Translators

variants = [
    GoogleTranslator(),
    # LibreTranslate(),
    Translators()
]
