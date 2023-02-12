Translators test
================

Тестирование различных библиотек машинного перевода

* [py-googletrans](https://github.com/ssut/py-googletrans)
* [libretranslate](https://github.com/LibreTranslate/LibreTranslate)
* [translators](https://github.com/UlionTse/translators)

В качестве данных, берутся товары из каталога [китайского онлайн-магазина](
https://list.jd.com/) в категории женской одежды

Схема перевода
--------------
```
Chinese -> English
Chinese -> Russian
```

Установить зависимости:
-----------------------

```bash
pip install -r requirements.txt
```

Старт Libretranslate сервера:
```bash
./run_libretranslate.sh
```

Использование:
--------------

```bash
python main.py <page>
```

`page` - пагинация в каталоге (если не указывать, по умолчанию будет использоваться первая страница)