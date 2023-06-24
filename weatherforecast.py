#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:29:26 2023

@author: paul : Student - 1st year BTech CSE
"""

import requests, sys

help_message = '''
Usage: weathermap.py [-c|-f|-C|-F] <city>
For Help -> Usage: weathermap.py [-h]
Options: -c for Current Weather in metric units, -f for 5-day Forecast in metric units, -C for Current Weather in imperial units, -F for 5-day Forecast in imperial units, -h for help
'''

option = '-c'

def validateInput():
    '''validate the input from CLI'''
    if len(sys.argv) > 3 or len(sys.argv) == 1:
        print(help_message)
        sys.exit()
    else:
        if len(sys.argv) == 3:
            city = sys.argv[2]
        else: 
            '''if sys.argv[1][0] == '-': print help message else take the input as city'''
            if sys.argv[1][0] == '-':
                print(help_message)
                sys.exit()
            else:
                city = sys.argv[1]
    return city

def checkValidCity(response, CITY):
    '''check if the city is valid and print error message if not'''
    if response['cod'] == '404':
        print("-------------------------------------------------------")
        print(sys.argv[0] + ": '" + CITY + "' city not found")
        print("-------------------------------------------------------")
        sys.exit()


def checkCLIOptions():
    '''
        if valid CLI options are '-c' or '-f' or '-C' or '-F' or '-h' then check for valid option in sys.argv[1]
    '''
    if len(sys.argv) == 3:
        global option
        option = sys.argv[1]
        return (option == '-c' or option == '-f' or option == '-h' or option == '-C' or option == '-F')
    else:
        return True       
    
    

def processCLIOptions():
    '''
        if no option, default to current weather
        if option is '-c' then make the base url for current weather in metric units
        if option is '-f' then make the base url for 5-day daily forecast in metric units
        if option is '-C' then make the base url for current weather in imperial units
        if option is '-F' then make the base url for 5-day daily forecast in imperial units
        if option is '-h' then print help 
    '''
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    if option == '-f':
        BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?units=metric"
    elif option == '-C':
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    elif option == '-F':
        BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?units=imperial"
    elif option == '-h':
        print(help_message)
        sys.exit()
    return BASE_URL
        
def parseJSONforCITY(response, CITY):
    '''
    print only for key = main, key = wind speed and key = weather[main] in a pretty format
    '''

    met = {'-f': ('°C','m/s'), '-F': ('°F','mph'), '-c': ('°C','m/s'), '-C': ('°F','mph')}

    if option == '-f' or option == '-F':
        print("5-day Forecast for " + CITY)
        """check for date field
           if the day is same, print the content in the same line
           if the day is different, print the content in the next line
        """
        day = ""
        for i in range(0, len(response['list'])):
            if day == response['list'][i]['dt_txt'][0:10]:
                print("Time: " + response['list'][i]['dt_txt'][11:16] + " Temperature: " + str('%.1f' % (response['list'][i]['main']['temp'])) + met[option][0] + " Weather: " + response['list'][i]['weather'][0]['main'])
            else:
                day = response['list'][i]['dt_txt'][0:10]
                print("-------------------------------------------------------")
                print("Date: " + day)
                print("Time: " + response['list'][i]['dt_txt'][11:16] + " Temperature: " + str('%.1f' % (response['list'][i]['main']['temp'])) + met[option][0] + " Weather: " + response['list'][i]['weather'][0]['main'])             

    else:
        print("-------------------------------------------------------")
        print("Current Weather for " + CITY)
        #convert to centrigrade and set precision 1
        print("Temperature: " + str('%.1f' % (response['main']['temp'])) + met[option][0])
        print("Wind Speed: " + str('%.1f' % (response['wind']['speed'])) + met[option][1])
        print("Weather: " + response['weather'][0]['main'])
        #print other conditions including feels like,humidity, temp_min, temp_max
        print("Feels Like: " + str('%.1f' % (response['main']['feels_like'])) + met[option][0])
        print("Humidity: " + str(response['main']['humidity']) + "%")
        print("Minimum Temperature: " + str('%.1f' %  (response['main']['temp_min'])) + met[option][0])
        print("Maximum Temperature: " + str('%.1f' %  (response['main']['temp_max'])) + met[option][0])
        print("-------------------------------------------------------")



# main program starts here

if (not checkCLIOptions()):
    print(help_message)
    sys.exit()
else:
    CITY = validateInput()

BASE_URL = processCLIOptions()
API_KEY = "58a126b51c7d6afe705982030b1c7499"
URL = BASE_URL + "&appid=" + API_KEY + "&q=" + CITY

response = requests.get(URL)
response = response.json()

checkValidCity(response, CITY)
parseJSONforCITY(response, CITY)
