const modal = document.querySelector('.modal')
const modalBg = document.querySelector('.modal-bg')

const modalImg = document.querySelector('.modal-image')
const modalHeader = document.querySelector('.modal-header')
const modalTitle = document.querySelector('.modal-title')
const modalDesc = document.querySelector('.modal-desc')
const modalLink = document.querySelector('.modal-btn')

const openBtns = document.querySelectorAll('.card-btn')
openBtns.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    const details = e.target.parentNode
    try {
      modalImg.src = details.attributes._img.nodeValue
      modalHeader.textContent = details.attributes._name.nodeValue
      modalTitle.textContent = details.attributes._title.nodeValue
      modalDesc.textContent = details.attributes._desc.nodeValue
      if (details.attributes._link.nodeValue)
        modalLink.href = details.attributes._link.nodeValue
      else modalLink.style.display = 'none'
    } catch (err) {}
    modalBg.classList.add('open-modal-bg')
    modal.classList.add('open-modal')
  })
})

modalBg.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-bg')) {
    modalBg.classList.remove('open-modal-bg')
    modal.classList.remove('open-modal')
  }
})
