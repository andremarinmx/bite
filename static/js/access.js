const buttonShowLogin = document.getElementById('buttonShowLogin')
const buttonShowRegister = document.getElementById('buttonShowRegister')
const buttonLogin = document.getElementById('buttonLogin')
const buttonRegister = document.getElementById('buttonRegister')

const loginError = document.getElementById('loginError')
const registerError = document.getElementById('registerError')

const hideError = (event) => {
	event.target.classList.add('display-none')
}
loginError.addEventListener('click', hideError)
registerError.addEventListener('click', hideError)

buttonShowLogin.addEventListener('click', () => {
	const forms = document.querySelectorAll('.Form')

	forms[0].classList.remove('display-none')
	forms[1].classList.add('display-none')
})

buttonShowRegister.addEventListener('click', () => {
	const forms = document.querySelectorAll('.Form')

	forms[0].classList.add('display-none')
	forms[1].classList.remove('display-none')
})

buttonLogin.addEventListener('click', async () => {
	const email = document.getElementById('loginEmail')
	const password = document.getElementById('loginPassword')

	const emailRegex = /^[A-Za-z0-9_\-]+(\.[A-Za-z0-9_\-]+)*@([A-Za-z0-9_\-]+\.)+[a-z]{2,5}$/
	const passwordRegex = /.{4,}/

	if (!emailRegex.test(email.value.trim()) || !passwordRegex.test(password.value)) {
		loginError.textContent = 'El formato del correo o la contraseña no es válido'
		loginError.classList.remove('display-none')

		return
	}

	const response = await fetch('/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			email: email.value.trim(),
			password: password.value
		})
	})
	const data = await response.json()

	if (response.status === 401) {
		loginError.textContent = data.message
		loginError.classList.remove('display-none')

		email.value = ''
		password.value = ''
	} else {
		window.location.href = data.route
	}
})

buttonRegister.addEventListener('click', async () => {
	const firstName = document.getElementById('registerFirstName')
	const lastName = document.getElementById('registerLastName')
	const email = document.getElementById('registerEmail')
	const password1 = document.getElementById('registerPassword1')
	const password2 = document.getElementById('registerPassword2')

	const identityRegex = /^[a-záéíóúñ]{1,20}$/i
	const emailRegex = /^[A-Za-z0-9_\-]+(\.[A-Za-z0-9_\-]+)*@([A-Za-z0-9_\-]+\.)+[a-z]{2,5}$/
	const passwordRegex = /.{4,}/

	if (!identityRegex.test(firstName.value.trim()) || !identityRegex.test(lastName.value.trim())) {
		registerError.textContent = 'El nombre y apellido solo puede tener letras.'
		registerError.classList.remove('display-none')

		return
	}

	if (!emailRegex.test(email.value.trim())) {
		registerError.textContent = 'El correo no cumple con el formato solicitado.'
		registerError.classList.remove('display-none')

		return
	}

	if (!passwordRegex.test(password1.value)) {
		registerError.textContent = 'La contraseña debe tener un mínimo de 4 caracteres.'
		registerError.classList.remove('display-none')

		return
	}

	if (password1.value !== password2.value) {
		registerError.textContent = 'Las contraseñas no coinciden entre sí.'
		registerError.classList.remove('display-none')

		return
	}

	const response = await fetch('/register', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			first_name: firstName.value.trim(),
			last_name: lastName.value.trim(),
			email: email.value.trim(),
			password: password1.value
		})
	})
	const data = await response.json()

	if (response.status !== 200) {
		registerError.textContent = data.message
		registerError.classList.remove('display-none')

		firstName.value = ''
		lastName.value = ''
		email.value = ''
		password1.value = ''
		password2.value = ''
	} else {
		window.location.href = data.route
	}
})
