from geopy.geocoders import Nominatim #pip install geopy

def geocode(city, country):
          geopy = Nominatim(user_agent="test")

          location = geopy.geocode(f"{city}, {country}").raw
          return location