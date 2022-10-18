from urllib.parse import urlsplit

import requests
import os
from pathvalidate import sanitize_filename
from redirect import check_for_redirect


def download_txt(book_url, filename, folder="books/"):
    book_id = urlsplit(book_url).path.strip("/").lstrip('b')
    url = "https://tululu.org/txt.php"
    params = {"id": book_id}
    response = requests.get(url, params=params)
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
