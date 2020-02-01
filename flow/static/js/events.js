var swiper = new Swiper('.swiper-container', {
    loop: true,
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 30,
        stretch: 10,
        depth: 200, //increased from 100 to 200
        modifier: 1,
        slideShadows: true,
    },
    pagination: {
        el: '.swiper-pagination',
    },
});


function showModal() {
    $("#exampleModal").modal('show');
}
$("#exampleModal").on("show.bs.modal", function() {
    $(".modal-dialog").velocity("transition.whirlIn", { duration: 400 });
})

register = data => {
    if (data == 'True') {
        document.getElementById('register_button').style.display = "block";
    } else {
        document.getElementById('register_button').style.display = "none";
    }
}