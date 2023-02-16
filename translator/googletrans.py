
import googletrans

from .decorators import with_timer
from .base import Translator

class GoogleTranslator(Translator):

    def __init__(self) -> None:
        super().__init__('Google Translator')

        self.translator = googletrans.Translator()

    @with_timer
    def translate(self, text, source='zh-cn', dest='en'):

        if source == 'zh':
            source = 'zh-cn'

        return self.translator.translate(text, src=source, dest=dest).text
