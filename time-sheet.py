#Setting up selenium for chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome("chromedriver")
import time

#Pulling up MyPima website
browser.get ("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

#Logging into MyPima
usernameelement = browser.find_element ("id", "username")
passwordelement = browser.find_element ("id", "password")
username = input(Pima Username:)
password = input(Pima Password:)

usernameelement.send_keys(username) #input username credentials
passwordelement.send_keys(password) #input password credentials

browser.find_element("name", "_eventId_proceed").click()

#Pausing script for DUO
WebDriverWait(driver=browser, timeout=10).until(expected.element_to_be_clickable(("id", "trust-browser-button"))).click()
WebDriverWait(driver=browser, timeout=10).until(expected.element_to_be_clickable((By.XPATH, "//input[@value='Time Sheet']"))).click()

#Pause code to click on day to start editing time sheet
WebDriverWait(browser, 10).until(expected.presenceofElementLocated(("name", "TimeIn")))

timein = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[1]/input")
timeinAM = browser.find_element("XPATh", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[2]/select")
lunchout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
lunchoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[4]/select")
lunchin = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
lunchinAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
timeout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input")
timeoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select")

timein.send_keys("9:00")

#For people that work after 12PM
#timeinAM.send_keys("PM")
#actions.send_keys(keys.ENTER)

lunchout.send_keys("")
