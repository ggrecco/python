from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

print("Iniciando nosso robo...\n")

# usa o software baixado para abrir o site
driver = webdriver.Chrome("C:\Users\gustavo.grecco\robos_python\chromedriver.exe")

# site que será aberto
driver.get("")