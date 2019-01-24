import requests
import json
from django.shortcuts import render
from django.shortcuts import redirect
from .models import City
from .forms import CityForm

def view(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&id=5128581&units=imperial&appid=b07b77de54c870219b0c77d46f9fdfa0'
    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()



    cities = City.objects.all()
    weather_data = []


    for city in cities:
        response = requests.get(url.format(city)).json()
        city_weather = {
            'city':city.name,
            'temperature':response['main']['temp'],
            'description':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)



    context = {'weather_data' : weather_data, 'form':form}
    if request.method =='POST':
        return render(request,'home/info.html',{'weather_data' : weather_data, 'form':form})
    else:
        return render(request,'home/weather.html',context)

def infoview(request):
    return render(request,'home/info.html',{})