import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

url = 'https://sagresonline.tce.pb.gov.br/#/municipal/inicio'

option = Options()
option.headlees = True
driver = webdriver.Chrome(options=option)

driver.get(url)
time.sleep(5)

def feicharPop():
#Feichar poppap 
    driver.find_element(
        By.CSS_SELECTOR,
        ".introjs-skipbutton" 
    ).click()
feicharPop()

time.sleep(1)
def selecionarCidade(cidade):
    #selecão cidade
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[2]/span"
    ).click()
    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[4]/div[1]/input'
    ).send_keys(cidade)
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[2]/app-localidade-selector/p-dropdown/div/div[4]/div[2]/ul/p-dropdownitem/li/div/div"
    ).click()
selecionarCidade('Cuitegi')
time.sleep(1)
def SelecionarAno(ano):
    #selecionar ano 
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[2]/span"
    ).click()
    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[4]/div[1]/input'
    ).send_keys(ano)
    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/ul/li[1]/sg-exercicio-selector/div/div/p-dropdown/div/div[4]/div[2]/ul/p-dropdownitem/li'
    ).click()
SelecionarAno("2022")
time.sleep(1)
    #selecionar detalhes 

def selecaoOpcao():
    driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/header/div/megamenu/div/ul/li[2]/a"
    ).click()

    driver.find_element(
        By.XPATH,
        '/html/body/app-root/div/header/div/megamenu/div/ul/li[2]/div/div[3]/ul/li[4]/a'
    ).click()

selecaoOpcao()
time.sleep(1)
feicharPop()
time.sleep(1)
elemento = driver.find_element(
    By.CSS_SELECTOR,
    '.ag-center-cols-viewport'
).get_attribute('outerHTML')

page = BeautifulSoup(
    elemento, 'lxml'
)
dicio = {
    "codUnidadeGestora":[],
    "ano" :[],
    "mes" :[],
    "numero" :[],
    "dataLancamento" :[],
    "codBanco":[],
    "numAgencia":[],
    "numContaBancaria":[],
    "codFornecedor":[],
    "nomeFornecedor":[]
}
driver.quit()
for tag in page.find_all('div',{'class':'ag-row'}):
    print(tag.find_all('div')[0].text)
    dicio["codUnidadeGestora"].append(tag.find_all('div')[0].text)
    dicio["ano"].append(tag.find_all('div')[1].text)
    dicio["mes"].append(tag.find_all('div')[2].text)
    dicio["numero"].append(tag.find_all('div')[3].text)
    dicio["dataLancamento"].append(tag.find_all('div')[4].text)
    dicio["codBanco"].append(tag.find_all('div')[5].text)
    dicio["numAgencia"].append(tag.find_all('div')[6].text)
    dicio["numContaBancaria"].append(tag.find_all('div')[7].text)
    dicio["codFornecedor":].append(tag.find_all('div')[8].text)
    dicio["nomeFornecedor"].append(tag.find_all('div')[9].text)
    
print(pd.DataFrame(dicio))


"""
    table = driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/div/app-despesa-extraorcamentaria/panel/div/div[2]/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div"
    ).get_attribute('outerHTML')
    print(BeautifulSoup(table, 'html.parser')) """
