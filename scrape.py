import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    # url = "https://www.katespade.co.uk/en-gb/wallets/spencer-compact-wallet/PWRU7748.html?dwcolor=001&dwsize=412_U"
    url = "https://www.katespade.co.uk/en-gb/wallets/spencer-zip-around-continental-wallet/PWRU7750.html?dwcolor=001#q=spencer&start=1"
    driver.get(url)
    
    try:
        element=driver.find_element_by_xpath('//*[@id="Quantity"]/option').text
        if element == '1':
          print("IN STOCK got to "+url)
          requests.post(url='',data='{"text":"In stock! gotto kate spade"}')
        else:
          print(element)
    except NoSuchElementException:
        print("No element found")
