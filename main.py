import requests
from dotenv import load_dotenv
import os


def download_book(url, book_id):
    params = {'id': book_id}
    response = requests.get(url, params=params, allow_redirects=True)
    response.raise_for_status()
    return response


def save_book(response):
    with open(f'books/{book_id}.txt', 'wt', encoding='utf-8') as file:
        file.write(response.text.replace('\xa0', ''))


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv('URL')
    for book_id in range(1, 11):
        response = download_book(url, book_id)
        os.makedirs('books/', exist_ok=True)
        try:
            check_for_redirect(response)
            save_book(response)
        except requests.HTTPError:
            print("Запрашиваемвя книга не найдена")


