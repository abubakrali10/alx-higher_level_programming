$(document).ready(function () {
  $.get({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
