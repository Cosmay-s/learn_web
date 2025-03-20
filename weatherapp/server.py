from flask import Flask
from weatherapp.weather import get_weather_by_city
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ["WEATHER_TOKEN"]

app = Flask(__name__)

@app.route("/")
def index():
    try:
        weather = get_weather_by_city("Moscow,Russia", token)
        return {
            "temp": float(weather['temp_C']),
            "feels": float(weather['FeelsLikeC'])
        }
    except Exception as error:
        return {"error": str(error)}