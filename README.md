# Парсер книг с сайта [tululu.org](https://tululu.org/) и оффлайн-библиотека на основе полученных данных парсинга

Скрипт предназначается для скачивания книг и информации о них с сайта [tululu.org](https://tululu.org/).

### Как установить

1. Скачайте код
2. Для работы скрипта нужен Python версии не ниже 3.7
3. Установите зависимости, указанные в файле requirements.txt командой:

   ```pip install -r requirements.txt```

### Как запустить парсинг

1. При запуске скрипта командой ```python3 parse_tululu_category.py``` по умолчанию будут скачаны книги с 1 gо 699 страницу включительно.

2. При запуске скрипта с помощью аргументов можно указать:

___

- С какой страницы будет начинаться скачивание и на какой заканчиваться, например:

  ```python3 parse_tululu_category.py -s 13 -e 17```

   или 

   ```python3 parse_tululu_category.py --start_page 13 --end_page 17```

   где:
   * 13 - страница, с которой начнется скачивание,
   * 17 - страница, до которой скачаются книги (не включая 17-ую)

___

- Путь к каталогу с результатами парсинга: картинкам, книгам, JSON, например:

  ```python3 parse_tululu_category.py -d destination_folder```

  или

  ```python3 parse_tululu_category.py --dest_folder destination_folder```

  где:
  * destination_folder - папка для сохранения файлов (необязательный аргумент)

___

- Не скачивать картинки (по умолчанию, при не указанном аргументе картинки скачиваются):

  ```python3 parse_tululu_category.py -i```

  или

  ```python3 parse_tululu_category.py --skip_images```

___

- Не скачивать книги (по умолчанию, при не указанном аргументе книги скачиваются):

  ```python3 parse_tululu_category -t```

  или

  ```python3 parse_tululu_category.py --skip_txt```

___

- Указать свой путь к файлу json с результатами парсинга:

  ```python3 parse_tululu_category.py -j```

  или

  ```python3 parse_tululu_category.py --json_path path```

  где:
  * path - путь к файлу json c результатами парсинга (необязательный аргумент)

___

### Как запустить оффлайн-библиотеку:

```python3 render_website.py```
* С помощью этого скрипта рендерятся страницы офлайн-библиотеки, просмотр возможен по адресу:
[http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html)
или на [GitHub Pages](https://pages.github.com/)

___

### Доступна уже опубликованная оффлайн-библиотека:
[Оффлайн-библиотека](https://leenythebear.github.io/library_parsing/pages/index1.html)


___

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).