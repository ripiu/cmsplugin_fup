$(document).ready(function() {
  $("mark.ripiu-fup").on("mouseover", function() {
    var fupid = $(this).data("id")
    $("#" + fupid + " > .fup-item").addClass("show");
  });
  $("mark").on("mouseout", function() {
    var fupid = $(this).data("id")
    $("#" + fupid + " > .fup-item").removeClass("show");
  });
});
