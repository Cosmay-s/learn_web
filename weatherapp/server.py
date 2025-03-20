from flask import Flask
from weatherapp.weather import get_weather_by_city
from weatherapp.config import load_from_env
import dataclasses as dc


conf = load_from_env()
app = Flask(__name__)


@dc.dataclass
class WeatherResult:
    temp: float
    feels: float


@app.route("/")
def index():
    try:
        weather = get_weather_by_city("Moscow,Russia", conf.token)
        weather_result = WeatherResult(
            temp=float(weather['temp_C']),
            feels=float(weather['FeelsLikeC'])
        )
        return dc.asdict(weather_result)
    except Exception as error:
        return {"error": str(error)}
