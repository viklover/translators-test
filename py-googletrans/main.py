import sys
import time
import requests
import googletrans

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

agent = UserAgent()
translator = googletrans.Translator()

def request(url):
    
    headers = {
        'User-Agent': agent.random
    }
    
    return requests.get(url, headers=headers)

def translate(text, dest='en'):
    
    start = time.time()

    translation = translator.translate(text, dest=dest).text

    end = time.time()

    return translation, end - start

def main(args):

    page = args[1] if len(args) > 1 else 1

    response = request(f'https://list.jd.com/list.html?cat=1315%2C1343%2C9719&page={page}&s=57&click=0')

    if not response:
        raise RuntimeError('Response failed')

    soup = BeautifulSoup(response.text, features="html.parser")
    items = soup.find(class_='gl-warp').findAll(class_='gl-i-wrap')

    print('Producs: \n')

    for item in items:
        
        name = item.find(class_="p-name").find('em').text

        print(f' - Name:\n {name}\n')

        name_en, seconds = translate(name)
        print(f' - EN ({round(seconds, 3)}):\n {name_en}\n')

        name_ru, seconds = translate(name, dest='ru')
        print(f' - RU ({round(seconds, 3)}):\n {name_ru}')

        print('-'*20)


if __name__ == "__main__":
    main(sys.argv)