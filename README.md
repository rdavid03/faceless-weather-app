# Faceless Weather App

## How to run
- Clone repository
- Run `app.py`
- If any errors occur with the database (`data.sqlite`) run the `prepare_database.py`

## About Project
The main goal of this project was to show off how useful free to use APIs are. I also used a free places and counties csv to create a database of counties and places along with their longitude and latitude as to pass off to NOAA with an API call. Running this all locally results in quicker outputs, as well as no need for a third-party API call to figure out the longitude and latitude of a given place. The csv file can be found on [Data.gov](https://catalog.data.gov/dataset/national-incorporated-places-and-counties).

### **Note:** 
Since the projects operates using NOAA, only places in the USA are able to be tracked.
