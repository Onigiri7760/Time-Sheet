#Setting up selenium for chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome("chromedriver")
import time
from datetime import datetime

#Pulling up MyPima website
browser.get ("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

#Logging into MyPima
usernameelement = browser.find_element ("id", "username")
passwordelement = browser.find_element ("id", "password")
username = input('Pima Username:')
password = input('Pima Password:')

usernameelement.send_keys(username) #input username credentials
passwordelement.send_keys(password) #input password credentials

browser.find_element("name", "_eventId_proceed").click()

#Pausing script for DUO
WebDriverWait(driver=browser, timeout=15).until(expected.element_to_be_clickable(("id", "trust-browser-button"))).click()
WebDriverWait(driver=browser, timeout=15).until(expected.element_to_be_clickable((By.XPATH, "//input[@value='Time Sheet']"))).click()

WebDriverWait(driver=browser, timeout=15).until(expected.presence_of_element_located((By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[3]/td")))

#currentweek = driver.find_element(By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[3]/td").text

#Start editing time sheet
#print(currentweek)

#print(datetime.date(currentweek).weekday())

monday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[8]").text
tuesday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[9]").text
wednesday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[10]").text
thursday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[11]").text
friday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[12]").text
saturday = browser.find_element (By.XPATH, "/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[6]").text

#workdays = blank array
#for(i=6;i<12;i++){
#    workDay = browser.find_element (By.XPATH, f"/html/body/div[3]/table[2]/tbody/tr[5]/td/form/table/tbody/tr/td[{i}]").text
#workdays += workDay
#}


day = input('What days do you work? ')

firstStartDay = (day.split()[0])
#firstStartDay = (workdays[0].split()[1])

browser.find_element(By.XPATH, "//a[@title='Enter Hours for Hourly Pay for ' + str(firststartday)]").click


#timein = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[1]/input")
#timeinAM = browser.find_element("XPATh", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[2]/select")
#lunchout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[4]/select")
#lunchin = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchinAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#timeout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input")
#timeoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select")


#time = input('What times do you work?')



