from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from user_data import inst_username, inst_password
import time


useragent = UserAgent()
options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={useragent.opera}")
# disable wwebdriver mode
options.set_preference("dom.webdriver.enabled", False)
options.add_argument("--headless")
# options.headless = True
s=Service('geckodriver.exe')
#s=Service('e:/python/geckodriver/geckodriver.exe')



driver = webdriver.Firefox(service=s, options=options)


#driver = webdriver.Chrome(service=s, options=options)
url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'


try:
    driver.get(url=url)
    time.sleep(5)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

