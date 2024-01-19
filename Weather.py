import requests
import json


api_key = "da42472ab6573016598b252b694b3c4c"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" +str(city) +"&appid=" + api_key 

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = json.loads(response.text)

        
        main = data['main']
        temperature = main['temp'] - 273.15  
        humidity = main['humidity']
        pressure = main['pressure']
        weather = data['weather'][0]['description']

        
        print("Weather in", city + ":")
        print("Temperature:", "{:.2f}".format(temperature), "°C")
        print("Humidity:", humidity, "%")
        print("Pressure:", pressure, "hPa")
        print("Weather:", weather)
    else:
        print("Error: City not found or invalid API key")


city = input("Enter a city: ")
get_weather(city)