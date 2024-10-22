// static/js/weather.js

const weatherIconMap = {
    'céu limpo': 'sun-fill.svg',
    'algumas nuvens': 'cloud-fill.svg',
    'nublado': 'cloud-fill.svg',
    'chuva leve': 'cloud-rain-fill.svg',
    'chuva moderada': 'cloud-rain-fill.svg',
    'trovoada': 'cloud-lightning-fill.svg',
    'garoa': 'umbrella-simple-fill.svg',
  };

  function getWeatherIcon(description = '') {
    return `${icons}${weatherIconMap[description.toLowerCase()] || 'sun-fill.svg'}`;
  }

  function updateWeatherDisplay(data) {
    $("#today-temp").html(`${data.temp_min}°/${data.temp_max}°`);
    $("#today-icon").attr("src", getWeatherIcon(data.description));

    if (data.temp_min_tomorrow && data.temp_max_tomorrow) {
      $("#tomorrow-temp").html(`${data.temp_min_tomorrow}°/${data.temp_max_tomorrow}°`);
      $("#tomorrow-icon").attr("src", getWeatherIcon(data.description_tomorrow));
    } else {
      $("#tomorrow-temp").html("Dados indisponíveis");
    }

    if (data.agora) {
      const horaMinutos = new Date(data.agora).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      $("#time").html(horaMinutos);
    } else {
      $("#time").html("Horário indisponível");
    }
  }

  function fetchWeatherData() {
    $.get(home, function (data) {
      if (data.error) {
        console.error(data.error);
      } else {
        updateWeatherDisplay(data);
      }
    }).fail(function (xhr, status, error) {
      console.error("Erro ao obter dados da API:", status, error);
    });
  }
