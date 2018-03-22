$(function() {
    $(".fup > input").on("change", function() {
        if ($(this).prop("checked")) {
            $(".fup > input").not(this).prop("checked", false);
        } 
    });
    $("mark.ripiu-fup > label").on("mouseover", function(e) {
        var radio = $("#" + $(this).attr("for"))
        radio.prop("checked", true);
        radio.trigger("change");
    });
    $("mark.ripiu-fup > label").on("mouseout", function(e) {
        var radio = $("#" + $(this).attr("for"))
        radio.prop("checked", false);
        radio.trigger("change");
    });
});
