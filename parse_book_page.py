from urllib.parse import urljoin

from bs4 import BeautifulSoup


def get_book_title_author(soup):
    title_and_author = soup.find("table", class_="tabs").find("h1").text
    title, author = title_and_author.split("::")
    return title.strip(), author.strip()


def get_book_image_url(soup):
    url = soup.find("div", class_="bookimage").find("img")["src"]
    common_url = "https://tululu.org/"
    image_url = urljoin(common_url, url)
    return image_url


def get_book_comments(soup):
    comments_tags = soup.find_all("div", class_="texts")
    comments = []
    for comment in comments_tags:
        comments.append(comment.find("span").text)
    return comments


def get_book_genre(soup):
    genre_tags = soup.find("span", class_="d_book").find_all("a")
    genres = []
    for genre in genre_tags:
        genres.append(genre.text)
    return genres


def parse_book_page(response, book_id):
    soup = BeautifulSoup(response.text, "lxml")
    title, author = get_book_title_author(soup)
    image_url = get_book_image_url(soup)
    genres = get_book_genre(soup)
    comments = get_book_comments(soup)
    book = {
        "title": title,
        "author": author,
        "image_url": image_url,
        "genres": genres,
        "comments": comments,
    }
    return book
