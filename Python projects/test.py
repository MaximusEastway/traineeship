import requests

# api-endpoint
URL = "http://dingdata.nl/premie"

# GET request naar de API uitvoeren
r = requests.get(url = URL, params = {'geslacht': 'man', 'geboortejaar': 1970, 'inkomen': 45000, 'kinderen': 2})

# Response body converteren naar JSON
response = r.json()

# In Python de JSON response body als variabelen gebruiken
print("Inkomen", response["resultaten"]["inkomen"])
print("Leeftijd", response["resultaten"]["leeftijd"])