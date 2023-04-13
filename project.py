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

# Define a function to extract the hospital type
def extract_address(Info):
    # Split the address string by comma
    parts = Info.split('·')
    print(parts)
    address = parts[1]
    return address

# Apply the function to the 'Address' column to extract the city name
data['Type_hospital'] = data['Info'].apply(extract_type)
data['Address_Contact'] = data['Info'].apply(extract_address)

# Save the updated DataFrame to a new CSV file
data.to_csv('modified.csv', index=False)
