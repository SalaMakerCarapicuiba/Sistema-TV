function updateTimelinePosition() {
    // Obter a hora atual
    const now = new Date();
    const currentHour = now.getHours();

    // Definir a variável de margem com base na hora atual
    let marginLeftValue;

    if (currentHour >= 7 && currentHour < 8) {
      marginLeftValue = 'var(--q1)';
    } else if (currentHour >= 8 && currentHour < 9) {
      marginLeftValue = 'var(--q2)';
    } else if (currentHour >= 9 && currentHour < 10) {
      marginLeftValue = 'var(--q3)';
    } else if (currentHour >= 10 && currentHour < 11) {
      marginLeftValue = 'var(--q4)';
    } else if (currentHour >= 11 && currentHour < 12) {
      marginLeftValue = 'var(--q5)';
    } else if (currentHour >= 12 && currentHour < 13) {
      marginLeftValue = 'var(--q6)';
    } else if (currentHour >= 13) {
      marginLeftValue = 'var(--q7)';
    } else {
      // Fora do horário entre 7h e 13h
      marginLeftValue = 'var(--q1)';  // Pode-se ajustar para o que faz mais sentido fora deste intervalo
    }

    // Atualizar o estilo do #timeline
    document.getElementById('timeline').style.marginLeft = marginLeftValue;
  }

  // Chamar a função para definir a posição inicial
  updateTimelinePosition();

  // Atualizar a cada 10 minutos
  setInterval(updateTimelinePosition, 10 * 60 * 1000);
