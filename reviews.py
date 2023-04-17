import time
from options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import bs4 as BeautifulSoup

options = Options()
options.add_argument("--lang=en")
driver = webdriver.Chrome(chrome_options=options)

url = "https://www.google.com/maps/place/Deccan+Hardikar+Hospital./@18.4777544,73.7928943,12z/data=!4m10!1m2!2m1!1shospitals+near+me!3m6!1s0x3bc2c080b5a1ac0b:0xdfdf8b393abef469!8m2!3d18.5304104!4d73.8474815!15sChFob3NwaXRhbHMgbmVhciBtZSIDkAEBkgEIaG9zcGl0YWzgAQA!16zL20vMGJwZjhf"

driver.get(url)
wait = WebDriverWait(driver, 10)
menu_bt = wait.until(EC.element_to_be_clickable(
                       (By.XPATH, '//button[@data-value=\'Sort\']'))
                   )  
menu_bt.click()
recent_rating_bt = driver.find_elements_by_xpath(
                                     '//div[@role=\'menuitem\']')[1]
recent_rating_bt.click()
time.sleep(5)

response = BeautifulSoup(driver.page_source, 'html.parser')
rlist = response.find_all('div', class_='section-review-content')

id_r = rlist.find('button', 
              class_='section-review-action-menu')['data-review-id']
username = rlist.find('div', 
                  class_='section-review-title').find('span').text
try:
    review_text = rlist.find('span', class_='section-review-text').text
except Exception:
    review_text = Nonerating = rlist.find('span', class_='section-review-stars')['aria-label']

rel_date = rlist.find('span', class_='section-review-publish-date').text

scrollable_div = driver.find_element_by_css_selector(
 'div.section-layout.section-scrollbox.scrollable-y.scrollable-show'
                     )

driver.execute_script(
               'arguments[0].scrollTop = arguments[0].scrollHeight', 
                scrollable_div
               )