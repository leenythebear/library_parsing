import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError

from main import check_for_redirect, download_txt, download_image
from parse_book_page import parse_book_page


def get_book_url(page):
    url = f'https://tululu.org/l55/{page}'
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    selector = 'table.d_book'
    book_tags = soup.select(selector)
    for book_tag in book_tags:
        book_link = book_tag.select_one('a')['href']
        book_url = urljoin(url, book_link)
        yield book_url


if __name__ == "__main__":
    for page in range(1, 2):
        book_url = get_book_url(page)
        print(book_url)
        for url in book_url:
            try:
                response = requests.get(url)
                check_for_redirect(response)
                response.raise_for_status()

                book = parse_book_page(response)

                book_json = json.dumps(book, ensure_ascii=False)
                with open("books.json", "a") as my_file:
                    my_file.write(book_json)

                print(book["title"])
                print(book["genres"])
                download_txt(url, book["title"])
                image_url = urljoin(url, book["image_url"])
                download_image(image_url)

            except HTTPError:
                print("Запрашиваемая книга не найдена")
                continue

            except ConnectionError:
                print("Что-то не так с интернет-соединением. Следующая попытка соединения через 1 минуту")
                time.sleep(60)
                continue




