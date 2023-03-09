// var btn = document.querySelectorAll('.year-text');
var cls = document.querySelectorAll('.clss');
var overlay = document.querySelector('.mars-cont');
var wholecontainer = document.querySelector('.container');
var icon = document.querySelector('.cross-icon-teams');
var menu=document.querySelector('.navbarMenu');
var nav=document.querySelector('.nav');
var value=0;
var updown;
const scrollingElement = (document.scrollingElement || document.body);
var social=document.getElementById("icon-down");

// for(i=0;i<btn.length;i++){
//   btn[i].addEventListener("click",function(e) {
//     console.log("rishi");
//     overlay.classList.add("overlay-team");
//     wholecontainer.style.display="none";
//   }); 
// }


for(i=0;i<cls.length;i++){
  cls[i].addEventListener("click",function() {
    overlay.classList.remove("overlay-team");
    nav.classList.remove("nav-team");
    wholecontainer.style.display="block";
    icon.style.display="block";
    menu.style.visibility="visible";
    scrollingElement.scrollTop = updown;
  }); 
}


function ToggleModal(id){
  overlay.classList.add("overlay-team");
  var category = document.querySelectorAll('.category');
  var team=document.getElementById(`${id}`);
  // team.style.display="none";
  for(i=0;i<category.length;i++){
      category[i].style.display="none";
  }
  icon.style.display="none";
  menu.style.visibility="hidden";
  // nav.style.display="none";
  nav.classList.add("nav-team");
  wholecontainer.style.display="none";
  team.style="display:block;";
  updown=value;
}

function  Updown(){
  scrollingElement.scrollTop = 1500;
}
document.addEventListener('scroll',function(){
  value=window.scrollY;
  if(window.scrollY>600){
    social.style="visibility:hidden;";
   }
   else{
    social.style="visibility:visible;";
   }
})