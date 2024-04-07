import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

city_name = input("Enter the city name: ")

OW_api_key = os.getenv("OPENWEATHER_API_KEY")

OW_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OW_api_key}&units=metric"

print(OW_api_url)

response = requests.get(OW_api_url)
response_json = response.json()

print(response_json)
print(response_json["main"])
print(response_json["main"]["temp"])
print(response_json["weather"][0]["main"])

data = json.dumps(response_json, indent=4)
