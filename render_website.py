from livereload import Server
from more_itertools import chunked

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


def reload():
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    with open("books.json", "r") as library:
        books_json = library.read()
    books = json.loads(books_json)
    chunked_books = list(chunked(books, 2))
    print(chunked_books)
    rendered_page = template.render(chunked_books=chunked_books)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == "__main__":
    reload()
    server = Server()
    server.watch('template.html', reload)
    server.serve(root='.')
