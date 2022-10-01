import argparse
from urllib.parse import urlsplit

import requests
import os
from pathvalidate import sanitize_filename
from parse_book_page import parse_book_page


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(book_id, filename, folder="books/"):
    url = "https://tululu.org/txt.php"
    params = {"id": book_id}
    response = requests.get(url, params)
    response.raise_for_status()
    check_for_redirect(response)

    correct_filename = f"{sanitize_filename(filename)}.txt"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, correct_filename)
    with open(file_path, "wt", encoding="utf-8") as file:
        file.write(response.text.replace("\xa0", ""))


def download_image(image_url, folder="images/"):
    filename = urlsplit(image_url).path.split("/")[-1]
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    response = requests.get(image_url)
    response.raise_for_status()
    with open(
        file_path,
        "wb",
    ) as file:
        file.write(response.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Парсер книг с сайта tululu.org')
    parser.add_argument(
        "-s",
        "--start_id",
        help="Начальный id книги для парсинга",
        default=1,
        type=int,
    )
    parser.add_argument(
        "-e",
        "--end_id",
        help="Конечный id книги для парсинга",
        default=11,
        type=int,
    )
    args = parser.parse_args()
    start_id = args.start_id
    end_id = args.end_id
    for id_book in range(start_id, end_id):

        url = f"https://tululu.org/b{id_book}/"
        try:
            response = requests.get(url)
            check_for_redirect(response)
            response.raise_for_status()
            book = parse_book_page(response)
            print(book["title"])
            print(book["genres"])
            download_txt(id_book, book["title"])
            download_image(book["image_url"])

        except requests.HTTPError:
            print("Запрашиваемая книга не найдена")
