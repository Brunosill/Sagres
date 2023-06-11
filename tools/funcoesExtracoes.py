from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def indicadoresGovernmentais(driver):
    driver.find_element(
        By.XPATH,
        "//*[@id='megamenu']/ul/li[2]/a"
    ).click()
    menuBruto = driver.find_element(
        By.XPATH,
        "//*[@id='megamenu']/ul/li[2]/div"
    ).get_attribute('outerHTML')
    driver.find_element(
        By.XPATH,
        "//*[@id='megamenu']/ul/li[2]/a"
    ).click()


    menuHTML = BeautifulSoup(
        menuBruto, 'lxml'
    )
    listaIndicadoresGovernamentais = {}

    for div in menuHTML.find_all("div", {"class":"menu-group ng-star-inserted"}):

        listaIndicadoresGovernamentais[div.find("label").text] = [a["href"] for a in div.find_all("a")]
    
    return listaIndicadoresGovernamentais