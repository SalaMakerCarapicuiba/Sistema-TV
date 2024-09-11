import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    api_key = '98e4910ec3fd6f86dfbfd39f589051bd'
    city = 'Carapicuíba'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'
    try:
        # Fazendo a requisição para a API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida
        weather_data = response.json()
        
        # Processando os dados
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'temp_min': round(weather_data['main']['temp_min']),
            'temp_max': round(weather_data['main']['temp_max']),
        }
        return JsonResponse(context)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Erro ao conectar à API'}, status=500)
    except requests.exceptions.HTTPError as errh:
        context = {'error': f"HTTP Error: {errh}"}
    except requests.exceptions.RequestException as e:
        context = {'error': "Erro ao conectar à API"}
    except KeyError:
        context = {'error': "Erro ao processar os dados da API"}

    return render(request, "index.html", context)