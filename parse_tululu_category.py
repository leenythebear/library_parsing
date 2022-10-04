from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_book():
    url = 'https://tululu.org/l55/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    book_tags = soup.find_all('table', class_='d_book')
    for book_tag in book_tags:
        book_link = book_tag.find('a')['href']
        book_url = urljoin(url, book_link)
        print(book_url)


if __name__ == "__main__":
    get_book()
