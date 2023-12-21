# Import Elevation data

import requests
import urllib
import pandas as pd

# USGS Elevation Point Query Service
#url = r'https://nationalmap.gov/epqs/pqs.php?
#new 2023:
url = r'https://epqs.nationalmap.gov/v1/json?'

# coordinates with known elevation[,],[],[],[],[],[],[],[],[],[],[]]
lat = [44.4151072]
lon = [-72.8343026]

# create data frame
df_ele = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

def elevation_function(df_ele, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df_ele[lat_column], df_ele[lon_column]):
                
        # define rest query params
        params = {
            'x': lon,
            'y': lat,
            'units': 'Feet',
            'wkid': 4326,
            'includeDate': 'False'
        }
        
        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        #elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])
        #new 2023:
        elevations.append(result.json()['value'])

    df_ele['elev_feet'] = elevations

elevation_function(df_ele, 'lat', 'lon')
print(df_ele.head())
    