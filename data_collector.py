# import libraries
import requests
from dotenv import load_dotenv
import os

load_dotenv()

final_data = []

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print('Error getting the API KEY')


def get_lat_lot(city, api_key):
    URL = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
    try:
        response = requests.get(url=URL)
        if response.status_code == 200:
            data = response.json()
            if data:
                lat = data[0]['lat']
                lon = data[0]['lon']
                return lat, lon
            else:
                print('Data not found!')
        else:
            print(f'Error with status code: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')


def get_final_data(city, api_key):
    lat, lon = get_lat_lot(city, api_key)
    URL = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
    try:
        response = requests.get(url=URL)
        if response.status_code == 200:
            data = response.json()
            data = data['list']

            for value in data:
                entry = {
                    'datetime': value['dt_txt'],
                    'temp': value['main']['temp'],
                    'feels_like': value['main']['feels_like'],
                    'humidity': value['main']['humidity'],
                    'weather_main': value['weather'][0]['main'],
                    'description': value['weather'][0]['description'],
                    'wind_speed': value['wind']['speed'],
                    'wind_gust': value['wind'].get('gust', None),
                }
                final_data.append(entry)
            return final_data

        else:
            print(f'Error with status code: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')

