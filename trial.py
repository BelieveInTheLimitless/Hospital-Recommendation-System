from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import requests
import numpy as np
import time

# Set up the driver
driver = webdriver.Firefox()


# Load the page
# url = "https://www.google.com/maps/search/hospitals/"

#print(driver.title)
print("Hospitals Data\n")
iterate = []

for lat in range(10, 17, 1):
    for lon in range(73, 75, 1):
        url = "https://www.google.com/maps/search/hospitals+near+me/@"+str(lat)+","+str(lon)+",10z"
        driver.get(url)

        time.sleep(5)

        hospitals_list = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')

        for hospital in hospitals_list:
            print(hospital.get_attribute('aria-label'))
            iterate.append(hospital.get_attribute('aria-label'))

        df = pd.DataFrame(iterate)
        df.to_csv('Medical.csv')


# Close the driver
driver.quit()

