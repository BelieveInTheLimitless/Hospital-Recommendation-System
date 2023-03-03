import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Firefox()

# Load the page
url = "https://www.google.com/search?q=laptop+screen+height+in+pixels&ei=ABMCZPT7E6jJz7sPyKuoSA&oq=24.5+c&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgCMgQIABBDMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHkoECEEYAFAAWABghRVoAHAAeACAAc0BiAHNAZIBAzItMZgBAMABAQ&sclient=gws-wiz-serp"
driver.get(url)
time.sleep(5)
scroll_pause_time = 5
height = driver.execute_script("return document.body.scrollHeight")
#print(driver.title)
print("Hospitals Data\n")

# Create an empty list to store hospitals data
hospitals_list = []

while True:
    # Find all hospitals on the current page
    #hospitals = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')
    # Append the hospitals to the hospitals_list
    #hospitals_list.extend(hospitals)
    
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    new_height = driver.execute_script("return document.body.scrollHeight")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if height == new_height:
        break
    height = new_height

# Print the hospitals data
for hospital in hospitals_list:
    print(hospital.get_attribute('aria-label'))

driver.quit()