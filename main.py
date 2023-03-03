import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import Select
import json


url = 'https://sagresonline.tce.pb.gov.br/#/municipal/inicio'

option = Options()
option.headlees = True
driver = webdriver.Firefox(options= option)

driver.get(url)
time.sleep(2)

# FEICHAR POPAPE 
driver.find_element(
    By.XPATH,
    "html//body//div[4]//div//div[5]//a[1]"
).click()
time.sleep(2)


def ListaCidadeAno():
    #lista de cidades
    driver.find_element(
        By.XPATH,
        "html//body//app-root//div//header//div//ul//li[2]//app-localidade-selector//p-dropdown//div//div[2]//span"
    ).click()
    
    element = driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[4]/div[2]/ul'
    )
    html_element = element.get_attribute('outerHTML')
    
    page = BeautifulSoup(
        html_element, 'html.parser'
    )
    lista_cidades = [tag.text for tag in page.find_all("div")]

    

    return ListaCidadeAno

def listaAno():

    #lista de anos
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[3]/span"
    ).click()
    elementAno = driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[4]/div[2]/ul'
    ).get_attribute('outerHTML')
    TagAno = BeautifulSoup(
        elementAno, 'html.parser'
    )
    listaAno = [tag.text for tag in TagAno.find_all('li')]

    return listaAno

ListaCidadeAno()

def SelecionarCidade(cidade):
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[3]/span"
    ).click()
    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[4]/div[1]/input'
    ).send_keys(cidade)

    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[4]/div[2]/ul/p-dropdownitem/li/div/div"
    ).click()

    print('Cidade selecionada')

SelecionarCidade('Cuitegi')

def SelecionarAno(ano):
    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[4]/div[1]/input'
    ).send_keys(ano)
    
    print('ano plantado')
    time.sleep(23)

SelecionarAno('2022')

time.sleep(40)
driver.quit()