from selenium.webdriver.common.by import By
import time

from tools.funcoesGerais import driverSagre, selecionaLocalidadeAno

driver = driverSagre()
driverLocalidade = selecionaLocalidadeAno(driver)
