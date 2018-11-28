import requests
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"2c62c85d5b93b25db85b32e2c43de2b6"}
response = requests.get(endpoint, params=payload)
data = response.json()
print data['main']
print response.url
print response.status_code
print response.headers["content-type"]
print response.text