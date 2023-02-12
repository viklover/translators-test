
import translators as ts
import translators.server as tss

from .base import Translator
from .decorators import with_timer

class Translators(Translator):

    def __init__(self) -> None:
        super().__init__("alibaba, yandex")

    def get_name(self):
        return f"Translators: {self.name}"

    @with_timer
    def translate(self, text, source='zh', dest='en'):

        if source == 'zh' and dest == 'en':
            return tss.alibaba(text, from_language=source, to_language=dest)

        elif source == 'en' and dest == 'ru':
            return tss.google(text, from_language=source, to_language=dest)

        return ts.translate_text(text, from_language=source, to_language=dest)
