from urllib.parse import urlsplit

import requests
from bs4 import BeautifulSoup
import os
from pathvalidate import sanitize_filename
from parse_book_page import get_book_title_author, get_book_image_url, get_book_comments, get_book_genre


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(book_id, filename, folder='books/'):
    url = 'https://tululu.org/txt.php'
    params = {'id': book_id}
    response = requests.get(url, params)
    response.raise_for_status()
    check_for_redirect(response)

    correct_filename = f'{sanitize_filename(filename)}.txt'
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, correct_filename)
    with open(file_path, 'wt', encoding='utf-8') as file:
        file.write(response.text.replace('\xa0', ''))


def download_image(image_url, folder='images/'):
    filename = urlsplit(image_url).path.split('/')[-1]
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    response = requests.get(image_url)
    response.raise_for_status()
    with open(file_path, 'wb', ) as file:
        file.write(response.content)


if __name__ == "__main__":
    for id_book in range(1, 11):

        url = f'https://tululu.org/b{id_book}/'
        try:
            response = requests.get(url)
            check_for_redirect(response)
            soup = BeautifulSoup(response.text, 'lxml')
            filename = get_book_title_author(soup)
            download_txt(id_book, filename)
            image_url = get_book_image_url(soup)
            download_image(image_url)
            print(get_book_comments(soup))
            print(get_book_genre(soup))
        except requests.HTTPError:
            print("Запрашиваемая книга не найдена")


