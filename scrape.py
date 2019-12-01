import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://shop.mango.com/gb/women/coats-quilted-coats/hood-quilted-coat_53048813.html?c=99&n=1&s=prendas_she.familia;15")
    driver.find_element_by_xpath("//form/div[2]/div/span").click()
    result = driver.find_element_by_xpath('/html/body/div[4]/div/form/div[2]/div[1]/main/div/div[3]/div[3]/form/div[2]/div/div/span[1]').text
    if result == 'XS - Not available I want it!':
        print('OOS' + result)
        requests.post(url='https://hooks.slack.com/services/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',data='{"text":"Out of stock!"}')
    else:
        requests.post(url='https://hooks.slack.com/services/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',data='{"text":"In stock!"}')

    # https://shop.mango.com/gb/women/coats-quilted-coats/hood-quilted-coat_53048813.html?c=99&n=1&s=prendas_she.familia;15
    