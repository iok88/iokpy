from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from user_data import inst_username, inst_password
import time
import requests
from bs4 import BeautifulSoup as BS
import pickle


useragent = UserAgent()
options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={useragent.opera}")


s=Service('geckodriver.exe')
#s=Service('e:/python/geckodriver/geckodriver.exe')

driver = webdriver.Firefox(service=s, options=options)


#driver = webdriver.Chrome(service=s, options=options)
#url = 'https://www.kufar.by/l/velosipedy'
#url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
url = 'https://www.instagram.com/'

try:
    driver.get(url=url)
    time.sleep(5)

    # email_input = driver.find_element("name",'username')
    # email_input.clear()
    # email_input.send_keys(inst_username)
    # time.sleep(5)
    #
    # password_input = driver.find_element("name",'password')
    # password_input.clear()
    # password_input.send_keys(inst_password)
    # time.sleep(5)
    #
    # password_input.send_keys(Keys.ENTER)
    # # login_button = driver.find_element().click()
    #
    # time.sleep(5)

    # cookies
    # pickle.dump(driver.get_cookies(), open(f"{inst_username}_cookies", "wb"))
    for cookie in pickle.load(open(f"{inst_username}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

