from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
import requests
from bs4 import BeautifulSoup as BS

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"--proxy-server=45.152.188.246:3128")

s=Service('e:/python/chromedriver_win32/chromedriver.exe')
#s=Service('e:/python/geckodriver/geckodriver.exe')

#driver = webdriver.Firefox(service=s)


driver = webdriver.Chrome(service=s, options=options)
#url = 'https://www.kufar.by/l/velosipedy'
#url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
url = 'https://www.2ip.ru'

try:
    driver.get(url=url)
    #driver.get_cookie()

    timer.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

