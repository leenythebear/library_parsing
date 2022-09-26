import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from pathvalidate import sanitize_filename
from parse_book_page import get_book_title_author


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(url, filename, folder='books/'):
    response = requests.get(url)
    response.raise_for_status()
    check_for_redirect(response)

    correct_filename = f'{sanitize_filename(filename)}.txt'
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, correct_filename)
    with open(file_path, 'wt', encoding='utf-8') as file:
        file.write(response.text.replace('\xa0', ''))


if __name__ == "__main__":
    # load_dotenv()
    # url = os.getenv('URL')
    url = 'https://tululu.org/b32168/'

    # response = download_txt(url, book_id)
    os.makedirs('books/', exist_ok=True)
    try:
        response = requests.get(url)
        check_for_redirect(response)
        soup = BeautifulSoup(response.text, 'lxml')
        filename = get_book_title_author(soup)
        download_txt(url, filename)

    except requests.HTTPError:
        print("Запрашиваемвя книга не найдена")


