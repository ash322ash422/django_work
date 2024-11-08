from django.shortcuts import render
import json #to load json data to python dictionary
import urllib.request # To make a request to api
from django.views import View

API_ID="892e6db9935e51f36b39a00987943b73" #I got it through email by signing up on their website
class WeatherView(View):
    
    def post(self, request, *args, **kwargs):#override
        city = request.POST['city']
        
        # source contain json data from api
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_ID).read()

        # converting json data to dictionary

        list_of_data = json.loads(source)
        print("list_of_data=",list_of_data)
        Farenheit = round(((list_of_data['main']['temp'] - 273.15) * (9/5)) + 32,2)
        Celsius = round(list_of_data['main']['temp'] - 273.15, 2)
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": 'LONGITUDE: ' + str(list_of_data['coord']['lon']) + \
                '; LATITUDE: ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'K; ' + str(Farenheit) + 'F; ' + str(Celsius) + 'C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
        return render(request, "mainapp/index.html",data)        
