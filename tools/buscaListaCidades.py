import time
from funcoesGerais import driverSagre
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os

path = f"{os.getcwd()}/docs/listaCidades.txt"


def buscaListaCidades():
    driver = driverSagre()

    time.sleep(2)
    driver.find_element(
        By.XPATH,
        "//*[@id='municipiosDropdown']/div/div[2]"
    ).click()

    cidade = driver.find_element(
        By.XPATH,
        "//*[@id='municipiosDropdown']/div/div[4]/div[2]/ul"
    ).get_attribute('outerHTML')

    driver.quit()

    htmlCidades = BeautifulSoup(
        cidade, 'lxml'
    )

    lista_cidade = [cidadeLi.text for cidadeLi in htmlCidades.find_all('li')]
    
    path = f"{os.getcwd()}/docs/listaCidades.txt"

    with open(path, 'w') as arquivo:
        arquivo.write(str(lista_cidade))

buscaListaCidades()