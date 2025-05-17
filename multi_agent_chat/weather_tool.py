import requests

HG_KEY = "SUA_CHAVE_HG_BRASIL"

def obter_clima(city: str) -> str:
    try:
        url = "https://api.hgbrasil.com/weather"
        params = {"key": HG_KEY, "city_name": city}
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        forecast = data.get("results", {}).get("forecast", [{}])[0]
        max_temp = forecast.get("max")
        min_temp = forecast.get("min")
        description = forecast.get("description")
        return f"Hoje: {description}. Máxima de {max_temp}°C e mínima de {min_temp}°C."
    except Exception as e:
        return f"Erro ao consultar o clima para {city}: {str(e)}"