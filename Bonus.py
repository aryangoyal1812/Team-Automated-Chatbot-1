# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 04:02:34 2021

@author: USER
"""

import requests 
def getWeather():
# Enter your API key here 
    api_key = "9c9623d2c835fb356931d3b0b8d19c4a"
      
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
      
    # Give city name 
    city_name = "Mandi"
      
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "q=" + city_name  + "&appid=" + api_key 
      
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
      
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
      
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
        # store the value of "main" 
        # key in variable y 
    y = x["main"] 
      
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
      
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
      
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
      
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
      
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
      
    # print following values 
    return("The weather at IIT Mandi is:\n Temperature (in Celsius) = " +
                    str(round((current_temperature-273),0)) + 
          "\n Atmospheric Pressure (in kPa) = " +
                    str(current_pressure/10) +
          "\n Humidity (in %) = " +
                    str(current_humidiy) +
          "\n Description = " +
                    str(weather_description)) 
import datetime
def getTime():
    now = datetime.datetime.now()
    s= "Current date: "
    s+= now.strftime("%d-%m-%Y")
    s+= "\nCurrent time: "
    s+= now.strftime("%H:%M")
    return s

    