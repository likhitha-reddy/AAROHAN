(function ($) {
  $.fn.timeline = function () {
    var selectors = {
      id: $(this),
      item: $(this).find(".timeline-item"),
      activeClass: "timeline-item--active",
      img: ".timeline__img",
    };
    selectors.item.eq(0).addClass(selectors.activeClass);
    selectors.id.css(
      "background-image",
      "url(" + selectors.item.first().find(selectors.img).attr("src") + ")"
    );
    var itemLength = selectors.item.length;
    $(window).scroll(function () {
      var max, min;
      var pos = $(this).scrollTop();
      selectors.item.each(function (i) {
        min = $(this).offset().top;
        max = $(this).height() + $(this).offset().top;
        var that = $(this);
        if (i == itemLength - 2 && pos > min + $(this).height() / 2) {
          selectors.item.removeClass(selectors.activeClass);
          selectors.id.css(
            "background-image",
            "url(" + selectors.item.last().find(selectors.img).attr("src") + ")"
          );
          selectors.item.last().addClass(selectors.activeClass);
        } else if (pos <= max - 40 && pos >= min) {
          selectors.id.css(
            "background-image",
            "url(" + $(this).find(selectors.img).attr("src") + ")"
          );
          selectors.item.removeClass(selectors.activeClass);
          $(this).addClass(selectors.activeClass);
        }
      });
    });
  };
})(jQuery);

$("#timeline-1").timeline();

var $page = $(".wrapper");
let pos = 0;
$(".menu_toggle").on("click", function () {
  $page.toggleClass("shazam");
  var wrapper = document.getElementById("wrapper");
  wrapper.style.overflow = "hidden";
  document.documentElement.scrollTop = 0;
  pos = document.getElementsByClassName("timeline-item--active")[0].id;
  console.log(pos);
  if(!($page.hasClass("shazam"))){
  setTimeout(function(){ document.getElementById(pos).scrollIntoView();
    var wrapper = document.getElementById("wrapper");
    wrapper.style.overflow = "auto";}, 700);
  }
});
$(".content").on("click", function () {
  // let pos = document.getElementsByClassName("timeline-item--active")[0].id;
  document.getElementById(pos).scrollIntoView();
  $page.removeClass("shazam");
  // var wrapper = document.getElementById("wrapper");
  // wrapper.style.overflow = "auto";
});

$(".content").hover( function () {
  console.log("hi!")
  // let pos = document.getElementsByClassName("timeline-item--active")[0].id;
 
});
