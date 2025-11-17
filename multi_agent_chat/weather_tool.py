"""Weather API integration module using HG Brasil API."""

import os
import logging
from typing import Optional
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def obter_clima(city: str) -> str:
    """
    Retrieve weather forecast for a given city using HG Brasil API.
    
    Args:
        city: Name of the city to get weather information for.
        
    Returns:
        A formatted string with weather information including description,
        maximum and minimum temperatures. Returns an error message if
        the request fails.
        
    Raises:
        No exceptions are raised; errors are returned as strings.
    """
    # Input validation
    if not city or not isinstance(city, str):
        logger.error("Invalid city parameter: must be a non-empty string")
        return "Erro: Nome da cidade inválido."
    
    city = city.strip()
    if not city:
        logger.error("Empty city name provided")
        return "Erro: Nome da cidade não pode ser vazio."
    
    # Get API key from environment variable
    hg_key = os.getenv("HG_BRASIL_API_KEY")
    if not hg_key:
        logger.error("HG_BRASIL_API_KEY environment variable not set")
        return "Erro: Chave da API HG Brasil não configurada. Configure a variável de ambiente HG_BRASIL_API_KEY."
    
    try:
        url = "https://api.hgbrasil.com/weather"
        params = {"key": hg_key, "city_name": city}
        
        logger.info(f"Fetching weather data for city: {city}")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if API returned valid results
        if "results" not in data:
            logger.warning(f"No results found for city: {city}")
            return f"Erro: Não foi possível obter informações do clima para {city}. Verifique o nome da cidade."
        
        forecast = data.get("results", {}).get("forecast", [{}])[0]
        max_temp = forecast.get("max")
        min_temp = forecast.get("min")
        description = forecast.get("description")
        
        if not all([max_temp, min_temp, description]):
            logger.warning(f"Incomplete weather data for city: {city}")
            return f"Erro: Dados incompletos do clima para {city}."
        
        logger.info(f"Successfully retrieved weather for {city}")
        return f"Hoje: {description}. Máxima de {max_temp}°C e mínima de {min_temp}°C."
        
    except requests.exceptions.Timeout:
        logger.error(f"Timeout while fetching weather for {city}")
        return f"Erro: Tempo esgotado ao consultar o clima para {city}. Tente novamente."
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error for city {city}: {str(e)}")
        return f"Erro ao consultar o clima para {city}: Problema na comunicação com a API."
    except (KeyError, IndexError, ValueError) as e:
        logger.error(f"Data parsing error for city {city}: {str(e)}")
        return f"Erro ao processar dados do clima para {city}."
    except Exception as e:
        logger.error(f"Unexpected error for city {city}: {str(e)}")
        return f"Erro inesperado ao consultar o clima para {city}."