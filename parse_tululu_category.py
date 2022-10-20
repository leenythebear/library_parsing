import argparse
import json
import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError

from downloads import download_txt, download_image, save_json
from redirect import check_for_redirect
from parse_book_page import parse_book_page


def get_book_url(page):
    url = f'https://tululu.org/l55/{page}'
    response = requests.get(url)
    check_for_redirect(response)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    selector = 'table.d_book'
    book_tags = soup.select(selector)
    for book_tag in book_tags:
        book_link = book_tag.select_one('a')['href']
        book_url = urljoin(url, book_link)
        yield book_url


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Парсер книг с сайта tululu.org"
    )
    parser.add_argument(
        "-s",
        "--start_page",
        help="Начальная страница для парсинга, по умолчанию - 1",
        default=1,
        type=int,
    )
    parser.add_argument(
        "-e",
        "--end_page",
        help="Конечная страница для парсинга, по умолчанию - 700",
        default=700,
        type=int,
    )
    parser.add_argument(
        "-d",
        "--dest_folder",
        help="Путь к каталогу с результатами парсинга: картинкам, книгам, JSON",
        default="",
    )
    parser.add_argument(
        "-i",
        "--skip_images",
        help="Не скачивать картинки",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-t",
        "--skip_txt",
        help="Не скачивать книги",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-j",
        "--json_path",
        help="Указать свой путь к файлу json с результатами парсинга",
        default='',

    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()

    books = []
    for page in range(args.start_page, args.end_page):
        book_url = get_book_url(page)

        for url in book_url:
            try:
                response = requests.get(url)
                check_for_redirect(response)
                response.raise_for_status()

                book = parse_book_page(response)
                books.append(book)

                if not args.skip_txt:
                    download_txt(url, book["title"], dest_folder=args.dest_folder)
                if not args.skip_images:
                    image_url = urljoin(url, book["image_url"])
                    download_image(image_url, dest_folder=args.dest_folder)

            except HTTPError:
                print("Запрашиваемая книга не найдена")
                continue

            except ConnectionError:
                print(
                    "Что-то не так с интернет-соединением. Следующая попытка соединения через 1 минуту")
                time.sleep(60)
                continue

    save_json(books, args.dest_folder, args.json_path)



