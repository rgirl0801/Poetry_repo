import json

import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
response = requests.get(url)
print(response.status_code)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
response = requests.get(url)
print(response)
assert response.status_code == 200, 'Wrong status code'
print(response.status_code)

url1 = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid=6b8c1c61a55bf4b35a4c960182fd85dd'

response1 = requests.get(url)
# jprint(response1.json())

r = requests.post('https://httpbin.org / post', data={'key': 'value'})

print(r)

# print content of request
print(r.json())
