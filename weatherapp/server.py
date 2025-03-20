from flask import Flask
from weatherapp.weather import get_weather_by_city
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ["WEATHER_TOKEN"]

app = Flask(__name__)

@app.route("/")
def index():
    weather = get_weather_by_city("Moscow,Russia", token)
    if weather:
        return f"Сейчас {weather['temp_C']}°C, ощущается как {weather['FeelsLikeC']}°C"
    else:
        return "Прогноз сейчас недоступен"