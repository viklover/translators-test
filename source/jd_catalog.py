
from .base import Source

import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class JdCatalog(Source):

    def __init__(self) -> None:
        super().__init__('JdCatalog')

        self.agent = UserAgent()

    def get(self, page=1):
        response = self.request(f'https://list.jd.com/list.html?cat=1315%2C1343%2C9719&page={page}&s=57&click=0')

        soup = BeautifulSoup(response.text, features="html.parser")
        items = soup.find(class_='gl-warp').findAll(class_='gl-i-wrap')

        return [item.find(class_="p-name").find('em').text for item in items]

    def request(self, url):
        headers = {'User-Agent': self.agent.random}
        return requests.get(url, headers=headers)
