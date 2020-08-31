const buttonLogout = document.getElementById('buttonLogout')
const logoutModal = document.querySelector('.BottomSheet')
const logoutCancelButton = logoutModal.querySelector('#logoutCancel')
const logoutConfirmButton = logoutModal.querySelector('#logoutConfirm')

addEventListener('load', () => {
	logoutModal.style.transition = 'all 0.15s linear'
})

buttonLogout.addEventListener('click', () => {
	logoutModal.classList.remove('modal-hidden')
})

logoutCancelButton.addEventListener('click', () => {
	logoutModal.classList.add('modal-hidden')
})

logoutConfirmButton.addEventListener('click', () => {
	window.location.href = '/logout'
})
