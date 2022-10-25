from livereload import Server


from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


def reload():
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    with open("books.json", "r") as library:
        books_json = library.read()
    books = json.loads(books_json)
    rendered_page = template.render(books=books)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == "__main__":
    reload()
    server = Server()
    server.watch('template.html', reload)
    server.serve(root='.')
