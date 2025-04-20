import requests
import csv

# Ask user for city name
city = input("Enter the name of the city: ").strip()

# Overpass API endpoint
overpass_url = "https://overpass-api.de/api/interpreter"

# Overpass Query Template with dynamic city name
query = f"""
[out:json][timeout:30];
area["name"="{city}"]["boundary"="administrative"]["admin_level"="6"]->.searchArea;
(
  node["tourism"](area.searchArea);
  way["tourism"](area.searchArea);
  relation["tourism"](area.searchArea);
);
out center;
"""

# Send the query to the Overpass API
response = requests.get(overpass_url, params={'data': query})

# Parse the response
data = response.json()
elements = data.get("elements", [])

print(f"Found {len(elements)} tourist attractions in {city}")

# Prepare CSV
filename = f"{city.lower().replace(' ', '_')}_tourist_attractions.csv"
with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Type", "Latitude", "Longitude"])

    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name", "Unnamed")
        tourism_type = tags.get("tourism", "Unknown")

        if el.get("type") == "node":
            lat = el.get("lat")
            lon = el.get("lon")
        else:
            center = el.get("center", {})
            lat = center.get("lat")
            lon = center.get("lon")

        writer.writerow([name, tourism_type, lat, lon])

print(f"CSV file '{filename}' created successfully.")
