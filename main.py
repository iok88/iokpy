# This is a sample Python script.
import requests
from bs4 import BeautifulSoup

URL = 'https://mysku.club/'
HEADERS ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44', 'accept':'*/*'}


def get_html(url, params=None):
    r = requests.get(url,headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='topic')
    topic=[]
    for item in items:
        price= item.find('li', class_='price')
        if price:
            price=item.find('li', class_='price').get_text()
        else:
            price = 'NO PRICE'
        topic.append({
            'title': item.find('div', class_='topic-title').get_text(strip=True),
            'link': item.find('a', class_='').get('href'),
            'price': price,
            #'shop' : item.find('a', class_='list-item-link').get_text(),
        })
        print(topic)


def parse():
    html = get_html(URL)
    if html.status_code ==200:
        get_content(html.text)

    else:
        print('Error')
parse()
