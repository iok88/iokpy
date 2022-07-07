# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.kufar.by/l/velosipedy'
HEADERS ={'cookie': '_ym_isad=1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}

FILE='kufar.csv'


def get_html(url, params=None):
    r = requests.get(url,headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='styles_link__KajLs')
    print(pagination)
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1
    #print(pagination)

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
        #print(topic)
    return topic

def save_file(items, path):
    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Заголовой', 'Ссылка', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price']])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        topic = []
        pages_count = get_pages_count(html.text)
        for page in range (1, pages_count+1):
            print (f'Парсинг страницы {page} из {pages_count} ... ')
            html = get_html(URL, params={'page': page})
            #url = URL + 'page' + str(page)
            #print(url)
            #html = get_html(url)

            topic.extend(get_content(html.text))
        #print(topic)
        save_file(topic, FILE)
        print(f'Получено {len(topic)} статей')

    else:
        print('Error')

#parse()

response = requests.get('https://www.kufar.by')
response.cookies
print(response.cookies)
for cookie in response.cookies:
    print('cookie domain = ' + cookie.domain)
    print('cookie name = ' + cookie.name)
    print('cookie value = ' + cookie.value)
