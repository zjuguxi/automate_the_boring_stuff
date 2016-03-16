#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys
from twilio.rest import TwilioRestClient 

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

from twilio.rest import TwilioRestClient 
main = w[0]['weather'][0]['main']
description = w[0]['weather'][0]['description']

# Text message from Twilio, unfinished
# put your own credentials here 
ACCOUNT_SID = "AC825858b8b7226b32ed899d11e0a55da5" 
AUTH_TOKEN = "c01335c6267aff225c27d7d285ab5bbd" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+8618657120319", 
    from_="+12016887056", 
    body='明天深圳天气是%s - %s ' % (main, description)
)