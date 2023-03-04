from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


lat = 18.4581802  # 18.4481802
lon = 73.7737253
restart = 73.7737253  # 73.7737253

for j in range(20):  #30
        lon = restart
        for i in range(15): #21
                driver = webdriver.Firefox(executable_path=r'E:\Firefox\geckodriver.exe')
                url = "https://www.google.com/maps/search/hospital/@"+str(lat)+","+str(lon)+",16z"
                driver.get(url)

                time.sleep(3)


                data = {
                        "Name": [],
                        "Co-ordinates": [],
                        "Rating": [],
                        "Type": []
                }


                hospitals_list = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')
                ratings = driver.find_elements_by_class_name("AJB7ye")

                hosp_info = driver.find_elements_by_class_name("W4Efsd")
                type_hosp = []

                for k in range(len(hosp_info)):
                        s = hosp_info[k].text
                        if s.find(")") > 0 or s.find("No reviews") == 0:
                                type_hosp.append(hosp_info[k + 1].text)

                for k in range(len(hospitals_list)):
                        hospital = hospitals_list[k]
                        rating = ratings[k].text
                        typeh = type_hosp[k][:type_hosp[k].find("·")]

                        #print(hospital.get_attribute('aria-label'), end=" ")
                        name = hospital.get_attribute('aria-label')

                        link = hospital.get_attribute('href')
                        r1 = link.find('!3d')
                        r2 = link.find('!4d')
                        r3 = link.find('!16s')

                        #print("Co-ordinates:", link[r1 + 3:r2], ",", link[r2 + 3:r3], end=" ")
                        coord = (link[r1 + 3:r2], link[r2 + 3:r3])

                        #print("Rating: ", rating, end=" ")

                        #print("Type: ", typeh)

                        data['Name'].append(name)
                        data['Co-ordinates'].append(coord)
                        data['Rating'].append(rating)
                        data['Type'].append(typeh)




                # hospitals_list = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')
                #
                # for hospital in hospitals_list:
                #     print(hospital.get_attribute('aria-label'))
                #     iterate.append(hospital.get_attribute('aria-label'))
                lon = lon + 0.015  # 0.015
                driver.quit()

                df = pd.DataFrame(data)
                if i == 0 and j == 0:
                        df.to_csv('hospitals_data.csv', index=False)
                else:
                        df.to_csv('hospitals_data.csv', mode='a', index=False, header=False)

        lat = lat + 0.010  # 0.012



