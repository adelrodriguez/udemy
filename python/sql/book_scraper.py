import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for book in soup.find_all('article'):
        title = get_title(book)
        price = get_price(book)
        rating = get_rating(book)

        books.append((title, price, rating))

    return books

def get_title(book):
    return book.select('h3 > a')[0]['title']

def get_price(book):
    price = book.select('.price_color')[0].text

    return float(price.replace('Â£', ''))

def get_rating(book):
    rating_dict = { 'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5 }
    star_rating = book.select('.star-rating')[0].get_attribute_list('class')[1]

    return rating_dict[star_rating]

def save_books(data):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE books (
            title TEXT,
            price REAL,
            rating INTEGER
        )
    ''')

    query = 'INSERT INTO books VALUES (?, ?, ?)'

    cursor.executemany(query, data)
    connection.commit()
    cursor.close()

    pass


books = scrape_books('http://books.toscrape.com/catalogue/category/books/history_32/index.html?')

save_books(books)