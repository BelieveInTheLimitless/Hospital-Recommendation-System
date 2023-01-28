from bs4 import BeautifulSoup
import requests
import pandas as pd

pages = [i for i in range(1, 9)]

suburbs = []

subs = open('pune_suburbs.txt', 'r')

for line in subs:
    line = line.lower()
    line = line.replace(' ', '-')
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace('.', '')
    line = line.strip()
    suburbs.append(line)

subs.close()


for suburb in suburbs:
    data = {
        'Name': [],
        'Type': [],
        'Rating': [],
        'Delivery Time': [],
        'Price': []
    }

    for page in pages:
        source = requests.get("https://www.swiggy.com/city/pune/" + str(suburb) + "-restaurants?page=" + str(page)).text

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
    if suburb == suburbs[0]:
        df.to_csv('pune_restaurants_data.csv', index=False)
    else:
        df.to_csv('pune_restaurants_data.csv', mode='a', index=False, header=False)

