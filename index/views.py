import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'
    response = requests.get(url)
    weather_data = response.json()
    
    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'temp_min': round(weather_data['main']['temp_min']),
        'temp_max': round(weather_data['main']['temp_max']),
    }
    return render(request, "index.html", context)

