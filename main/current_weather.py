import requests as rq #pip install requests
import json

#uses openweathermap. (For further informaton vist: https://openweathermap.org )
def get_weather(openweathermap_api_key, latitude, longitude):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={openweathermap_api_key}"
        response = rq.get(url)
        if response.status_code == 200:
          weather_data = response.json() 
          with open("weather.json", "w") as json_file:
                    json.dump(weather_data, json_file, indent=4)
                    print("weather.json")
        else:
          print(f"Error: {response.status_code}")
