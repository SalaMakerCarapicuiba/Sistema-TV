document.addEventListener('DOMContentLoaded', function () {
  // Função para calcular a posição em percentual de um horário
  function getPositionPercentage(hours, minutes) {
    const startTime = new Date();
    startTime.setHours(13, 50, 0); // Início às 13:50
    const endTime = new Date();
    endTime.setHours(17, 20, 0); // Fim às 20:20 (corrigi o horário para coincidir com o seu intervalo final)
    const totalDuration = endTime - startTime;

    const time = new Date();
    time.setHours(hours, minutes, 0);
    const elapsedTime = time - startTime;

    return (elapsedTime / totalDuration) * 100;
  }

  // Função para ajustar a largura das aulas de acordo com os horários de início e fim
  function adjustClassWidths(classes) {
    const classElements = document.querySelectorAll('.class'); // Seleciona todos os elementos com a classe 'class'

    classes.forEach((classItem, index) => {
      const { startHour, startMinute, endHour, endMinute } = classItem;

      // Verifica se há um elemento correspondente no índice
      if (classElements[index]) {
        // Calcula a posição inicial e a largura da aula
        const startPercentage = getPositionPercentage(startHour, startMinute);
        const endPercentage = getPositionPercentage(endHour, endMinute);
        const widthPercentage = endPercentage - startPercentage;

        // Aplica a margem esquerda e a largura da aula
        const classElement = classElements[index];
        classElement.style.left = `${startPercentage}%`;
        classElement.style.width = `${widthPercentage}%`;
      }
    });
  }

  // Função para calcular a posição dos marcadores de horário
  function positionHourMarkers() {
    const startTime = new Date();
    startTime.setHours(13, 50, 0); // Início às 13:50
    const endTime = new Date();
    endTime.setHours(17, 20, 0); // Fim às 20:20
    const totalDuration = endTime - startTime;

    // Função auxiliar para calcular a posição em percentual de um horário
    function getMarkerPosition(hours, minutes) {
      const markerTime = new Date();
      markerTime.setHours(hours, minutes, 0);
      const elapsedTime = markerTime - startTime;
      return (elapsedTime / totalDuration) * 100;
    }

    // Verifica se os elementos de horário existem antes de ajustar suas posições
    const hour1 = document.getElementById('hour1');
    const hour2 = document.getElementById('hour2');
    const hour3 = document.getElementById('hour3');
    const hour4 = document.getElementById('hour4');
    const hour5 = document.getElementById('hour5');

    if (hour1) hour1.style.left = getMarkerPosition(13, 50) + '%';
    if (hour2) hour2.style.left = getMarkerPosition(14, 30) + '%';
    if (hour3) hour3.style.left = getMarkerPosition(15, 0) + '%';
    if (hour4) hour4.style.left = getMarkerPosition(16, 10) + '%';
    if (hour5) hour5.style.left = getMarkerPosition(17, 20) + '%';
  }

  // Exemplo de uso da função com horários fictícios das aulas
  const classes = [
    { startHour: 13, startMinute: 50, endHour: 15, endMinute: 30 }, // Aula 1
    { startHour: 15, startMinute: 0, endHour: 16, endMinute: 30 },  // Aula 2
    { startHour: 16, startMinute: 0, endHour: 17, endMinute: 20 },  // Aula 3
    { startHour: 14, startMinute: 0, endHour: 15, endMinute: 0 },   // Aula 4
    { startHour: 16, startMinute: 0, endHour: 17, endMinute: 20 },  // Aula 5
  ];

  // Chama a função para ajustar a largura das aulas
  adjustClassWidths(classes);

  // Posiciona os marcadores de horário
  positionHourMarkers();

  // Função para atualizar a posição do timeline
  function updateTimelinePosition() {
    const startTime = new Date();
    startTime.setHours(13, 50, 0); // Início às 13:50
    const endTime = new Date();
    endTime.setHours(17, 20, 0); // Fim às 20:20
    const currentTime = new Date();

    if (currentTime >= endTime || currentTime < startTime) {
      currentTime.setHours(13, 50, 0); // Reinicia para 13:50
    }

    const totalDuration = endTime - startTime;
    const elapsedTime = currentTime - startTime;
    const percentage = (elapsedTime / totalDuration) * 100;

    const timeline = document.getElementById('timeline');
    if (timeline) {
      timeline.style.left = percentage + '%';
    } else {
      console.error('Elemento #timeline não encontrado');
    }
  }

  // Atualiza a posição do timeline
  updateTimelinePosition();

  // Atualiza a cada minuto
  setInterval(updateTimelinePosition, 60000);
});
