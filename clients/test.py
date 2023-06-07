import requests

endpoint = 'http://localhost:8000/api_view/'
get_response = requests.get(endpoint, params={"nombre": "maría"})
print(get_response.json()['message'])