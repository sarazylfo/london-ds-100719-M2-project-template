
import requests
from dotenv import load_dotenv
import os
load_dotenv()
class MongoHandler():
    pass
class WeatherGetter():
    def __init__(self, time = None):
        self.BASE_URL = 'https://api.darksky.net/'
        self.SECRET_KEY = os.getenv("DARKSKYAPI")
        self.time = time
        
        
    def weather_getter(self, time):
        forcast = requests.get(f"{self.BASE_URL}forecast/{self.SECRET_KEY}/52.5200,13.4050,{time}?exclude=minutely,hourly,daily,alerts,flags")
        return forcast


