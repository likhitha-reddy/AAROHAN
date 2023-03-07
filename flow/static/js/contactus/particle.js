const particle_container  = document.querySelector("#particle-container");
for(var i=0;i<30;i++){
    var particle = document.createElement("div")
    particle.classList.add('particle')
    particle_container.appendChild(particle)
}
