class PokeAPI:
    base_url = 'https://pokeapi.co/api/v2/'

'
    
    def __init__(self):
        
    #private method that will set up the requelt URL,
    #make the request, return the response data
    
    #the _ before the fxn name is a naming cnovention to signal this is a private method
    
    def _get(self, name, height, weight):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={name}"
        response = requests.get('https://pokeapi.co/api/v2/')
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        print(request_url)
        
    #public method that will call the private method and creat a weather object with the data
    
    def get_stats(self, height):
    
        poke_data = self.get(height, 'someting.json') ###--need to figure out
        if poke_data:
            name = poke_data['names']['name']
            poke_ob = GetStats
        
        # if weather_data:
        #     current_temp = weather_data['current']['temp_f']
        #     feels_like = weather_data['current']['feelslike_f']
        #     condition = weather_data['current']['condition']['text']
        #     city = weather_data['location']['name']
        #     city_obj = CityWeather(city, region, current_temp, feels_like, condition)
        #     return city_obj
            
        #     print(weather_data)
        # else:
        #     print('somehing wron')
        #     return None