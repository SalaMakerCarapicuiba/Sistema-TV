import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Notices

def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Para requisições AJAX, só retornamos os dados do clima
            return JsonResponse({
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'temp_min': round(weather_data['main']['temp_min']),
                'temp_max': round(weather_data['main']['temp_max']),
            })

        # Para a primeira renderização da página, retornamos os usuários e notificações também
        users = User.objects.all()
        notices = Notices.objects.all()

        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'temp_min': round(weather_data['main']['temp_min']),
            'temp_max': round(weather_data['main']['temp_max']),
            'users': users,
            'notices': notices
        }

        return render(request, "index.html", context)

    except requests.exceptions.RequestException as e:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Erro ao conectar à API'}, status=500)
        return render(request, "index.html", {'error': 'Erro ao conectar à API'})

    except KeyError:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Erro ao processar os dados da API'}, status=500)
        return render(request, "index.html", {'error': 'Erro ao processar os dados da API'})
