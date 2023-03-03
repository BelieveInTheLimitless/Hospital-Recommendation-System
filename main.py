from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Firefox()

# Load the page
url = "https://www.google.com/maps/search/hospitals/"
driver.get(url)
print(driver.title)


hospitals_list = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')

for hospital in hospitals_list:
    print(hospital.get_attribute('aria-label'))

# Close the driver
driver.quit()