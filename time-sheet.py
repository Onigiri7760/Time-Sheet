#Import necessary libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

# Function that is executed when the Submit button is clicked
def analyze_data():
    # Get the values entered in the GUI
    weekdays_value = weekdays.get()
    start_time_value = start_time.get()
    end_time_value = end_time.get()
    lunch_out_value = lunch_out.get()
    lunch_in_value = lunch_in.get()

# Initialize the GUI
root = tk.Tk()
root.title("Pima College Time Sheet")

# Define variables
weekdays = tk.StringVar()
start_time = tk.StringVar()
end_time = tk.StringVar()
lunch_out = tk.StringVar()
lunch_in = tk.StringVar()

# Label and Entry for the weekdays entry
weekdays_label = tk.Label(root, text="Weekdays (comma separated):")
weekdays_label.grid(row=0, column=0, padx=5, pady=5)
weekdays_entry = tk.Entry(root, textvariable=weekdays)
weekdays_entry.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry for the start date entry
start_time_label = tk.Label(root, text="Start time:")
start_time_label.grid(row=1, column=0, padx=5, pady=5)
start_time_entry = tk.Entry(root, textvariable=start_time)
start_time_entry.grid(row=1, column=1, padx=5, pady=5)

# Label and Entry for the end date entry
end_time_label = tk.Label(root, text="End Time:")
end_time_label.grid(row=2, column=0, padx=5, pady=5)
end_time_entry = tk.Entry(root, textvariable=end_time)
end_time_entry.grid(row=2, column=1, padx=5, pady=5)

# Label and Entry for the lunch out entry
lunch_out_label = tk.Label(root, text="Lunch Out:")
lunch_out_label.grid(row=3, column=0, padx=5, pady=5)
lunch_out_entry = tk.Entry(root, textvariable=lunch_out)
lunch_out_entry.grid(row=3, column=1, padx=5, pady=5)

# Label and Entry for the lunch in entry
lunch_in_label = tk.Label(root, text="Lunch In:")
lunch_in_label.grid(row=4, column=0, padx=5, pady=5)
lunch_in_entry = tk.Entry(root, textvariable=lunch_in)
lunch_in_entry.grid(row=4, column=1, padx=5, pady=5)

# Button to initiate the analysis process
Submit_button = tk.Button(root, text="Submit", command=analyze_data)
Submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Run the GUI event loop
root.mainloop()

#Setting up Selenium for Chrome
browser = webdriver.Chrome("chromedriver")

#Accessing MyPima website
browser.get ("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

#Login to MyPima
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

#Ask the user for a weekdays
weekday_user_input = input('What days do you work? (Seperate with commas) ')
weekdays = [day.strip().lower() for day in weekday_user_input.split(',')]

#Find the corresponding weekday for each user input weekday
for weekday in weekdays:
    weekday_index = next((i for i, day in enumerate(workdays) if weekday in day.lower()), None)
    if weekday_index is not None:
     #print the corresponding weekday from the workDay list
        print(workdays[weekday_index])
    else:
        print("Invalid weekday.")


FirstStartDay = (weekday_user_input.split()[0])

browser.find_element(By.XPATH, f"//a[@title='Enter Hours for Hourly Pay for {FirstStartDay}]").click


#timein = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[1]/input")
#timeinAM = browser.find_element("XPATh", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[2]/select")
#lunchout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[4]/select")
#lunchin = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#lunchinAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[2]/td[3]/input")
#timeout = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input")
#timeoutAM = browser.find_element("XPATH", "/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select")


#time = input('What times do you work?')



