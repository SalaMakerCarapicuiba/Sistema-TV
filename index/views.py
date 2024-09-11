import requests
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

    try:
        # Fazendo a requisição para a API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida
        weather_data = response.json()

        # Dados do clima processados
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'temp_min': round(weather_data['main']['temp_min']),
            'temp_max': round(weather_data['main']['temp_max']),
        }

        # Verifica se a requisição foi feita via AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(context)

        # Caso contrário, renderiza o template com os dados
        return render(request, "index.html", context)

    except requests.exceptions.RequestException as e:
        # Trata erros de conexão ou HTTP
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Erro ao conectar à API'}, status=500)
        return render(request, "index.html", {'error': 'Erro ao conectar à API'})

    except KeyError:
        # Trata erros de chave ao processar a resposta da API
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Erro ao processar os dados da API'}, status=500)
        return render(request, "index.html", {'error': 'Erro ao processar os dados da API'})
    