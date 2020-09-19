import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

count = 1

with open('blog_data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'url', 'date'])

while True:
    response = requests.get(f'https://www.rithmschool.com/blog?page={count}', )

    if response.status_code == 200:
        print(f'Scraping page {count}')
        count +=1
    else:
        print(f'Got status code {response.status_code}')
        break

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.select('article')

    with open('blog_data.csv', 'a') as csv_file:
        csv_writer = writer(csv_file)

        for article in articles:
            a_tag = article.find('a')

            title = a_tag.get_text()
            url = a_tag['href']
            date = article.find('time')['datetime']
            csv_writer.writerow([title, url, date])
    
    sleep(1)