#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
'''
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
'''

# location = input('Location?')

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/city?id=1795565&APPID=1dd2005eaae49a0e1a5fabbc2faf1d77' 
response = requests.get(url)
response.raise_for_status()

 # Load JSON data into a Python variable.
weatherData = json.loads(response.text)
   # Print weather descriptions.
w = weatherData['list']
# print(('Current weather in {0}:').format(location))
print('Current weather in Shenzhen: ')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])