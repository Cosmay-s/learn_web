import httpx

def get_weather_by_city(city_name, token):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": token,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }

    with httpx.Client() as client:
        result = client.get(weather_url, params=params)
        weather = result.json()

    if 'data' not in weather or 'current_condition' not in weather['data']:
        return False   
    try:
        return weather['data']['current_condition'][0]
    except (IndexError, TypeError):
        return False