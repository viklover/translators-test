
from .googletrans import GoogleTranslator
from .yandex import YandexTranslator
from .translators import Translators

yandexTranslator = YandexTranslator()
googleTranslator = GoogleTranslator()
translators = Translators()

def get_by_api(api_name):
    
    match api_name:
        case 'google':
            return googleTranslator
        case 'yandex':
            return yandexTranslator
        case _:
            return translators.set_api(api_name)
