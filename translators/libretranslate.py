
import libretranslatepy

from .decorators import with_timer
from .translator import Translator

class LibreTranslate(Translator):

    def __init__(self) -> None:
        super().__init__('Libre Translator')

        self.translator = libretranslatepy.LibreTranslateAPI('http://localhost:5000')

    @with_timer
    def translate(self, text, source='zh', dest='en'):
        return self.translator.translate(text, source=source, target=dest)
