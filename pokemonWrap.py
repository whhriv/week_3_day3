import requests
requests

class WeatherAPI:
    base_url = 'https://pokeapi.co/api/v2/'
'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    #private method that will set up the requelt URL,
    #make the request, return the response data
    
    #the _ before the fxn name is a naming cnovention to signal this is a private method
    
    def _get(self, uid=none, api_method ):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={city}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        print(request_url)
        
    #public method that will call the private method and creat a weather object with the data
    
    def get_current_weather(self,city):
        weather_data = self._get(city, '/current.json')
        if weather_data:
            current_temp = weather_data['current']['temp_f']
            feels_like = weather_data['current']['feelslike_f']
            condition = weather_data['current']['condition']['text']
            city = weather_data['location']['name']
            city_obj = CityWeather(city, region, current_temp, feels_like, condition)
            return city_obj
            
            print(weather_data)
        else:
            print('somehing wron')
            return None