import logging
from flask import Flask
from weatherapp.weather import WeatherClient
from weatherapp.config import load_from_env
import dataclasses as dc

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

conf = load_from_env()
app = Flask(__name__)

weather_client = WeatherClient("http://api.worldweatheronline.com", conf.token)

logger.info("Сервер запущен")

@dc.dataclass
class WeatherResult:
    temp: float
    feels: float

@app.route("/")
def index():
    logger.info("Запрос погоды")
    weather = weather_client.get_weather_by_city("Moscow,Russia")
    
    if not weather:
        logger.error("Не удалось получить данные о погоде")
        return {"error": "Ошибка получения данных"}, 500
    
    weather_result = WeatherResult(
        temp=float(weather['temp_C']),
        feels=float(weather['FeelsLikeC'])
    )

    logger.info(f"Успешно получены данные о погоде: {weather_result}")
    return dc.asdict(weather_result)


@app.errorhandler(Exception)
def handle_exception(error):
    error_message = str(error)
    logger.exception(f"Глобальная ошибка: {error_message}")
    return {"error": error_message}, 500


@app.route('/favicon.ico')
def favicon():
    return '', 204
