
$(".Symptoms").click(function () {
  $("#myModalnote").css('display', 'block');
  $("#ok").click(function () {
    $("#myModalnote").css('display', 'none');
  });
})