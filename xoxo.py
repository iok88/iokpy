import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    # r = requests.get("https://stopgame.ru/review/new/izumitelno/p1")
    r = requests.get("https://mysku.club/index/page" + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select("#content > .topic")

    if(len(items)):
        for el in items:
            title = el.select('.topic-title > a')
            print(title[0].text)
        page += 1
        print('page page  ' + str(page))
    else:
        break


    # for el in html.select(".items > .article-summary"):
    #    title = el.select('.caption > a')
    #    print( title[0].text)
