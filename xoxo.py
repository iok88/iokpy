import requests
from bs4 import BeautifulSoup as BS

#r = requests.get("https://stopgame.ru/review/new/izumitelno/p1")
r = requests.get("https://mysku.club/")
html = BS(r.content, 'html.parser')

#for el in html.select(".items > .article-summary"):
#    title = el.select('.caption > a')
#    print( title[0].text)

for el in html.select("#content > .topic"):
    title = el.select('.topic-title > a')
    print( title[0].text)