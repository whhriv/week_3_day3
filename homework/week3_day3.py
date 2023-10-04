import requests
requests
base_url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
api_method = '/poke_res.json'
request_url = f"{base_url}{api_method}"

class PokeAPI:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str_(self):
        return f"nombre estas {self.name} and he weighs {self.weight} at {self.height} tall"
    
    def _get(self, height, weight, name):
        request_url = f"{self.base_url}"
        poke_res = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
        data=poke_res.json()
        data.keys()
        height = data.get('height')
        poke_obj = poke_res(height)
        return poke_obj

print(f" Height: {height}, Weight: {weight} and name {nombre}")
