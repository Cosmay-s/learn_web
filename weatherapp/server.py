import logging
from flask import Flask, jsonify
from weatherapp.weather import WeatherClient
from weatherapp.config import load_from_env
import dataclasses as dc


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="w",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)

conf = load_from_env()
app = Flask(__name__)

@dc.dataclass
class WeatherResult:
    temp: float
    feels: float

@app.route("/")
def index():
    weather = WeatherClient.get_weather_by_city("Moscow,Russia", conf.token)
    weather_result = WeatherResult(
        temp=float(weather['temp_C']),
        feels=float(weather['FeelsLikeC'])
    )
    return dc.asdict(weather_result)


@app.errorhandler(Exception)
def handle_exception(error):
    error_message = str(error)
    logger.exception(f"Глобальная ошибка: {error_message}")
    return {"error": error_message}, 500
