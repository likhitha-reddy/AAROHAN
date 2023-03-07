document.onmousemove = function (e) {
  var x = e.clientX;
  var y = e.clientY;
  document.getElementsByClassName("parallax-scene")[0].style.marginLeft =
    0.1 * x + "px";
  document.getElementsByClassName("parallax-scene")[0].style.marginTop =
    -0.1 * y + "px";
};

//ONLOAD
$(function () {
  //DECLARE GLOBAL VARIABLE FOR USE IN HANDLERS
  var orig, sib;
  var runs = 0;
  var charSet = "ABOUT US";

  //RUN JS WHEN 'DISTORT' IS HOVERED
  $(".distort").hover(
    function () {
      var curr = $(this);
      orig = $(this).text();
      sib = setInterval(function () {
        distortText(curr);
      }, 100);
    },
    function () {
      //RESET THE ORIGINAL TEXT
      clearInterval(sib);
      $(this).text(orig);
    }
  );

  function distortText(i) {
    //MAINTAINS SOME READABILITY IN THE TEXT BY ONLY ALLOWING 3 CHARACTERS TO BE DISTORTED
    if (runs >= 2) {
      runs = 0;
      i.text(orig);
      return;
    }
    //GET EACH INDIVIDUAL CHARACTER
    var chars = i.text().split("");
    //GET A RANDOM CHARACTER FROM THE TEXT
    var rand = Math.floor(Math.random() * chars.length);
    //GET A RANDOM REPLACEMENT CHARACTER
    var randRep = Math.floor(Math.random() * charSet.length);
    //CHECK TO MAKE SURE THAT THE NEW CHARACTER IS DIFFERENT FROM THE OLD
    if (chars[rand] != charSet[randRep] && chars[rand] != " ") {
      chars[rand] = charSet[randRep];
    } else {
      distortText(i);
    }
    //UPDATE TEXT
    i.text(chars.join(""));
    runs += 1;
  }
});
