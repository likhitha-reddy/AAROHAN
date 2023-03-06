const modal = document.querySelector('.modal')
const modalBg = document.querySelector('.modal-bg')

const modalImg = document.querySelector('.modal-image')
const modalHeader = document.querySelector('.modal-header')
const modalTitle = document.querySelector('.modal-title')
const modalDesc = document.querySelector('.modal-desc')
const modalContact = document.querySelector('.modal-contact')
const modalDate = document.querySelector('.modal-date')
const modalVenue = document.querySelector('.modal-venue')
const modalLink = document.querySelector('.modal-btn')

const openBtns = document.querySelectorAll('.card-btn')
openBtns.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    const details = e.target.parentNode
    try {
      modalImg.src = details.attributes._img.nodeValue
      modalHeader.textContent = details.attributes._name.nodeValue
      modalTitle.textContent = details.attributes._id.nodeValue
      modalDesc.textContent = details.attributes._desc.nodeValue
      modalContact.textContent = details.attributes._contact.nodeValue
      modalDate.textContent = details.attributes._date.nodeValue
      modalVenue.textContent = details.attributes._venue.nodeValue
      modalLink.href = details.attributes._link.nodeValue
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