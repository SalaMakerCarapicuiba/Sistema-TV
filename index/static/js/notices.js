function updateNoticeDisplay(data) {
  if (data.notice_image) {
    $(".small-window img").attr("src", data.notice_image);
  } else {
    $(".small-window img").remove();
    $(".small-window").html("<p>Sem imagem disponível</p>");
  }
  $(".textbox h3").html(data.notice_category);
  $("#noticeContext").html(data.notice_content);
  noticeIndex = (noticeIndex + 1) % data.total_notices;
}

// Função para buscar dados das notícias
function fetchNoticeData() {
  $.get(home, { notice_index: noticeIndex }, function (data) {
    console.log(data);  // Verifica o retorno
    if (data.error) {
      console.error(data.error);
    } else {
      updateNoticeDisplay(data);
    }
  }).fail(function () {
    console.error("Erro ao obter os dados das notícias.");
  });
}

// Função para atualizar a exibição de recados
function updateRecadoDisplay(data) {
  $(".textbox h1").html(data.recado_title);  // Atualiza o título do recado
  $(".textbox.right p").html(data.recado_message); // Atualiza o conteúdo do recado
  recadoIndex = (recadoIndex + 1) % data.total_recados;
}

// Função para buscar dados dos recados
function fetchRecadoData() {
  $.get(home, { recado_index: recadoIndex }, function (data) {
    console.log(data);  // Verifica o retorno
    if (data.error) {
      console.error(data.error);
    } else {
      updateRecadoDisplay(data);
    }
  }).fail(function () {
    console.error("Erro ao obter os dados dos recados.");
  });
}
