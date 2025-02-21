(function ($) {
  "use strict";
  //*=============menu sticky js =============*//
  var $window = $(window);
  var didScroll,
    lastScrollTop = 0,
    delta = 5,
    $mainNav = $(".sticky-nav").filter(":visible"),
    $body = $("body"),
    $mainNavHeight = $mainNav.outerHeight() + 15,
    scrollTop;

  $window.on("scroll", function () {
    didScroll = true;
    scrollTop = $(this).scrollTop();
  });

  setInterval(function () {
    if (didScroll) {
      if (Math.abs(lastScrollTop - scrollTop) <= delta) {
        return;
      }
      if (scrollTop > lastScrollTop && scrollTop > $mainNavHeight) {
        $mainNav
          .removeClass("fadeInDown")
          .addClass("fadeInUp")
          .css("top", -$mainNavHeight);
        $body.removeClass("remove").addClass("add");
      } else {
        if (scrollTop + $(window).height() < $(document).height()) {
          $mainNav
            .removeClass("fadeInUp")
            .addClass("fadeInDown")
            .css("top", 0)
            .addClass("gap");
          $body.removeClass("add").addClass("remove");
        }
      }
      lastScrollTop = scrollTop;
      didScroll = false;
    }
  }, 200);

  if ($(".sticky-nav").length) {
    $(window).scroll(function () {
      var scroll = $(window).scrollTop();
      if (scroll) {
        $(".sticky-nav").addClass("navbar_fixed");
        $(".sticky-nav-doc .body_fixed").addClass("body_navbar_fixed");
      } else {
        $(".sticky-nav").removeClass("navbar_fixed");
        $(".sticky-nav-doc .body_fixed").removeClass("body_navbar_fixed");
      }
    });
  }

  $(document).ready(function () {
    $(window).scroll(function () {
      if ($(document).scrollTop() > 500) {
        $("body").addClass("test");
      } else {
        $("body").removeClass("test");
      }
    });
  });

  //* Navbar Fixed
  function navbarFixed() {
    if ($(".sticky_nav").length) {
      $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll) {
          $(".sticky_nav").addClass("navbar_fixed");
        } else {
          $(".sticky_nav").removeClass("navbar_fixed");
        }
      });
    }
  }
  navbarFixed();

  /*--------------- mobile dropdown js--------*/

  function mobile_dropdown_menu() {
    $(".menu > li .dropdown-toggle,.menu > li .mobile_dropdown_icon").on(
      "click",
      function () {
        $(this).parent().find("> ul").first().slideToggle(300);
        $(this).parent().siblings().find("> ul").hide(300);
        $(this).toggleClass("active");
        $(this)
          .parent()
          .siblings()
          .find(".mobile_dropdown_icon")
          .removeClass("active");
        return false;
      }
    );
  }
  mobile_dropdown_menu();

  if ($(".marquee").length) {
    var Increment = 1; // Amount to move per tick...
    var LoopDelay = 500 / 30; // How fast ticks happen...
    var Loop;

    function DestroyLoop() {
      clearInterval(Loop);
    }

    function CreateLoop() {
      Loop = setInterval(function () {
        var FirstSlide = $(".marquee .slide:first-child");
        var FirstMargin = parseInt(FirstSlide.css("margin-left")) - Increment;
        FirstSlide.css({ "margin-left": FirstMargin });

        if (Math.abs(FirstMargin) >= FirstSlide.outerWidth()) {
          FirstSlide.css({ "margin-left": 0 });
          FirstSlide.appendTo($(".marquee"));
        }
      }, LoopDelay);
    }

    $(".marquee").on("mouseenter", DestroyLoop);
    $(".marquee").on("mouseleave", CreateLoop);
    CreateLoop();
  }

  // Remove svg.radial-progress .complete inline styling
  $("svg.radial-progress").each(function (index, value) {
    $(this).find($("circle.complete")).removeAttr("style");
  });

  $(window)
    .scroll(function () {
      $("svg.radial-progress").each(function (index, value) {
        // If svg.radial-progress is approximately 25% vertically into the window when scrolling from the top or the bottom
        if (
          $(window).scrollTop() >
            $(this).offset().top - $(window).height() * 0.75 &&
          $(window).scrollTop() <
            $(this).offset().top + $(this).height() - $(window).height() * 0.25
        ) {
          // Get percentage of progress
          var percent = $(value).data("percentage");

          // Get radius of the svg's circle.complete
          var radius = $(this).find($("circle.complete")).attr("r");

          // Get circumference (2πr)
          var circumference = 2 * Math.PI * radius;

          // Get stroke-dashoffset value based on the percentage of the circumference
          var strokeDashOffset =
            circumference - (percent * circumference) / 100;

          // Transition progress for 1.25 seconds
          $(this)
            .find($("circle.complete"))
            .animate({ "stroke-dashoffset": strokeDashOffset }, 1250);
        }
      });
    })
    .trigger("scroll");

  /*---------------------- elements Popup --------------------- */
  $(document).ready(function () {
    $(".divs div").each(function (e) {
      if (e != 0) $(this).hide();
    });

    $(".next").click(function () {
      //$(".list li").addClass("active");
      if (($(".divs div:visible").next().length = !0)) {
        $(".divs div:visible").next().show().prev().hide();
        var activeClass = "." + $(".divs div:visible").attr("class");
        $(".list").find("li").removeClass("active show");
        $(".list").find(activeClass).addClass("active show");
      } else {
        $(".divs div:visible").hide();
        $(".divs div:first").show();
        $(".list").find("li").removeClass("active show");
        $(".list li:first").addClass("active show");
      }
      return false;
    });

    $(".prev").click(function () {
      if (($(".divs div:visible").prev().length = !0)) {
        $(".divs div:visible").prev().show().next().hide();
        var activeClass = "." + $(".divs div:visible").attr("class");
        $(".list").find("li").removeClass("active show");
        $(".list").find(activeClass).addClass("active show");
      } else {
        $(".divs div:visible").hide();
        $(".divs div:last").show();
        $(".list").find("li").removeClass("active show");
        $(".list li:last").addClass("active show");
      }
      return false;
    });
    $(".close_btn").on("click", function () {
      $(".nav.list li").removeClass("active show");
      $(".nav.list li .dropdown-menu").removeClass("show");
      $("body").removeClass("blur");
    });
    $(".nav.list li .img_pointing").on("click", function () {
      $("body").toggleClass("blur");
    });
    var selector, elems, makeActive;

    selector = ".nav.list li";

    elems = document.querySelectorAll(selector);

    makeActive = function () {
      for (var i = 0; i < elems.length; i++)
        elems[i].classList.remove("active");

      this.classList.add("active");
    };

    for (var i = 0; i < elems.length; i++)
      elems[i].addEventListener("mousedown", makeActive);

    if ($(".nav.list li").hasClass("active")) {
      $("body").addClass("blur");
    }
  });

  //popup 2
  function popupGallery() {
    if ($(".img_popup").length) {
      $(".img_popup").each(function () {
        $(".img_popup").magnificPopup({
          type: "image",
          closeOnContentClick: true,
          closeBtnInside: false,
          fixedContentPos: true,
          removalDelay: 300,
          mainClass: "mfp-no-margins mfp-with-zoom",
          image: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1], // Will preload 0 - before current, and 1 after the current image,
          },
        });
      });
    }
  }

  /*--------------- Tab button js--------*/

  $(".next").on("click", function () {
    const nextTabLinkEl = $(".v_menu .active")
      .closest("li")
      .next("li")
      .find("a");
    const nextTab = new bootstrap.Tab(nextTabLinkEl);
    nextTab.show();
  });
  $(".previous").on("click", function () {
    const prevTabLinkEl = $(".v_menu  .active")
      .closest("li")
      .prev("li")
      .find("a");
    const prevTab = new bootstrap.Tab(prevTabLinkEl);
    prevTab.show();
  });

  function Click_menu_hover() {
    if ($(".tab-demo").length) {
      $.fn.tab = function (options) {
        var opts = $.extend({}, $.fn.tab.defaults, options);
        return this.each(function () {
          var obj = $(this);

          $(obj)
            .find(".tabHeader li")
            .on(opts.trigger_event_type, function () {
              $(obj).find(".tabHeader li").removeClass("active");
              $(this).addClass("active");

              $(obj).find(".tabContent .tab-pane").removeClass("active show");
              $(obj)
                .find(".tabContent .tab-pane")
                .eq($(this).index())
                .addClass("active show");
            });
        });
      };
      $.fn.tab.defaults = {
        trigger_event_type: "click", //mouseover | click é»˜è®¤æ˜¯click
      };
    }
  }

  Click_menu_hover();

  function Tab_menu_activator() {
    if ($(".tab-demo").length) {
      $(".tab-demo").tab({
        trigger_event_type: "mouseover",
      });
    }
  }

  Tab_menu_activator();

  // Data table
  function DataTable() {
    if ($("#dtMaterialDesignExample").length) {
      $(document).ready(function () {
        $("#dtMaterialDesignExample").DataTable();
        $("#dtMaterialDesignExample_wrapper")
          .find("label")
          .each(function () {
            $(this).parent().append($(this).children());
          });
        $("#dtMaterialDesignExample_wrapper .dataTables_filter")
          .find("input")
          .each(function () {
            const $this = $(this);
            $this.attr("placeholder", "Search");
            $this.removeClass("form-control-sm");
          });
        $("#dtMaterialDesignExample_wrapper .dataTables_length").addClass(
          "d-flex flex-row"
        );
        $("#dtMaterialDesignExample_wrapper .dataTables_filter").addClass(
          "md-form"
        );
        $("#dtMaterialDesignExample_wrapper select").removeClass(
          "custom-select custom-select-sm form-control form-control-sm"
        );
        $("#dtMaterialDesignExample_wrapper select").addClass("mdb-select");
        $("#dtMaterialDesignExample_wrapper .dataTables_filter")
          .find("label")
          .remove();
      });
    }
  }

  DataTable();

  // === Back to Top Button
  var back_top_btn = $("#back-to-top");

  $(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
      back_top_btn.addClass("show");
    } else {
      back_top_btn.removeClass("show");
    }
  });

  back_top_btn.on("click", function (e) {
    e.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, "300");
  });

  /*------------ Cookie functions and color js ------------*/
  function createCookie(name, value, days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
  }

  function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(";");
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == " ") c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  function eraseCookie(name) {
    createCookie(name, "", -1);
  }

  var prefersDark =
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;
  var selectedNightTheme = readCookie("body_dark");

  if (
    selectedNightTheme == "true" ||
    (selectedNightTheme === null && prefersDark)
  ) {
    applyNight();
    $(".dark_mode_switcher").prop("checked", true);
  } else {
    applyDay();
    $(".dark_mode_switcher").prop("checked", false);
  }

  // Dark Mode Switcher
  function applyNight() {
    if ($(".js-darkmode-btn .ball").length) {
      $(".js-darkmode-btn .ball").css("left", "39px");
    }
    $("body").addClass("body_dark");
  }

  function applyDay() {
    if ($(".js-darkmode-btn .ball").length) {
      $(".js-darkmode-btn .ball").css("left", "3px");
    }
    $("body").removeClass("body_dark");
  }

  $(".dark_mode_switcher").change(function () {
    if ($(this).is(":checked")) {
      applyNight();

      createCookie("body_dark", true, 999);
    } else {
      applyDay();
      createCookie("body_dark", false, 999);
    }
  });

  // Dark Mode Switcher 2
  function applyNight2() {
    if ($(".js-darkmode-btn2 .ball").length) {
      $(".js-darkmode-btn2 .ball").css("left", "52px");
    }
    $("body").addClass("body_dark");
  }

  function applyDay2() {
    if ($(".js-darkmode-btn2 .ball").length) {
      $(".js-darkmode-btn2 .ball").css("left", "0");
    }
    $("body").removeClass("body_dark");
  }

  $(".dark_mode_switcher").change(function () {
    if ($(this).is(":checked")) {
      applyNight2();

      createCookie("body_dark", true, 999);
    } else {
      applyDay2();
      createCookie("body_dark", false, 999);
    }
  });

  $(".mobile_menu_btn").on("click", function () {
    $(".side_menu").addClass("menu-opened");
    $("body").removeClass("menu-is-closed").addClass("menu-is-opened");
  });
  $(".close_nav,.click_capture").on("click", function (e) {
    if ($(".side_menu").hasClass("menu-opened")) {
      $(".side_menu").removeClass("menu-opened");
      $("body").removeClass("menu-is-opened");
    } else {
      $(".side_menu").addClass("menu-opened");
    }
  });

  $(window).on("load", function () {
    if ($(".scroll").length) {
      $(".scroll").mCustomScrollbar({
        mouseWheelPixels: 50,
        scrollInertia: 0,
      });
    }
  });

  if ($(".chapter-tab").length) {
    var triggerChapterTabList = [].slice.call(
      document.querySelectorAll(".chapter-tab .nav-link")
    );
    triggerChapterTabList.forEach(function (triggerEl) {
      var tabTrigger = new bootstrap.Tab(triggerEl);

      triggerEl.addEventListener("click", function (event) {
        $(".chapter-tab").find(".active").removeClass("active");
        event.preventDefault();
        tabTrigger.show();
      });
    });
  }

  $(".social_share_btn").click(function () {
    $(this).find(".social_share_list").toggleClass("open");
  });

  if ($(".branding-slider").length) {
    $(".branding-slider").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: false,
      speed: 5000,
      pauseOnHover: false,

      cssEase: "linear",
      autoplaySpeed: 10,
      responsive: [
        {
          breakpoint: 765,
          settings: {
            slidesToShow: 2,
          },
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
          },
        },
      ],
    });
  }

  if ($(".branding-reverse-slider").length) {
    $(".branding-reverse-slider").slick({
      autoplay: true,
      infinite: true,
      rtl: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: false,
      speed: 5000,
      pauseOnHover: false,
      cssEase: "linear",
      autoplaySpeed: 10,
      responsive: [
        {
          breakpoint: 765,
          settings: {
            slidesToShow: 2,
          },
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
          },
        },
      ],
    });
  }

  if ($(".single-members-slider").length) {
    $(".single-members-slider").slick({
      autoplay: false,
      infinite: false,
      slidesToShow: 7,
      slidesToScroll: 1,
      dots: false,
      arrows: true,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 5,
          },
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 4,
          },
        },
        {
          breakpoint: 500,
          settings: {
            slidesToShow: 3,
          },
        },
      ],
    });
  }

  if ($(".single-members-slider").length) {
    $(".single-members-slider .slick-track").addClass("nav");
  }

  if ($(".proccess-banner-slider").length) {
    $(".proccess-banner-slider").slick({
      autoplay: true,
      infinite: false,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      arrows: false,
      autoplaySpeed: 5000,
      pauseOnHover: false,
    });

    $(".proccess-banner-slider .slick-dots li").each(function (index) {
      var progress = index + 1;
      $(this).html(`<svg class="progress-svg" width="40" height="40">
      <g transform="translate(20,20)">
        <circle class="circle-go" r="19" cx="0" cy="0"></circle>
        <text class="circle-tx" x="0" y="2" alignment-baseline="middle" stroke-width="0" text-anchor="middle">${progress}</text>
      </g>
      </svg>`);
    });
  }

  if ($(".trip-post .slider-photo").length) {
    $(".trip-post .slider-photo").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: false,
      arrows: true,
      prevArrow:
        '<button type="button" class="nav-arrow prev"><i class="fas fa-chevron-left"></i></button>',
      nextArrow:
        '<button type="button" class="nav-arrow"><i class="fas fa-chevron-right"></i></button>',
    });
  }

  if ($(".instagram-feed-three").length) {
    $(".instagram-feed-three").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 8,
      slidesToScroll: 1,
      dots: false,
      arrows: false,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 5,
          },
        },
        {
          breakpoint: 630,
          settings: {
            slidesToShow: 4,
          },
        },
        {
          breakpoint: 500,
          settings: {
            slidesToShow: 3,
          },
        },
      ],
    });
  }

  if ($(".testimonial-slider").length) {
    $(".testimonial-slider").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: false,
      arrows: true,
      nextArrow: '<div class="next"><span class="arrow"></span></div>',
    });

    var getSlickItem = $(".testimonial-slider").slick("getSlick");
    if (getSlickItem.currentSlide < 9) {
      $(".current_slide").text(`0${getSlickItem.currentSlide + 1}`);
    } else {
      $(".current_slide").text(getSlickItem.currentSlide + 1);
    }
    if (getSlickItem.getDotCount() < 9) {
      $(".total_slide").text(`0${getSlickItem.getDotCount() + 1}`);
    } else {
      $(".total_slide").text(getSlickItem.getDotCount() + 1);
    }

    $(".testimonial-slider").on(
      "beforeChange",
      function (event, slick, currentSlide, nextSlide) {
        if (nextSlide < 9) {
          $(".current_slide").text(`0${nextSlide + 1}`);
        } else {
          $(".current_slide").text(nextSlide + 1);
        }
      }
    );
  }

  if ($(".testimonial-slide-3").length) {
    $(".testimonial-slide-3").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: false,
      centerMode: true,
      centerPadding: 0,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 1,
          },
        },
      ],
    });
  }

  if ($(".testimonial-slider-6").length) {
    $(".testimonial-slider-6").slick({
      autoplay: true,
      infinite: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      arrows: false,
    });
  }

  if ($(".portfolio-details-gallery-slider").length) {
    $(".portfolio-details-gallery-slider").slick({
      autoplay: false,
      infinite: false,
      slidesToShow: 4,
      slidesToScroll: 1,
      dots: false,
      arrows: true,
      prevArrow:
        '<button type="button" class="nav-arrow prev"><i class="fas fa-chevron-left"></i></button>',
      nextArrow:
        '<button type="button" class="nav-arrow next"><i class="fas fa-chevron-right"></i></button>',
      responsive: [
        {
          breakpoint: 776,
          settings: {
            slidesToShow: 3,
          },
        },
        {
          breakpoint: 565,
          settings: {
            slidesToShow: 2,
          },
        },
      ],
    });
  }

  //mixit up
  if ($("#team-filter").length) {
    var containerEl = document.querySelector("#team-filter");
    var mixer = mixitup(containerEl);
  }

  //Wow js
  new WOW().init();

  //before after js
  if ($("#beforeAfter").length > 0) {
    $("#beforeAfter").beforeAfter({
      movable: true,
      clickMove: true,
      position: 49.65,
      separatorColor: "#fafafa",
      bulletColor: "#fff",
    });
  }

  //fullpage slider
  if ($("#fullpage").length > 0) {
    $("#fullpage").fullpage({
      navigation: true,
      navigationPosition: "right",
      autoScrolling: true,
      css3: true,
      verticalCentered: true,
      scrollingSpeed: 1000,
      afterResponsive: function (isResponsive) {},
    });
    $("#moveDown").click(function () {
      $.fn.fullpage.moveSectionDown();
    });
  }
  if ($("#work_history").length > 0) {
    $("#work_history").fullpage({
      navigation: true,
      navigationPosition: "right",
      autoScrolling: true,
      css3: true,
      verticalCentered: true,
      scrollingSpeed: 1000,
      responsiveWidth: 992,
      anchors: [
        "work_slide_one",
        "work_slide_two",
        "work_slide_three",
        "work_slide_four",
        "work_slide_five",
        "work_slide_six",
        "work_slide_seven",
      ],
    });
    $("#moveDown").click(function () {
      $.fn.fullpage.moveSectionDown();
    });
  }

  if ($("#wave").length > 0) {
    $("#wave").fullpage({
      navigation: true,
      navigationPosition: "right",
      autoScrolling: true,
      scrollBar: false,
      scrollOverflow: true,
      animateAnchor: true,
      css3: true,
      verticalCentered: true,
      scrollingSpeed: 1000,
      afterResponsive: function (isResponsive) {},
    });
    $("#moveDown").click(function () {
      $.fn.fullpage.moveSectionDown();
    });
  }

  //flact picker(calender)
  if ($("#basicDate").length > 0) {
    $("#basicDate").flatpickr({
      enableTime: false,
      dateFormat: "F, d Y",
    });
  }
  if ($("#availability").length > 0) {
    $("#availability").flatpickr({
      enableTime: false,
      dateFormat: "F, d Y",
    });
  }
  if ($("#filterGalleryFrom").length > 0) {
    $("#filterGalleryFrom").flatpickr({
      enableTime: false,
      dateFormat: "d-m-Y",
    });
  }
  if ($("#filterGalleryTo").length > 0) {
    $("#filterGalleryTo").flatpickr({
      enableTime: false,
      dateFormat: "d-m-Y",
    });
  }

  //nice slelect
  if ($(".select").length) {
    $(".select").niceSelect();
  }

  //counter up js
  if ($(".counter").length) {
    $(".counter").counterUp({
      delay: 10,
      time: 1000,
    });
  }

  // video popup
  if ($(".popup-youtube").length) {
    $(".popup-youtube").magnificPopup({
      type: "iframe",
      mainClass: "mfp-fade",
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
    });
  }

  popupGallery();

  //swiper sliders
  if ($(".skill-slider").length) {
    var swiper = new Swiper(".skill-slider", {
      loop: true,
      slidesPerView: 2,
      spaceBetween: 20,
      keyboard: {
        enabled: true,
      },
      freeMode: true,
      watchSlidesProgress: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 4,
        },
      },
    });
  }

  if ($(".logo-slide-4").length) {
    var swiper2 = new Swiper(".logo-slide-4", {
      spaceBetween: 10,
      slidesPerView: 1,
      loop: true,
      watchSlidesProgress: true,
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 5,
        },
      },
    });
  }

  if ($(".testimonial-slide-4").length) {
    var swiper3 = new Swiper(".testimonial-slide-4", {
      spaceBetween: 10,
      loop: true,
      navigation: false,
      thumbs: {
        swiper: swiper2,
      },

      breakpoints: {
        768: {
          navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          },
        },
      },
    });
  }

  if ($(".company-case-logo-slider-1").length) {
    var companyCaselogoSlide1 = new Swiper(".company-case-logo-slider-1", {
      spaceBetween: 24,
      slidesPerView: 1,
      loop: false,
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
      },
    });
  }
  if ($(".company-case-logo-slider-2").length) {
    var companyCaselogoSlide2 = new Swiper(".company-case-logo-slider-2", {
      spaceBetween: 24,
      slidesPerView: 1,
      loop: false,
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
      },
    });
  }
  if ($(".company-case-logo-slider-3").length) {
    var companyCaselogoSlide3 = new Swiper(".company-case-logo-slider-3", {
      spaceBetween: 24,
      slidesPerView: 1,
      loop: false,
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
      },
    });
  }

  if ($(".company-case-slider-1").length) {
    var companyCaseSlider = new Swiper(".company-case-slider-1", {
      spaceBetween: 10,
      loop: true,
      navigation: false,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      thumbs: {
        swiper: companyCaselogoSlide1,
      },

      effect: "creative",
      creativeEffect: {
        prev: {
          shadow: true,
          translate: [0, 0, -400],
        },
        next: {
          translate: ["100%", 0, 0],
        },
      },
    });
  }

  if ($(".company-case-slider-2").length) {
    var companyCaseSlider = new Swiper(".company-case-slider-2", {
      spaceBetween: 10,
      loop: true,
      navigation: false,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      thumbs: {
        swiper: companyCaselogoSlide2,
      },
      effect: "creative",
      creativeEffect: {
        prev: {
          shadow: true,
          translate: [0, 0, -400],
        },
        next: {
          translate: ["100%", 0, 0],
        },
      },
    });
  }

  if ($(".company-case-slider-3").length) {
    var companyCaseSlider = new Swiper(".company-case-slider-3", {
      spaceBetween: 10,
      loop: true,
      navigation: false,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      thumbs: {
        swiper: companyCaselogoSlide3,
      },
      effect: "creative",
      creativeEffect: {
        prev: {
          shadow: true,
          translate: [0, 0, -400],
        },
        next: {
          translate: ["100%", 0, 0],
        },
      },
    });
  }

  // Homepage 6 Testimonial Section
  if ($(".testimonial-slide-5").length) {
    var swiper4 = new Swiper(".testimonial-slide-5", {
      spaceBetween: 10,
      loop: true,
      navigation: false,

      breakpoints: {
        768: {
          navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          },
        },
      },
    });
  }

  // Homepage 6 Testimonial Section
  if ($(".testimonial-slider-active").length) {
    var swiper5 = new Swiper(".testimonial-slider-active", {
      slidesPerView: 1,
      spaceBetween: 24,
      grabCursor: true,
      loop: true,
      speed: 500,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        576: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 4,
        },
      },
    });
  }

  // Homepage 7 Banner Slider
  if ($(".banner-thumbs").length) {
    var bannerThumbs = new Swiper(".banner-thumbs", {
      slidesPerView: 1,
      loop: true,
      centeredSlides: true,
      watchSlidesProgress: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 5,
        },
      },
    });
  }

  if ($(".banner-main").length) {
    var bannerMain = new Swiper(".banner-main", {
      loop: true,
      navigation: false,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      thumbs: {
        swiper: bannerThumbs,
      },

      breakpoints: {
        768: {
          navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          },
        },
      },
    });
  }

  if ($(".instagram-feed-active").length) {
    // Homepage 7 Portfolio Slider
    var portfolio = new Swiper(".instagram-feed-active", {
      slidesPerView: 1,
      spaceBetween: 24,
      loop: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 4,
        },
        1200: {
          slidesPerView: 5,
        },
      },
    });
  }

  if ($(".instagram-feed-two").length) {
    var instagramTwo = new Swiper(".instagram-feed-two", {
      slidesPerView: 1,
      spaceBetween: 10,
      loop: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        330: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 5,
        },
        1200: {
          slidesPerView: 8,
        },
      },
    });
  }

  if ($(".case-study-swiper-init").length) {
    var case_study_swiper = new Swiper(".case-study-swiper-init", {
      slidesPerView: 1,
      spaceBetween: 10,
      loop: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
  }
  if ($(".case-study-main-swiper").length) {
    var case_study_main_swiper = new Swiper(".case-study-main-swiper", {
      slidesPerView: 1,
      direction: "vertical",
    });
  }
  if ($(".case-study-sidebar-swiper").length) {
    var case_study_sidebar_swiper = new Swiper(".case-study-sidebar-swiper", {
      mousewheel: true,
      centeredSlides: true,
      direction: "vertical",
      slidesPerView: "auto",
      thumbs: {
        swiper: case_study_main_swiper,
      },
    });
  }

  if ($(".testimonial-slider-inner").length) {
    var Testimonial = new Swiper(".testimonial-slider-inner", {
      slidesPerView: 1,
      spaceBetween: 10,
      // speed: 500,
      // effect: 'fade',
      loop: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
  }

  // Homepage 7 Banner Slider
  if ($(".portfolio-carousel-thumbs").length) {
    var portCarouselThumb = new Swiper(".portfolio-carousel-thumbs", {
      slidesPerView: 1,
      loop: true,
      spaceBetween: 12,
      breakpoints: {
        300: {
          slidesPerView: 3,
        },
        480: {
          slidesPerView: 4,
        },
        768: {
          slidesPerView: 6,
        },
        992: {
          slidesPerView: 8,
        },
      },
    });
  }

  if ($(".portfolio-carousel-slider").length) {
    var portCarousel = new Swiper(".portfolio-carousel-slider", {
      loop: true,
      navigation: {
        nextEl: ".portfolio-carousel-thumbnails .swiper-button-next",
        prevEl: ".portfolio-carousel-thumbnails .swiper-button-prev",
      },
      spaceBetween: 12,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      thumbs: {
        swiper: portCarouselThumb,
      },
    });
  }

  //parallax js

  if ($(".banner_animation_01").length > 0) {
    $(".banner_animation_01").parallax({
      scalarX: 10.0,
      scalarY: 0.0,
    });
  }
  if ($(".banner_animation_02").length > 0) {
    $(".banner_animation_02").parallax({
      scalarX: 10.0,
      scalarY: 4.0,
    });
  }
  if ($(".banner_animation_03").length > 0) {
    $(".banner_animation_03").parallax({
      scalarX: 7.0,
      scalarY: 10.0,
    });
  }
  if ($("#banner_wave").length > 0) {
    var myWave = $("#banner_wave").wavify({
      height: 100,
      bones: 5,
      amplitude: 110,
      color: "rgba(255, 255, 255, .05)",
      speed: 0.4,
    });
  }

  if ($(".scroller").length > 0) {
    gsap.registerPlugin(ScrollTrigger);
    let bodyScrollBar = Scrollbar.init(document.body, {
      damping: 0.1,
      delegateTo: document,
    });
    ScrollTrigger.scrollerProxy(".scroller", {
      scrollTop(value) {
        if (arguments.length) {
          bodyScrollBar.scrollTop = value;
        }
        return bodyScrollBar.scrollTop;
      },
    });

    bodyScrollBar.addListener(ScrollTrigger.update);

    gsap.set(".panel", { zIndex: (i, target, targets) => targets.length - i });

    var images = gsap.utils.toArray(".panel:not(.purple)");

    images.forEach((image, i) => {
      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: "section.black",
          scroller: ".scroller",
          start: () => "top -" + window.innerHeight * (i + 0.5),
          end: () => "+=" + window.innerHeight,
          scrub: true,
          toggleActions: "play none reverse none",
          invalidateOnRefresh: true,
        },
      });

      tl.to(image, { height: 0 });
    });

    gsap.set(".panel-text", {
      zIndex: (i, target, targets) => targets.length - i,
    });

    var texts = gsap.utils.toArray(".panel-text");

    texts.forEach((text, i) => {
      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: "section.black",
          scroller: ".scroller",
          start: () => "top -" + window.innerHeight * (i + 0.5),
          end: () => "+=" + window.innerHeight,
          scrub: true,
          toggleActions: "play none reverse none",
          invalidateOnRefresh: true,
        },
      });

      tl.to(text, { duration: 0.33, opacity: 1, y: "5%" }).to(
        text,
        { duration: 0.33, opacity: 0, y: "0%" },
        0.66
      );
    });

    ScrollTrigger.create({
      trigger: "section.black",
      scroller: ".scroller",
      scrub: true,
      markers: false,
      pin: true,
      start: () => "top +" + 160,
      end: () => "+=" + (images.length + 1) * window.innerHeight,
      invalidateOnRefresh: true,
    });
  }

  if ($("[data-scroll-container]").length) {
    var loco_scroll = new LocomotiveScroll({
      el: document.querySelector("[data-scroll-container]"),
      smooth: true,
    });
  }

  // Home1 Video Popup
  if ($(".btn-circle .text p").length) {
    const text = document.querySelector(".btn-circle .text p");

    text.innerHTML = text.innerText
      .split("")
      .map(
        (char, i) =>
          `<span style="transform:rotate(${i * 9.5}deg)">${char}</span>`
      )
      .join("");
  }
})(jQuery);

var tpj = jQuery;
if (window.RS_MODULES === undefined) window.RS_MODULES = {};
if (RS_MODULES.modules === undefined) RS_MODULES.modules = {};
RS_MODULES.modules["showcase"] = {
  once:
    RS_MODULES.modules["showcase"] !== undefined
      ? RS_MODULES.modules["showcase"].once
      : undefined,
  init: function () {
    window.revapi16 =
      window.revapi16 === undefined ||
      window.revapi16 === null ||
      window.revapi16.length === 0
        ? document.getElementById("showcase")
        : window.revapi16;
    if (
      window.revapi16 === null ||
      window.revapi16 === undefined ||
      window.revapi16.length == 0
    ) {
      window.revapi16initTry =
        window.revapi16initTry === undefined ? 0 : window.revapi16initTry + 1;
      if (window.revapi16initTry < 20)
        requestAnimationFrame(function () {
          RS_MODULES.modules["showcase"].init();
        });
      return;
    }
    window.revapi16 = jQuery(window.revapi16);
    if (window.revapi16.revolution == undefined) {
      revslider_showDoubleJqueryError("showcase");
      return;
    }
    revapi16.revolutionInit({
      revapi: "revapi16",
      DPR: "dpr",
      sliderLayout: "fullscreen",
      visibilityLevels: "1240,1240,1240,480",
      gridwidth: "1140,1140,1140,480",
      gridheight: "900,900,900,800",
      spinner: "spinner7",
      perspective: 600,
      perspectiveType: "local",
      spinnerclr: "#ff355b",
      editorheight: "900,768,960,800",
      responsiveLevels: "1240,1240,1240,480",
      ajaxUrl: "http://slider-revolution.local/wp-admin/admin-ajax.php",
      progressBar: { disableProgressBar: true },
      navigation: {
        onHoverStop: false,
      },
      sbtimeline: {
        set: true,
        speed: "0ms",
        fixed: true,
        fixStart: "1500ms",
        fixEnd: "3100ms",
      },
      viewPort: {
        global: false,
        globalDist: "-200px",
        enable: true,
      },
      fallbacks: {
        allowHTML5AutoPlayOnAndroid: true,
      },
    });
  },
}; // End of RevInitScript
if (window.RS_MODULES.checkMinimal !== undefined) {
  window.RS_MODULES.checkMinimal();
}

var tpj = jQuery;
if (window.RS_MODULES === undefined) window.RS_MODULES = {};
if (RS_MODULES.modules === undefined) RS_MODULES.modules = {};
RS_MODULES.modules["portfolio"] = {
  once:
    RS_MODULES.modules["portfolio"] !== undefined
      ? RS_MODULES.modules["portfolio"].once
      : undefined,
  init: function () {
    window.revapi9 =
      window.revapi9 === undefined ||
      window.revapi9 === null ||
      window.revapi9.length === 0
        ? document.getElementById("portfolio")
        : window.revapi9;
    if (
      window.revapi9 === null ||
      window.revapi9 === undefined ||
      window.revapi9.length == 0
    ) {
      window.revapi9initTry =
        window.revapi9initTry === undefined ? 0 : window.revapi9initTry + 1;
      if (window.revapi9initTry < 20)
        requestAnimationFrame(function () {
          RS_MODULES.modules["portfolio"].init();
        });
      return;
    }
    window.revapi9 = jQuery(window.revapi9);
    if (window.revapi9.revolution == undefined) {
      revslider_showDoubleJqueryError("portfolio");
      return;
    }
    revapi9.revolutionInit({
      revapi: "revapi9",
      sliderType: "carousel",
      DPR: "dpr",
      sliderLayout: "fullwidth",
      visibilityLevels: "1240,1240,1240,480",
      gridwidth: "1140,1140,1140,480",
      gridheight: "1000,1000,1000,1000",
      spinner: "spinner7",
      perspective: 600,
      perspectiveType: "local",
      spinnerclr: "#ff355b",
      editorheight: "1000,768,960,1000",
      responsiveLevels: "1240,1240,1240,480",
      stopAtSlide: 1,
      stopAfterLoops: 0,
      stopLoop: true,
      ajaxUrl: "http://slider-revolution.local/wp-admin/admin-ajax.php",
      carousel: {
        speed: "2000ms",
        showLayersAllTime: "all",
        maxVisibleItems: 5,
      },
      progressBar: { disableProgressBar: true },
      navigation: {
        // wheelCallDelay: 1000,
        onHoverStop: false,
        touch: {
          touchenabled: false,
          desktopCarousel: false,
        },
        bullets: {
          enable: true,
          tmp: "",
          style: "light-bars",
          hide_onmobile: true,
          hide_under: "600px",
          h_align: "right",
          h_offset: 80,
          v_offset: 100,
          container: "layergrid",
        },
      },
      viewPort: {
        global: false,
        globalDist: "-200px",
        enable: true,
      },
      fallbacks: {
        allowHTML5AutoPlayOnAndroid: true,
      },
    });
  },
}; // End of RevInitScript
if (window.RS_MODULES.checkMinimal !== undefined) {
  window.RS_MODULES.checkMinimal();
}
