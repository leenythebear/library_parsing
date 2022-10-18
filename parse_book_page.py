from bs4 import BeautifulSoup


def get_book_title_author(soup):
    title_and_author = soup.select_one('h1')
    title, author = title_and_author.text.split("::")
    return title.strip(), author.strip()


def get_book_comments(soup):
    comments_tags = soup.find_all("div", class_="texts")
    comments = [comment.find("span").text for comment in comments_tags]
    return comments


def get_book_genres(soup):
    genre_tags = soup.select_one('span.d_book').select('a')
    genres = [genre.text for genre in genre_tags]
    return genres


def parse_book_page(response):
    soup = BeautifulSoup(response.text, "lxml")
    title, author = get_book_title_author(soup)
    image_url = soup.select_one('.bookimage img')['src']
    genres = get_book_genres(soup)
    comments = get_book_comments(soup)
    book = {
        "title": title,
        "author": author,
        "image_url": image_url,
        "genres": genres,
        "comments": comments,
    }
    return book
