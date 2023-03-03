from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Firefox()

# Load the page
url = "https://www.google.com/maps/search/hospitals/"
driver.get(url)

# Find all the div elements with class 'hfpxzc'
hfpxzc_divs = driver.find_elements(By.CLASS_NAME, "DUwDvf fontHeadlineLarge")
# Print the divs
for div in hfpxzc_divs:
    print(div.tag_name)

# Close the driver
driver.quit()