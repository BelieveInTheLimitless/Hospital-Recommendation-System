from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

pages = np.arange(1, 8, 1)

areas = ["thergaon", "varye-bk", "lonikand", "kolwadi", "alandi-chorachi", "pimpalgaon-mahalunge", "kuruli", "kalewadi", "shivajinagar", "bibvewadi", "hadpsar-ie", "khadki-bazar", "mohamadwadi", "chinchwadgaon", "phursungi", "karvenagar", "n-i-b-m", "viman-nagar", "baner-road", "kothrud", "navsahyadri", "sadashiv-peth", "khadakwal", "ghotondi", "sonari", "varale", "pimpri-bk", "vasuli", "pimpri", "kolvadi", "mulanagar", "sate", "saygaon", "kondhwa-kh", "wakad", "malewadi", "hadapsar", "khadki", "parvati", "shivajinagar-pune", "deccan-gymkhana", "swargate-chowk", "dapodi", "bhukum", "kondhwa-lh", "kalas", "tathawade", "khadaki", "baner", "airport-pune", "market-yard-pune", "akurdi", "dehu", "lonavala-bazar", "shivnagar", "vagholi", "katraj", "aundh-pune"]

data = {
    'Name': [],
    'Type': [],
    'Rating': [],
    'Delivery Time': [],
    'Price': []
}

for page in pages:

    for area in areas:
        
        source = requests.get("https://www.swiggy.com/city/pune/" + str(area) + "-restaurants?page=" + str(page)).text

        soup = BeautifulSoup(source, 'lxml')

        for restaurant in soup.find_all('div', class_='_3XX_A'):

            name = restaurant.find('div', class_='nA6kb').text

            type = restaurant.find('div', class_='_1gURR').text

            details = restaurant.find('div', class_='_3Mn31').text
            details = details.split('•')

            rating = details[0]

            minutes = details[1]

            price_for_two = details[2]


            data['Name'].append(name)
            data['Type'].append(type)
            data['Rating'].append(rating)
            data['Delivery Time'].append(minutes)
            data['Price'].append(price_for_two[1:])


        df = pd.DataFrame(data)

df.to_csv('restaurants_data.csv')
