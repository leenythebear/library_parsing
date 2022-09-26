from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_book_title_author(soup):
    title_and_author = soup.find('title').text.split(', ')[0]
    book_name = title_and_author.split('-')[0].strip()
    return book_name


def get_book_image_url(soup):
    url = soup.find('div', class_='bookimage').find('img')['src']
    common_url = 'https://tululu.org/'
    image_url = urljoin(common_url, url)
    return image_url


def get_book_comments(soup):
    comments_tags = soup.find_all('div', class_='texts')
    comments = []
    for comment in comments_tags:
        comments.append(comment.find('span').text)
    return comments


