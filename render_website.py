import os

from livereload import Server
from more_itertools import chunked

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

BOOKS_PER_PAGE = 10
NUMBER_OF_COLUMNS = 2


def reload():
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    with open("books.json", "r") as books_json:
        books = json.load(books_json)

    folder_path = 'pages/'
    os.makedirs(folder_path, exist_ok=True)

    books_for_page = list(chunked(books, BOOKS_PER_PAGE))
    page_count = len(books_for_page)

    for page_number, separate_books in enumerate(books_for_page, 1):
        chunked_books = list(chunked(separate_books, NUMBER_OF_COLUMNS))
        page_name = f'index{page_number}.html'
        page_path = os.path.join(folder_path, page_name)

        rendered_page = template.render(chunked_books=chunked_books, page_count=page_count, page_number=page_number)

        with open(page_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "__main__":
    reload()
    server = Server()
    server.watch('template.html', reload)
    server.serve(root='.')
