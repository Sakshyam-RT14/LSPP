from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": 'kathmandu',
        "appid": API_KEY,
        "units": "imperial"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        print(response.text)

        data = response.json()


        print(f"\nWeather in {city}")
        print("-" * 20)
        print("Condition:", data["weather"][0]["main"])
        print("Description:", data["weather"][0]["description"])
        print("Temperature:", data["main"]["temp"], "°F")
        print("Country:", data["sys"]["country"])

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


city = input("Enter city: ")
get_weather(city)