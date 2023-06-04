import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def driverSagre():
    url = 'https://sagresonline.tce.pb.gov.br/#/municipal/inicio'

    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.get(url)

    time.sleep(3)
    # feichando pop
    driver.find_element(
    By.CSS_SELECTOR,
    ".introjs-skipbutton" 
    ).click()

    return driver