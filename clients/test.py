import requests

endpoint = 'http://localhost:8000/api_view/'
endpoint2 = 'http://localhost:8000/api_view/person/'
endpoint3 = 'http://localhost:8000/api_view/person/f730d55e-eb64-49e8-8b4d-c09f167d40dc'

get_response = requests.get(endpoint, params={"nombre": "maría"})
print(get_response.json()['message'])

get_response = requests.get(endpoint2)
print(get_response.json())

get_response = requests.get(endpoint3)
print(get_response.json())