$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'><img src=" + data.result.url_small + "></a>"
          + data.result.js_photo_delete
          // + "<a href='/photos/advertisement/" + data.result.adv_id + "/delete/" + data.result.photo_id + "/'>Удалить</a>"
          +"</td></tr>"
        )
      } else {
         alert('Инвалидные данные')
      }
    }
  });

});
