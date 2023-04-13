import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('hospitals_data.csv')

# Extract the column you want to copy into a new DataFrame
new_df = df[['Name','Co-ordinates','Rating','Info']]

# Save the new DataFrame to a new CSV file
new_df.to_csv('output_file.csv', index=False)

data = pd.read_csv('output_file.csv')

# Define a function to extract the city name
def extract_city(Info):
    # Split the address string by comma
    parts = Info.split('·')
    parts = parts[0].split(',')
    # The city name should be the second-to-last part
    city = parts[0].strip()
    return city

# Apply the function to the 'Address' column to extract the city name
data['Type_hospital'] = data['Info'].apply(extract_city)

# Save the updated DataFrame to a new CSV file
data.to_csv('modified.csv', index=False)
