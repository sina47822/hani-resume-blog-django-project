(function ($) {
  "use strict";

  /*============= preloader js css =============*/
  var cites = [];
  cites[0] =
    "ما این وبسایت را برای تعامل با خوانندگان و همراهان خود طراحی کرده ایم";
  cites[1] = "اگر به دنبال راه حلی برای کسب و کار خود هستید این فرصت را از دست ندهید";
  cites[2] = "برای رشد و پیشرفت خود می توانید روی من حساب کنید";
  cites[3] = "من میتوانم شما را در بهبود کسب و کارتان همراهی کنم";
  var cite = cites[Math.floor(Math.random() * cites.length)];
  $("#preloader p").text(cite);
  $("#preloader").addClass("loading");

  $(window).on("load", function () {
    setTimeout(function () {
      $("#preloader").fadeOut(500, function () {
        $("#preloader").removeClass("loading");
      });
    }, 500);
  });
})(jQuery);
