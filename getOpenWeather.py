# Little python script to test Open Weather API and scrap some basic current weather data

import json, requests, sys

def read_location():
    with open('cities.txt') as f:
        cities = f.readlines()
    f.close()
    cities.append('Select new location')
    for i in range(len(cities)):
        cities[i] = cities[i].strip()
    i = 0
    print('What is your location?\n\nFrequent locations: ')
    for loc in cities:  
        print('(%i). %s' % (i, loc))
        i += 1

    location_n = input('\nSelect location number\n')
    location = cities[int(location_n)]
    if(location == 'Select new location'):
        location = input('Introduce new location:\n')
        return location
    else:
        return location

def get_data(loc):
    url2 = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=50a1db6532391640a9546cf65b4429bf&units=metric' % (loc)
    response = requests.get(url2)
    weatherData = response.json()
    return weatherData

def degree_conversion(windDegrees):
    if(int(windDegrees) > 270):
        return "↙"
    elif(int(windDegrees) > 180):
        return "↘"
    elif(int(windDegrees) > 90):
        return "↖"
    else:
        return "↗" 

def print_data(weather_data, location):
    temp = weather_data["main"]["temp"]
    feelslike = weather_data["main"]["feels_like"]
    windSpeed = round(weather_data["wind"]["speed"] * 3.6, 2)
    windDegrees = weather_data["wind"]["deg"]
    description = weather_data["weather"][0]["main"]
    humidity = weather_data["main"]["humidity"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]
    windDirection = degree_conversion(windDegrees)

    print('\033[1m' + "===============================================")
    print('Weather in %s:' % location)
    print('  > %s°C (Feels like %s°C)' % (temp, feelslike))
    print('  > ↓ %s°C    ↑ %s°C' % (temp_min, temp_max))
    print('  > Wind: %s km/h Direction: %s' % (windSpeed, windDirection))
    print('  > Humidity: ' + str(humidity) + '%')
    print('  > Sky description: ' + description)
    print("===============================================" + '\033[0m')

def main():
    location = read_location()
    weatherData = get_data(location)
    print_data(weatherData, location)

if __name__ == "__main__":
    main()  