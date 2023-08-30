# Scrapy Parser Python Enhancement Proposals (PEP)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://scrapy.org/)
[![XPath](https://img.shields.io/badge/-XPath-464646?style=flat&logo=XPath&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=flat&logo=CSS&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?style=flat&logo=Pytest&logoColor=ffffff&color=043A6B)](https://www.python.org/)

________
# Парсинг документов PEP

![alt text](https://pictures.s3.yandex.net/resources/sprint2_picture1_1672399951.png)

Асинхронный парсер документов PEP на базе фреймворка Scrapy, собирающий данные о
PEP с сайта `https://www.python.org/`.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет
два файла в формате `.csv` в папке `results/...`.

* В первый файл сохраняет список всех PEP: номер, название и статус.
  Во второй файл подсчитывает общее количество каждого статуса и сумму всех
  статусов.
  В последней строке файла в колонке «Статус» общее количество всех документов.
* Метод паука parse() собирает ссылки на документы PEP.
  Метод parse_pep() парсит страницы с документами и формирует Items.
  При парсинге применены CSS- и XPath-селекторы.
  Для создания Items описан класс PepParseItem.
* Файлы со списком PEP именованы по маске pep_ДатаВремя.csv.
  Файлы со сводкой по статусам именованы по маске status_summary_ДатаВремя.csv.

## Технологии проекта

* Python — высокоуровневый язык программирования.
* Scrapy — популярный фреймворк для парсинга веб сайтов. Особенности:
    * Многопоточность
    * Веб-краулер для перехода от ссылки к ссылке
    * Извлечение данных
    * Проверка данных
    * Сохранение в другой формат/базу данных
* XPath — язык запросов к элементам XML-документа. 
* CSS - Cascading Style Sheets, каскадные таблицы стилей.
* Pytest — среда тестирования, основанная на Python. 

## Инструкция по развёртыванию проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:SemenovY/scrapy_parser_pep
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

## Запуск парсера

```
scrapy crawl pep
```

### Зависимости:

* Python 3.9
* Scrapy

_____________
***Над проектом работал:***
* Семёнов Юрий | GitHub: [SemenovY](https://github.com/SemenovY)| Python developer.

### *Free Software, Not for commercial use!*
### =^..^=______/
