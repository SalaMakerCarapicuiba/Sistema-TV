// static/js/timeline.js

function positionHourMarkers() {
    const startTime = new Date();
    startTime.setHours(13, 50, 0);
    const endTime = new Date();
    endTime.setHours(20, 20, 0);
    const totalDuration = endTime - startTime;

    function getMarkerPosition(hours, minutes) {
      const markerTime = new Date();
      markerTime.setHours(hours, minutes, 0);
      const elapsedTime = markerTime - startTime;
      return (elapsedTime / totalDuration) * 100;
    }

    document.getElementById('hour1').style.left = getMarkerPosition(13, 50) + '%';
    document.getElementById('hour2').style.left = getMarkerPosition(14, 30) + '%';
    document.getElementById('hour3').style.left = getMarkerPosition(15, 0) + '%';
    document.getElementById('hour4').style.left = getMarkerPosition(16, 10) + '%';
    document.getElementById('hour5').style.left = getMarkerPosition(20, 20) + '%';
  }

  function updateTimelinePosition() {
    const startTime = new Date();
    startTime.setHours(13, 50, 0);
    const endTime = new Date();
    endTime.setHours(20, 20, 0);
    const currentTime = new Date();

    if (currentTime >= endTime) {
      currentTime.setHours(13, 50, 0);
    }

    const totalDuration = endTime - startTime;
    const elapsedTime = currentTime - startTime;
    const percentage = (elapsedTime / totalDuration) * 100;

    const timeline = document.getElementById('timeline');
    timeline.style.left = percentage + '%';
  }
