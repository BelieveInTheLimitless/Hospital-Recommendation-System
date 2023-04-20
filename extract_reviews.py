from bs4 import BeautifulSoup
import pandas as pd

link = open("html.txt", encoding='utf-8')
soup = BeautifulSoup(link.read(), "lxml")

"GHT2ce"
"MyEned"

data = {
         'Rating': [],
         'Review': [],
     }


i = 0

#print(len(soup.find_all('div', class_="GHT2ce")))

# for review in soup.find_all('div', class_="GHT2ce"):
#         if i % 2:
#                 data['Review'].append(review.text)
#         i += 1


# for review in data['reviews'] :
#         print(review)

for review in soup.find_all('div', class_="MyEned"):
        data['Review'].append(review.text)

# print(soup.find_all('span', class_="kvMYJc"))

for stars in soup.find_all('span', class_="kvMYJc"):
        #print(stars['aria-label'])
        data['Rating'].append(stars['aria-label'])

for i in range(len(data['Review']), len(data['Rating'])):
        data['Review'].append('None')

df = pd.DataFrame(data)
df.to_csv('reviews.csv', index=False)