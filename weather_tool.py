import openmeteo_requests
from geopy.geocoders import Nominatim
from openmeteo_sdk.Variable import Variable
import requests_cache
from retry_requests import retry
from datetime import datetime

def weather_tool(query: str):
    """
    Tells the current temperature and humidity of a certain location based on the query.

    Args:
        query (str): The Location.

    Returns:
        str: the temperature and humidity of the place.
    """
    def weather(lat, lon):
      # Setup the Open-Meteo API client with cache and retry on error
      cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
      retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
      openmeteo = openmeteo_requests.Client(session=retry_session)
  
      # Make sure all required weather variables are listed here
      # The order of variables in hourly or daily is important to assign them correctly below
      url = "https://api.open-meteo.com/v1/forecast"
      params = {
          "latitude": lat,
          "longitude": lon,
          "current": ["temperature_2m", "relative_humidity_2m"]
      }
      responses = openmeteo.weather_api(url, params=params)
  
      # Process first location. Add a for-loop for multiple locations or weather models
      response = responses[0]
  
      current = response.Current()
      current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
  
      # Extract temperature and humidity
      current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
      current_relative_humidity_2m = next(filter(lambda x: x.Variable() == Variable.relative_humidity and x.Altitude() == 2, current_variables))
  
      # Convert Unix timestamp to readable format
      timestamp = current.Time()
      readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
  
      # Display the results in a more presentable format
      return (
          f"\nWeather Information for {place.title()}:\n"
          f"Date and Time: {readable_time}\n"
          f"Temperature: {current_temperature_2m.Value():.2f}°C\n"
          f"Relative Humidity: {current_relative_humidity_2m.Value():.2f}%"
      )
    
    def get_coordinates(place_name):
      try:
          # Initialize geolocator
          geolocator = Nominatim(user_agent="geoapi")
  
          # Get location details
          location = geolocator.geocode(place_name)
  
          # Extract latitude and longitude
          if location:
              return location.latitude, location.longitude
          else:
              return "Place not found"
      except Exception as e:
          return f"An error occurred: {e}"
    
    # Example usage
    place = query
    coordinates = get_coordinates(place)
    
    if isinstance(coordinates, tuple):
        return(weather(coordinates[0], coordinates[1]))
    else:
        return(coordinates)