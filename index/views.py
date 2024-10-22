import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Notices
import datetime

def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'

    # URL da previsão do tempo
    url_forecast = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=pt_br'

    try:
        # Obtendo os dados da previsão para os próximos dias
        response_forecast = requests.get(url_forecast)
        response_forecast.raise_for_status()
        forecast_data = response_forecast.json()

        # Clima atual
        current_weather = forecast_data['list'][0]
        current_description = current_weather['weather'][0]['description']

        # Clima de amanhã
        tomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        forecast_tomorrow = None
        for forecast in forecast_data['list']:
            if tomorrow_date in forecast['dt_txt'] and '12:00:00' in forecast['dt_txt']:
                forecast_tomorrow = forecast
                break

        agora = datetime.datetime.now()
        data_em_texto = '{}/{}/{}'.format(agora.day, agora.month, agora.year)

        # Obtenção das notícias
        notices = Notices.objects.all()
        total_notices = notices.count()

        # Índice da notícia enviado pelo AJAX (padrão: 0)
        notice_index = int(request.GET.get('notice_index', 0)) % total_notices

        current_notice = notices[notice_index]

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Resposta para AJAX com dados da notícia e do clima
            return JsonResponse({
                'notice_image': current_notice.imagem.url if current_notice.imagem else None,
                'notice_title': current_notice.subject,
                'notice_content': current_notice.content,
                'notice_category': current_notice.category,
                'total_notices': total_notices,
                'temp_min': round(current_weather['main']['temp_min']),
                'temp_max': round(current_weather['main']['temp_max']),
                'description': current_description,
                'temp_min_tomorrow': round(forecast_tomorrow['main']['temp_min']) if forecast_tomorrow else None,
                'temp_max_tomorrow': round(forecast_tomorrow['main']['temp_max']) if forecast_tomorrow else None,
                'description_tomorrow': forecast_tomorrow['weather'][0]['description'] if forecast_tomorrow else None,
                'agora': agora,
                'hora_atual': agora.hour
            })

        # Renderização inicial da página completa
        context = {
            'city': city,
            'temperature': current_weather['main']['temp'],
            'description': current_description,
            'temp_min': round(current_weather['main']['temp_min']),
            'temp_max': round(current_weather['main']['temp_max']),
            'temp_min_tomorrow': round(forecast_tomorrow['main']['temp_min']) if forecast_tomorrow else None,
            'temp_max_tomorrow': round(forecast_tomorrow['main']['temp_max']) if forecast_tomorrow else None,
            'description_tomorrow': forecast_tomorrow['weather'][0]['description'] if forecast_tomorrow else None,
            'users': User.objects.all(),
            'notices': notices,
            'agora': agora,
            'data': data_em_texto,
            'hora_atual': agora.hour
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
