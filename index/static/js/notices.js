// static/js/notices.js

let noticeIndex = 0;

function updateNoticeDisplay(data) {
  if (data.notice_image) {
    $(".small-window img").attr("src", data.notice_image);
  } else {
    $(".small-window img").remove();
    $(".small-window").html("<p>Sem imagem disponível</p>");
  }

  $(".textbox h1").html(data.notice_title);
  $(".textbox h3").html(data.notice_category);
  $(".textbox p").html(data.notice_content);
  noticeIndex = (noticeIndex + 1) % data.total_notices;
}

function fetchNoticeData() {
  $.get(home, { notice_index: noticeIndex }, function (data) {
    if (data.error) {
      console.error(data.error);
    } else {
      updateNoticeDisplay(data);
    }
  }).fail(function () {
    console.error("Erro ao obter os dados das notícias.");
  });
}
