from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Firefox()

# Load the page
url = "https://www.google.com/maps/search/hospitals/"
driver.get(url)
print(driver.title)

# Find all the div elements with class 'hfpxzc'
hospitals_list = driver.find_elements(By.CLASS_NAME, "DUwDvf fontHeadlineLarge")
# Print the divs
for hospital in hospitals_list:
    print(hospital.tag_name)

# Close the driver
driver.quit()