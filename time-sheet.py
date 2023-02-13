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
pswd = driver.find_element ("id", "password")

uname.send_keys("") #input username credentials
pswd.send_keys("") #input password credentials

driver.find_element("name", "_eventId_proceed").click()

#Pausing script for DUO
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("id", "trust-browser-button"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Time Sheet']"))).click()

#Pause code to click on day to start editing time sheet
WebDriverWait(driver, 10).until(EC.presenceofElementLocated(("name", "TimeIn")))

timein = driver.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[1]/input")
lunchout = driver.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
lunchoutAM = driver.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[4]/select").click()
lunchin = driver.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
lunchinAM = driver.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input").click()
timeout =

timein.send_keys("9:00")

#/html/body/div[3]/form/table[2]/tbody/tr/td/input