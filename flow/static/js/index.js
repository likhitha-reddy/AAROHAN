// eye move with mouse
var balls = document.getElementsByClassName("ball");
document.onmousemove = function() {
  var x = (event.clientX * 100) / window.innerWidth + "%";
  var y = (event.clientY * 100) / window.innerHeight + "%";

  balls[0].style.left = x;
  balls[0].style.top = y;
  balls[0].style.transform = "translate(-" + x + ",-" + y + ")";
};

// events animation
const animateBadge = () => {
  if (window.screen.width > 480) {
    TweenMax.to("#side1", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    TweenMax.to("#side2", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    TweenMax.to("#side3", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    TweenMax.to("#side4", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    TweenMax.to("#side5", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    TweenMax.to("#side6", 1, {
      left: "-30px",
      opacity: 1,
      ease: Power2.easeInOut
    });
    console.log("anim1 done");
  }
};

//social icons color change
const iconChange = () => {
  for (var i = 1; i < 5; i++) {
    var icons = document.getElementById("icn" + i);
    icons.style.color = "white";
  }
};

//social icons color change
const iconChange2 = () => {
  for (var i = 1; i < 5; i++) {
    var icons = document.getElementById("icn" + i);
    icons.style.color = "black";
  }
};
