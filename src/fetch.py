import requests
import os

class Fetch:
    def __init__(self, city_name):
        self.city_name = city_name
        self.image_id = None
        self.api_token = os.environ.get("API_KEY")
        self.api_base_url = os.environ.get("BASE_URL")
    
    # Get weather icon form open weather map API
    def get_weather_icon(self, image_id):
        self.image_id = image_id
        image_url = f"https://openweathermap.org/img/w/{self.image_id}.png"
        res = requests.get(image_url, stream=True)

        if res.status_code == 200:
            return res.content
        return res.status_code
    
    #  Get weather form open weather map API for a city
    def get_weather(self): 
        params = {
            'q': self.city_name,
            'appid' : self.api_token,
            'units' : 'metric'
        }

        response = requests.get(self.api_base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
        

    #  Get weather form open weather map API for a city for next day forecast  
    def get_forecast(self):
        params = {
            "q": self.city_name,
            "appid": self.api_token,
            "units": "metric",
            "cnt": 1
        }
        res = requests.get(self.api_base_url, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            print("ERROR: ", res.status_code)
            return None