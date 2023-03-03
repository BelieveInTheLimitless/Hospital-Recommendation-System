import csv
import googlemaps

# Set up the Google Maps API client
api_key = 'AIzaSyBzFeRsrQtomI0E-Czwa0j5aq_N1volIvA'
gmaps = googlemaps.Client(api_key)

# Search for hospitals near a specific location
location = 'Pune'
radius = 5000  # meters
query = 'hospital'
places_result = gmaps.places(query, location=location, radius=radius)

# Extract the relevant information from the API response
results = []
for place in places_result['results']:
    result = {
        'name': place['name'],
        'address': place['formatted_address'],
        'location': place['geometry']['location'],
        'rating': place.get('rating', ''),
        'types': place['types'],
    }
    results.append(result)

# Save the results to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'address', 'location', 'rating', 'types']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)