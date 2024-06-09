import os
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('7264345092:AAGCYsJ3hct1JKTnPEEbr49g5KOdiOmb1L8')
WEATHER_API_KEY = os.getenv('ae2f7888d076b6cc4794517a58cc78e4')
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your Weather bot!\nSend me a city name to get the weather forecast.")

@dp.message_handler()

def get_weather_data(city):
    try:
        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'uk'
        }
        response = requests.get(WEATHER_API_URL, params=params)
        data = response.json()
        if data['cod'] != 200:
            return None

        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_message = (f"Погода в місті {city}:\n"
                           f"Опис: {weather_desc}\n"
                           f"Температура: {temp}°C\n"
                           f"Відчувається як: {feels_like}°C\n"
                           f"Вологість: {humidity}%\n"
                           f"Швидкість вітру: {wind_speed} м/с")

        return weather_message
    except Exception as e:
        print(e)
        return None