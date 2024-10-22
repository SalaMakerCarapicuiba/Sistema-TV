$(document).ready(function () {
  // Carregar e atualizar os dados do clima e das notícias
  fetchWeatherData();
  fetchNoticeData();

  // Atualizar o clima e as notícias a cada 30 segundos
  setInterval(fetchWeatherData, 30000);
  setInterval(fetchNoticeData, 30000);

  // Chamar a função para definir a posição inicial do timeline
  updateTimelinePosition();

  // Posicionar os marcadores de horário
  positionHourMarkers();

  setInterval(updateTimelinePosition, 60000);
});
