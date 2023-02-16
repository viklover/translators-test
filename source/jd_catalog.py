
from .base import Source

import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from argparse import ArgumentParser, _SubParsersAction

class JdCatalog(Source):

    def __init__(self) -> None:
        super().__init__('JdCatalog')

        self.agent = UserAgent()

        self.page = 1
        self.items = 30

    def setup_parser(self, subparsers: _SubParsersAction, func):

        parser: ArgumentParser = subparsers.add_parser('catalog', help='using the chinese online shop as a source of sentences')
        parser.add_argument('-p', type=int, default=1, help='catalog page')
        parser.add_argument('-i', type=int, default=30, help='max items')
        parser.set_defaults(func=lambda args: func('catalog', args))

        return super().setup_parser(parser)

    def set_args(self, args):
        self.page = args.p
        self.items = args.i

    def get(self):
        response = self.request(f'https://list.jd.com/list.html?cat=1315%2C1343%2C9719&page={self.page}&s=57&click=0')

        soup = BeautifulSoup(response.text, features="html.parser")
        items = soup.find(class_='gl-warp').findAll(class_='gl-i-wrap')

        return [item.find(class_="p-name").find('em').text for item in items[:self.items]]

    def request(self, url):
        headers = {'User-Agent': self.agent.random}
        return requests.get(url, headers=headers)
