// Função para calcular a posição dos marcadores de horário
function positionHourMarkers() {
  const startTime = new Date();
  startTime.setHours(13, 50, 0); // Início às 13:50
  const endTime = new Date();
  endTime.setHours(20, 20, 0); // Fim às 20:20
  const totalDuration = endTime - startTime;

  // Função auxiliar para calcular a posição em percentual de um horário
  function getMarkerPosition(hours, minutes) {
      const markerTime = new Date();
      markerTime.setHours(hours, minutes, 0);
      const elapsedTime = markerTime - startTime;
      return (elapsedTime / totalDuration) * 100;
  }

  // Posiciona cada marcador de horário na barra de acordo com seu horário relativo
  document.getElementById('hour1').style.left = getMarkerPosition(13, 50) + '%';
  document.getElementById('hour2').style.left = getMarkerPosition(14, 30) + '%';
  document.getElementById('hour3').style.left = getMarkerPosition(15, 0) + '%';
  document.getElementById('hour4').style.left = getMarkerPosition(16, 10) + '%';
  document.getElementById('hour5').style.left = getMarkerPosition(20, 20) + '%';
}

// Função para atualizar a posição da timeline de acordo com o horário atual
function updateTimelinePosition() {
  const startTime = new Date();
  startTime.setHours(13, 50, 0); // Início às 13:50
  const endTime = new Date();
  endTime.setHours(20, 20, 0); // Fim às 20:20
  const currentTime = new Date();

  if (currentTime >= endTime || currentTime < startTime) {
      currentTime.setHours(13, 50, 0); // Reinicia para 13:50
  }

  const totalDuration = endTime - startTime;
  const elapsedTime = currentTime - startTime;
  const percentage = (elapsedTime / totalDuration) * 100;

  const timeline = document.getElementById('timeline');
  timeline.style.left = percentage + '%';
}
