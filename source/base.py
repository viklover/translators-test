
from argparse import ArgumentParser

class Source(object):

    def __init__(self, name: str) -> None:
        self.name = name

    def setup_parser(self, parser: ArgumentParser):
        
        parser.add_argument(
            '-api', nargs='+', help='services to be used for translation', choices=TRANSLATORS_CHOICE, default=DEFAULT_TRANSLATORS_CHOICE)
        
        parser.add_argument(
            '-target', nargs='+', help='languages target', choices=TARGET_LANG_CHOICE, default=DEFAULT_TARGET_LANG_CHOICE)

    def get(self):
        pass


TRANSLATORS_CHOICE = [
    'google', 'yandex', 'alibaba', 'argos', 'bing', 'caiyun', 
    'deepl', 'iciba', 'iflytek', 'itranslate', 'lingvanex', 'niutrans', 
    'mglip', 'papago', 'reverso', 'sogou', 'tencent', 'translateCom', 
    'utibet', 'youdao'
]
DEFAULT_TRANSLATORS_CHOICE = ['google']

TARGET_LANG_CHOICE = ['en', 'ru', 'zh']
DEFAULT_TARGET_LANG_CHOICE = ['en', 'ru']
