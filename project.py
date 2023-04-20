import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('hospitals_data.csv')

# Extract the column you want to copy into a new DataFrame
new_df = df[['Name','Co-ordinates','Rating','Info']]

# Save the new DataFrame to a new CSV file
new_df.to_csv('output_file.csv', index=False)

data = pd.read_csv('output_file.csv')

# Define a function to extract the hospital type
def extract_type(Info):
    # Split the address string by comma
    parts = Info.split('·')
    # print(parts[1])
    parts = parts[0].split(',')
    # The city name should be the second-to-last part
    hos_type = parts[0].strip()
    return hos_type

def extract_number(Rating):

    parts = Rating.split('(')
    #print(parts)
    number = parts[1].split(')')
    Return = number[0]
    return Return

def extract_rating(Rating):

    parts = Rating.split('(')
    #print(parts)
    return parts[0]

def extract_latitude(coordinates):

    parts = coordinates.split("('")
    number = parts[1]
    number = number.split(",")
    latitude = number[0].split("'")
    print(latitude[0])
    return latitude[0]

def extract_longitude(coordinates):

    parts = coordinates.split("('")
    number = parts[1]
    number = number.split(",")
    longitude = number[1].split("'")
    longitude = longitude[1].split("'")
    print(longitude[0])
    return longitude[0]


# Define a function to extract the hospital type
def extract_address(Info):
    # Split the address string by comma
    parts = Info.split('·')
    print(parts)
    address = parts[1]
    return address

# Apply the function to the 'Address' column to extract the city name

data['Latitude'] = data['Co-ordinates'].apply(extract_latitude)
data['Longitude'] = data['Co-ordinates'].apply(extract_longitude)
data['Ratings'] = data['Rating'].apply(extract_rating)
data.drop(['Rating'], axis=1)
data['Type_hospital'] = data['Info'].apply(extract_type)
data['Address_Contact'] = data['Info'].apply(extract_address)
data['Number_of_Ratings'] = data['Rating'].apply(extract_number)

# Save the updated DataFrame to a new CSV file
data.to_csv('modified.csv', index=False)
