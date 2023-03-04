from selenium import webdriver
from selenium.webdriver.common.by import By
#This will not run on online IDE
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import numpy as np
import time

# Set up the driver
driver = webdriver.Firefox()
temp = "https://www.google.com/maps/search/hospitals+in+nashik/"

area = open('areas.txt', 'r')

iterate = []

for line in area:
    line = line.lower()
    line = line.replace('-', '+')
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace('.', '')
    line = line.strip()
    iterate.append(line)

area.close()


# Load the page
# url = "https://www.google.com/maps/search/hospitals/"

#print(driver.title)
print("Hospitals Data\n")


for i in iterate:

    url = "www.google.com/maps/search/hospitals+in+"+str(i)
    driver.get(url)

    hospitals_list = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')

    for hospital in hospitals_list:
            print(hospital.get_attribute('aria-label'))
            iterate.append(hospital.get_attribute('aria-label'))

    df = pd.DataFrame(iterate)
    df.to_csv('Medical.csv')


# Close the driver
driver.quit()

