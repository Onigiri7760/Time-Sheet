#Setting up selenium for chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("chromedriver")
import time

#Pulling up MyPima website
driver.get ("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

#Logging into MyPima
uname = driver.find_element ("id", "username")
uname.send_keys("jmaier1") #input username credentials
pswd = driver.find_element ("id", "password")
pswd.send_keys("Azkaban7760") #input password credntials
driver.find_element("name", "_eventId_proceed").click()

#Pausing script for DUO
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "Time Sheet")))
time.sleep(30)

#Script proceeds with time sheet edit
driver.find_element(By.XPATH, "//input[@type='submit']").click
