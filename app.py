import requests, json, sqlite3, time

# Connect to the database
con = sqlite3.Connection("data.sqlite")
cur = con.cursor()
locations = [] # List to store locations, set to empty, so while loop runs

# Ask the user for a city name
while len(locations) == 0:
    city_name = input("Enter a city name: ")
    locations = cur.execute(f"SELECT GNIS, primary_lat_dec, primary_long_dec, state_name, name, last_updated, weather FROM us_cities WHERE Name LIKE '%{city_name}%'").fetchall()
    if len(locations) == 0:
        print(f"Could not find coordinates for {city_name}")

# If multiple locations are found, ask the user to select one
if len(locations) > 1:
    print("Multiple locations found. Please select one:")
    for i in range(len(locations)):
        print(f"{i+1}. {locations[i][4]}, {locations[i][3]}")
    selection = int(input("Enter the number of the location: "))
    GNIS, latitude, longitude, state, city_name, last_updated, weather = locations[selection-1]
else:
    print("City found!")
    GNIS, latitude, longitude, state, city_name, last_updated, weather = locations[0]

# Close the database connection
cur.execute("UPDATE us_cities SET last_updated = ? WHERE GNIS = ?", (int(time.time()),GNIS))
con.commit()
cur.close()
con.close()

# Base URL for NWS API
BASE_URL = "https://api.weather.gov"

# Step 1: Get the weather station grid point
grid_url = f"{BASE_URL}/points/{latitude},{longitude}"
grid_response = requests.get(grid_url)
grid_data = grid_response.json()
data = requests.get(grid_data["properties"]["forecastGridData"]).json()

# Extract forecast URL
forecast_url = grid_data["properties"]["forecast"]

# Step 2: Get the forecast
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(data, indent=4))

# Print the first forecast period
first_period = forecast_data["properties"]["periods"][0]
print(f"Location: {grid_data['properties']['relativeLocation']['properties']['city']}, {grid_data['properties']['relativeLocation']['properties']['state']}")
print(f"{first_period['name']}: {first_period['detailedForecast']}")