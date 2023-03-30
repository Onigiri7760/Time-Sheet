#Import necessary libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

#Setting up Selenium for Chrome
browser = webdriver.Chrome("chromedriver")

#Accessing MyPima website
browser.get ("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

#Loggin to MyPima
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

WebDriverWait(driver=browser, timeout=15).until(expected.presence_of_element_located((By.XPATH, "/html/body/div[3]/table/tbody/tr[3]/td")))


#Gather dates for the current week
workdays = [browser.find_element (By.XPATH, f"/html/body/div[3]/table/tbody/tr[5]/td/form/table/tbody/tr/td[{x}]").text
    for j in range(6, 13)
    for x in [j]]

#Remove newline character from each element in workdays
workdays = [day.replace('\n', ' ') for day in workdays]
for workday in workdays:
    # Convert the workday string to a datetime object
    date_obj = datetime.strptime(workday, '%A %b %d, %Y')
    # Convert the datetime object to element format
    formatted_date = date_obj.strftime('%A %d-%b-%Y').replace(date_obj.strftime('%b'), date_obj.strftime('%b').upper())
    print(formatted_date)

#Ask the user for a weekdays
weekday_user_input = input('What days do you work? ')
weekdays = [day.strip().lower() for day in weekday_user_input.split(',')]

#Find the corresponding weekday for each user input weekday

for weekday in weekdays:
    weekday_index = next((i for i, day in enumerate(workdays) if weekday in day.lower()), None)
    if weekday_index is not None:
     #print the corresponding weekday from the workDay list
        print(workdays[weekday_index])
    else:
        print("Invalid weekday.")


#firstStartDay = (day.split()[0])
#firstStartDay = (workdays[0].split()[1])

#browser.find_element(By.XPATH, "//a[@title='Enter Hours for Hourly Pay for ' + str(firststartday)]").click


#timein = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[1]/input")
#timeinAM = browser.find_element("XPATh", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[2]/select")
#lunchout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[4]/select")
#lunchin = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchinAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#timeout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input")
#timeoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select")


#time = input('What times do you work?')



