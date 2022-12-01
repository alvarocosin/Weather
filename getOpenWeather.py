import json, requests, sys

# APPID = 'weatherkey'

location = input('What is your location?\n')

url2 = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=50a1db6532391640a9546cf65b4429bf&units=metric' % (location)

response = requests.get(url2)

weatherData = response.json()

temp = weatherData["main"]["temp"]
windSpeed = weatherData["wind"]["speed"] * 3.6
description = weatherData["weather"][0]["description"]

print('El tiempo en %s es de %s°C' % (location, temp))
print('Viento: %s km/h' % windSpeed)
print(description)