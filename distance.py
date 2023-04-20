import pandas as pd

lat = float(input("Enter your latitude: "))
lon = float(input("Enter your longitude: "))

ran = float(input("Enter the range(in km): ")) #in km

change_per_deg_lat = 111.2
change_per_deg_long = 105.75

df = pd.read_csv("modified.csv")

for row in df.itertuples():

        x = abs(float(row[6]) - lon) * change_per_deg_long
        y = abs(float(row[5]) - lat) * change_per_deg_lat
        dist = (x**2 + y**2)**(1/2)

        if dist <= ran:
                print(row[1])

