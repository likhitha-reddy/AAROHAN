// var btn = document.querySelectorAll('.year-text');
var cls = document.querySelectorAll('.clss');
var overlay = document.querySelector('.mars-cont');
var wholecontainer = document.querySelector('.container');
var icon = document.querySelector('.cross-icon');

// for(i=0;i<btn.length;i++){
//   btn[i].addEventListener("click",function(e) {
//     console.log("rishi");
//     overlay.classList.add("overlay-team");
//     wholecontainer.style.display="none";
//   }); 
// }


for(i=0;i<cls.length;i++){
  cls[i].addEventListener("click",function() {
    console.log("sushi");
    overlay.classList.remove("overlay-team");
    wholecontainer.style.display="block";
    icon.style.display="block";
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
  wholecontainer.style.display="none";
  console.log(id);
  team.style="display:block;";
}