import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=35.6944&longitude=51.4215&hourly=temperature_2m"
location = "delhi technologicaluniversity"
PARAM = {"adress": location}

info = requests.get(url=URL, params=PARAM)
data = info.json()
temps = data["hourly"]["temperature_2m"]
print(temps)
