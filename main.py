import requests
import os


def download_book():
    for book_id in range(0, 9):
        url = f'https://tululu.org/txt.php?id={book_id}'
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs('books', exist_ok=True)
        with open(f'books/{book_id}.txt', 'wt', encoding='utf-8') as file:
            file.write(response.text.replace('\xa0', ''))

# print(response.text)