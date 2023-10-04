import requests
requests

class PokeAPI:
    base_url = 'https://pokeapi.co/api/v2/'

    
#     def __init__(self, api_key):
#         self.api_key = api_key
        
    #private method that will set up the requelt URL,
    #make the request, return the response data
    
    #the _ before the fxn name is a naming cnovention to signal this is a private method
    
    def _get(self, height ):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={city}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        print(request_url)
        
    #public method that will call the private method and creat a weather object with the data
    
    def get_poke_height(self, height):
        poke_height = self._get(height, '/poke_res.json')
        if poke_height:
            Pika_height = poke_height['height']
            
            poke_obj = poke(height)
            return poke_obj
            
            print(get_poke_height)
        else:
            print('somehing wron')
            return None
        
