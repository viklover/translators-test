
from yandexfreetranslate import YandexFreeTranslate

from .decorators import with_timer
from .base import Translator

class YandexTranslator(Translator):

    def __init__(self) -> None:
        super().__init__('Yandex Translator')

        self.translator = YandexFreeTranslate()

    @with_timer
    def translate(self, text, source='zh', dest='en'):
        return self.translator.translate(source, dest, text)
