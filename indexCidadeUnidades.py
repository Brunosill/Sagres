import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://sagresonline.tce.pb.gov.br/#/municipal/inicio'

option = Options()
option.headless = False
driver = webdriver.Chrome(options=option)
driver.get(url)
time.sleep(3)

#feichar pop
driver.find_element(
    By.CSS_SELECTOR,
    ".introjs-skipbutton" 
).click()

#lista de cidades

driver.find_element(
    By.XPATH,
    "//*[@id='municipiosDropdown']/div/div[2]"
).click()

cidade = driver.find_element(
    By.XPATH,
    "//*[@id='municipiosDropdown']/div/div[4]/div[2]/ul"
).get_attribute('outerHTML')

htmlCidades = BeautifulSoup(
    cidade, 'lxml'
)

time.sleep(4)

print(htmlCidades.)
driver.quit()