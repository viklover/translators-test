Translators test
================

Тестирование различных библиотек машинного перевода

* [translators](https://github.com/UlionTse/translators)
* [py-googletrans](https://github.com/ssut/py-googletrans)
* [yandexfreetranslate](https://github.com/alekssamos/yandexfreetranslate.git)


Установка зависимостей
-----------------------
* Python 3.10+

```bash
pip install -r requirements.txt
```

Использование
---------------------
Посмотреть все команды и аргументы к ним: 

```bash
python main.py -h
```
Перевод введённого предложения
```bash
> python main.py translate "你好世界" -api google yandex -target en ru

Sentence: 你好世界
--------------------
  Google Translator
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
  EN - 0.22s:
  Hello World

  RU - 0.22s:
  Привет, мир

--------------------
  Yandex Translator
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
  EN - 0.27s:
  Hello world

  RU - 0.18s:
  Привет, мир
```

Перевод названия товара из [китайского онлайн-магазина](
https://list.jd.com/):
```bash
> python main.py catalog -p 18 -i 1 -api google -target ru

Sentence: 歌珀莱（GEPORAIS）品牌女装高端提花连衣裙女春季2023年新款收腰气质设计感中长裙子 粉色 M 预售15天
--------------------
  Google Translator
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
  RU - 0.44s:
  Бренд GEPORAIS, женское жаккардовое платье высокого класса, женская весна 2023, новый дизайн, юбка средней длины с талией и темпераментом, розовый M, предпродажа в течение 15 дней.
```