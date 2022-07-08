from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
import requests
from bs4 import BeautifulSoup as BS

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.opera}")
s=Service('e:/python/chromedriver_win32/chromedriver.exe')
#s=Service('e:/python/geckodriver/geckodriver.exe')
driver = webdriver.Chrome(service=s, options=options)
#driver = webdriver.Firefox(service=s)



# url = 'https://www.kufar.by/l/velosipedy'
url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'

try:
    driver.get(url=url)
    timer.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

