from django.shortcuts import render
from django.contrib import messages
import requests
from django.conf import settings

def weatherView(request):
    try: 
        url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

        city = request.POST.get('city', 'Las Vegas')
        API_KEY = settings.OPEN_WEATHER_API_KEY

        city_weather = requests.get(url.format(city=city, API_KEY=API_KEY)).json()

        # Temperature shown in APi is in kelvin so converting it in Celsius
        api_temp = city_weather['main']['temp']
        current_temp = round(api_temp - 273.15)

        weather = {
            'city' : city,
            'temperature' : current_temp,
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        return render(request, 'weather/weather.html', {'weather':weather})
    except:
        return render(request, 'weather/weather.html')