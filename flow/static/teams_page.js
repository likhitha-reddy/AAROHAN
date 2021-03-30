var $page = $('.wrapper')
let pos = 0
$('.menu_toggle').on('click', function () {
  $page.toggleClass('shazam')
  var wrapper = document.getElementById('wrapper')
  wrapper.style.overflow = 'hidden'

  // if (!$page.hasClass('shazam')) {
  //   document.getElementsByClassName('content')[0].style.backgroundSize = '450%'
  //   setTimeout(() => {
  //     document.getElementsByClassName('content')[0].style.backgroundSize =
  //       'cover'
  //   }, 700)
  // }
})
