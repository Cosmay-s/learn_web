from flask import Flask
from weatherapp.weather import get_weather_by_city
from weatherapp.config import load_from_env


conf = load_from_env()

app = Flask(__name__)

@app.route("/")
def index():
    try:
        weather = get_weather_by_city("Moscow,Russia", conf.token)
        return {
            "temp": float(weather['temp_C']),
            "feels": float(weather['FeelsLikeC'])
        }
    except Exception as error:
        return {"error": str(error)}