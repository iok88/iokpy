from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
import time
import requests
from bs4 import BeautifulSoup as BS


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.opera}")


s=Service('e:/python/chromedriver_win32/chromedriver.exe')
#s=Service('e:/python/geckodriver/geckodriver.exe')

#driver = webdriver.Firefox(service=s)


driver = webdriver.Chrome(service=s, options=options)
#url = 'https://www.kufar.by/l/velosipedy'
#url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
url = 'https://www.instagram.com/'

try:
    driver.get(url=url)
    time.sleep(10)

    email_input = driver.find_element("name",'username')
    email_input.clear()
    email_input.send_keys("iok88")
    time.sleep(10)

    password_input = driver.find_element("name",'password')
    password_input.clear()
    password_input.send_keys("1988Iokkoi")
    time.sleep(10)

    password_input.send_keys(Keys.ENTER)
    # login_button = driver.find_element().click()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

