import httpx
import logging

logger = logging.getLogger(__name__)

class WeatherClient:
    def __init__(self, url: str, token: str) -> None:
        self.token = token
        self.client = httpx.Client(base_url=url)

    def get_weather_by_city(self, city_name: str) -> dict | None:
        weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
        params = {
            "key": self.token,
            "q": city_name,
            "format": "json",
            "num_of_days": 1,
            "lang": "ru"
        }

        try:
            result = self.client.get(weather_url, params=params)
            weather = result.json()

            if 'data' not in weather or 'current_condition' not in weather['data']:
                logger.warning(f"API не вернул ожидаемые данные для {city_name}")
                return None  

            logger.info(f"Успешно получены данные о погоде для {city_name}")
            return weather['data']['current_condition'][0]     
        except Exception as e:
            logger.exception(f"Ошибка при запросе погоды для {city_name}: {e}")
            return None