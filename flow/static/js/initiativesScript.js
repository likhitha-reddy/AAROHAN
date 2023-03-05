const register = document.querySelectorAll(".know");


for (var i = 0; i <register.length; i++) {
    const str1= register[i];
    console.log(str1);
    str1.addEventListener("click",() => {
        const id = str1.getAttribute("value");
        const div=document.getElementById(id);
        div.classList.add("modaldisplay");
    });
}

const closes = document.querySelectorAll(".cross");


for (var i = 0; i <closes.length; i++) {
    const str2= closes[i];
    str2.addEventListener("click",() => {
        const id = str2.getAttribute("value");
        const div=document.getElementById(id);
        div.classList.remove("modaldisplay");
    });
}