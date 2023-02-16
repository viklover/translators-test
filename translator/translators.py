
import translators as ts
import translators.server as tss

from .base import Translator
from .decorators import with_timer

class Translators(Translator):

    def __init__(self) -> None:
        super().__init__("Translators")

        self.current_api = 'google'

    def get_name(self):
        return f"{self.current_api.title()} translator"

    def set_api(self, api):
        self.current_api = api
        return self

    @with_timer
    def translate(self, text, source='zh', dest='en'):
        return eval(f'tss.{self.current_api}(text, from_language=source, to_language=dest)')
