import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Notices
import datetime

def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'
    
    # Usando apenas o endpoint de previsão
    url_forecast = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=pt_br'
    
    try:
        # Obtendo os dados da previsão para os próximos dias, incluindo o clima atual
        response_forecast = requests.get(url_forecast)
        response_forecast.raise_for_status()
        forecast_data = response_forecast.json()

        # Clima atual (usamos a primeira previsão disponível, que é do horário mais próximo)
        current_weather = forecast_data['list'][0]

        # Extraindo a data de amanhã
        tomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
        # Procurando a previsão de amanhã para o meio-dia (12:00:00)
        forecast_tomorrow = None
        for forecast in forecast_data['list']:
            if tomorrow_date in forecast['dt_txt'] and '12:00:00' in forecast['dt_txt']:
                forecast_tomorrow = forecast
                break

        # Obtendo a data e hora atual
        agora = datetime.datetime.now()
        data_em_texto = '{}/{}/{}'.format(agora.day, agora.month, agora.year)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Para requisições AJAX, retornamos também a data e hora
            return JsonResponse({
                'city': city,
                'temperature': current_weather['main']['temp'],
                'description': current_weather['weather'][0]['description'],
                'temp_min': round(current_weather['main']['temp_min']),
                'temp_max': round(current_weather['main']['temp_max']),
                'temp_min_tomorrow': round(forecast_tomorrow['main']['temp_min']) if forecast_tomorrow else None,
                'temp_max_tomorrow': round(forecast_tomorrow['main']['temp_max']) if forecast_tomorrow else None,
                'agora': agora,  # Inclui o horário atual formatado
                'data_em_texto': data_em_texto  # Data formatada para exibição
            })

        # Para a primeira renderização da página, retornamos os usuários e notificações também
        users = User.objects.all()
        notices = Notices.objects.all()

        context = {
            'city': city,
            'temperature': current_weather['main']['temp'],
            'description': current_weather['weather'][0]['description'],
            'temp_min': round(current_weather['main']['temp_min']),
            'temp_max': round(current_weather['main']['temp_max']),
            'temp_min_tomorrow': round(forecast_tomorrow['main']['temp_min']) if forecast_tomorrow else None,
            'temp_max_tomorrow': round(forecast_tomorrow['main']['temp_max']) if forecast_tomorrow else None,
            'users': users,
            'notices': notices,
            'agora': agora,
            'data': data_em_texto
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
