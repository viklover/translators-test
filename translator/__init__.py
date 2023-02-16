
from .googletrans import GoogleTranslator
from .translators import Translators

googleTranslator = GoogleTranslator()
translators = Translators()

def get_by_api(api_name):
    
    match api_name:
        case 'google':
            return googleTranslator
        case _:
            return translators.set_api(api_name)
