from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_book():
    url = 'https://tululu.org/l55/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    book_link = soup.find('table', class_='d_book').find('a')['href']
    book_url = urljoin(url, book_link)
    print(book_url)


if __name__ == "__main__":
    get_book()
