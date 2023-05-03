import requests
import pandas

data = pandas.read_csv("Raw_data.csv")
print(data["Latitude"][0])

address_list = []
for (index, value) in data.iterrows():
    lat = value["Latitude"]
    lon = value["Longitude"]
    response = requests.get(url=f"https://geocode.maps.co/reverse?lat={lat}&lon={lon}", verify=False)
    response.raise_for_status()
    data_api = response.json()
    address = data_api["display_name"]
    address_list.append(address)

data["address_api"] = address_list
data.to_csv("output.csv")
