import requests

# HEADER: Learning JSON, api url and .get()
# when?: using the github api to import latest stats/commit for a currently building section on my portfolio

city = "Orlando"
url = 'http://api.weatherapi.com/v1/current.json?key=a2f4701974274454abf84031261708&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in Orlando is", description, "and", temp, "degrees.")


