from urllib.parse import urlsplit

import requests
import os
from pathvalidate import sanitize_filename
from redirect import check_for_redirect


def download_txt(book_url, filename, dest_folder, folder="books/"):
    book_id = urlsplit(book_url).path.strip("/").lstrip('b')
    url = "https://tululu.org/txt.php"
    params = {"id": book_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    check_for_redirect(response)

    correct_filename = f"{sanitize_filename(filename)}.txt"
    txt_path = os.path.join(dest_folder, folder)
    os.makedirs(txt_path, exist_ok=True)
    file_path = os.path.join(txt_path, correct_filename)
    with open(file_path, "wt", encoding="utf-8") as file:
        file.write(response.text.replace("\xa0", ""))


def download_image(image_url, dest_folder, folder="images/"):
    filename = urlsplit(image_url).path.split("/")[-1]
    image_path = os.path.join(dest_folder, folder)
    os.makedirs(image_path, exist_ok=True)
    file_path = os.path.join(image_path, filename)
    response = requests.get(image_url)
    response.raise_for_status()
    with open(
        file_path,
        "wb",
    ) as file:
        file.write(response.content)
