from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from bs4 import BeautifulSoup
import time
import pandas as pd
import os
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://portal.ciee.org.br/para-voce/vagas/")

# selecionar o dropdown de estados
select_estado = Select(driver.find_element(By.CLASS_NAME, "option-estado"))
select_estado.select_by_value("5")

# aceitando os cookies
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT, "Concordo").click()

for e in range(20):
    # espera a pagina carregar
    driver.implicitly_wait(4)

    # scroll pro fim da pagina
    #driver.execute_script("window.scrollTo(0, 614);")
    scroll = ActionChains(driver)
    scroll.move_to_element(driver.find_element(By.CLASS_NAME, "btn-carregar"))

    # clica no botao "carregar mais"
    botao_carregar = driver.find_element(By.CLASS_NAME, "btn-carregar")
    # botao_carregar = driver.find_element(By.LINK_TEXT, "Carregar mais vagas")
    botao_carregar.click()


#-------- DEBUG ------- (deixa o navegador aberto, impedindo que o script acabe)
while(True):
    pass
