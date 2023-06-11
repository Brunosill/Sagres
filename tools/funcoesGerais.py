import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def driverSagre(apresentar = False):
    url = 'https://sagresonline.tce.pb.gov.br/#/municipal/inicio'

    option = Options()
    option.headless = apresentar
    #driver = webdriver.Firefox(options=option)
    driver = webdriver.Chrome(options=option)
    driver.get(url)

    time.sleep(3)
    # fe|i|chando pop
    driver.find_element(
    By.CSS_SELECTOR,
    ".introjs-skipbutton" 
    ).click()

    return driver

def selecionaLocalidadeAno(driver, cidade="Cuitegi", ano="2022"):
    #clica menu ano
    driver.find_element(
        By.XPATH,
        "//*[@id='exercicioDropdown']"
    ).click()
    #dar ano
    driver.find_element(
        By.XPATH,
        "//*[@id='exercicioDropdown']/div/div[4]/div[1]/input"
    ).send_keys(ano)
    #confimar ano
    driver.find_element(
        By.XPATH,
        "//*[@id='exercicioDropdown']/div/div[4]/div[2]/ul/p-dropdownitem/li"
    ).click()

    
    #clica na opção localidade
    driver.find_element(
        By.XPATH,
        "//*[@id='municipiosDropdown']/div/div[2]/span"
    ).click()
    #da a localidade
    driver.find_element(
        By.XPATH,
        "//*[@id='municipiosDropdown']/div/div[4]/div[1]/input"
    ).send_keys(cidade)
    #clica na localidade
    driver.find_element(
        By.XPATH,
        "//*[@id='municipiosDropdown']/div/div[4]/div[2]/ul/p-dropdownitem/li"
    ).click()   

    return driver