from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
#from user_data import inst_username, inst_password
import pickle
import requests
from bs4 import BeautifulSoup as BS
import time

useragent = UserAgent()
options = webdriver.FirefoxOptions()
#options.add_argument(f"user-agent={useragent.opera}")

s=Service('geckodriver.exe')

driver = webdriver.Firefox(service=s, options=options)
url = 'https://www.kufar.by/l/velosipedy'


try:
    driver.get(url=url)
    time.sleep(5)
    pickle.dump(driver.get_cookies(), open(f"kufar_cookies", "wb"))
    for cookie in pickle.load(open(f"kufar_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()