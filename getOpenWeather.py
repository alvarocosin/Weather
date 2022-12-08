# Little python script to test Open Weather API and scrap some basic current weather data

import json, requests, sys

def read_location():
    frequent_locations = ['Zaragoza', 'Valencia', 'Madrid', 'London', 'Select new location']

    i = 0
    print('What is your location?\n\nFrequent locations: ')
    for loc in frequent_locations:  
        print('(%i). %s' % (i, loc))
        i += 1

    location_n = input('\nSelect location number\n')
    location = frequent_locations[int(location_n)]
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
        return "NE"
    elif(int(windDegrees) > 180):
        return "NW"
    elif(int(windDegrees) > 90):
        return "SE"
    else:
        return "SW" 

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

    print("===============================================")
    print('Weather in %s:' % location)
    print('  > %s°C (Feels like %s°C)' % (temp, feelslike))
    print('  > Min: %s°C | Max: %s°C' % (temp_min, temp_max))
    print('  > Wind: %s km/h | Direction: %s' % (windSpeed, windDirection))
    print('  > Humidity: ' + str(humidity) + '%')
    print('  > Sky description: ' + description)
    print("===============================================")

def main():
    location = read_location()
    weatherData = get_data(location)
    print_data(weatherData, location)

if __name__ == "__main__":
    main()  