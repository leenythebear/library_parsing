import requests
import os


def download_book(url, book_id):
    params = {'id': book_id}
    response = requests.get(url, params=params, allow_redirects=True)
    response.raise_for_status()
    return response


def save_book(response):
    with open(f'books/{book_id}.txt', 'wt', encoding='utf-8') as file:
        file.write(response.text.replace('\xa0', ''))

# print(response.text)