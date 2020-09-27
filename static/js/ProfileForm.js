const profileDataForm = document.getElementById('profileDataForm')

const firstName = document.getElementById('firstName')
const lastName = document.getElementById('lastName')
const email = document.getElementById('email')

const profileError = document.getElementById('profileError')

// Ocultar mensajes de error.
profileError.addEventListener('click', (event) => {
	event.target.classList.add('display-none')
})

// Habilitar el botón de Guardar cuando se modifiquen los datos.
const enableButton = () => {
	document.getElementById('buttonUpdateData').removeAttribute('disabled')
}
firstName.addEventListener('change', enableButton)
lastName.addEventListener('change', enableButton)
email.addEventListener('change', enableButton)

// Guardar los datos (enviar a la API).
profileDataForm.addEventListener('submit', async (event) => {
	event.preventDefault()

	const identityRegex = /^[a-záéíóúñ]{1,20}( [a-záéíóúñ]{1,20})?$/i
	const emailRegex = /^[A-Za-z0-9_\-]+(\.[A-Za-z0-9_\-]+)*@([A-Za-z0-9_\-]+\.)+[a-z]{2,5}$/

	if (!identityRegex.test(firstName.value.trim()) || !identityRegex.test(lastName.value.trim())) {
		profileError.textContent = 'El nombre y apellido no es válido.'
		profileError.classList.remove('display-none')

		return
	}

	if (!emailRegex.test(email.value.trim())) {
		profileError.textContent = 'El correo no parece ser un correo realmente...'
		profileError.classList.remove('display-none')

		return
	}
	
	// Realizar la petición.
	const response = await fetch('/users', {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			first_name: firstName.value.trim(),
			last_name: lastName.value.trim(),
			email: email.value.trim()
		})
	})
	const data = await response.json()

	if (response.status !== 200) {
		profileError.textContent = data.message
		profileError.classList.remove('display-none')
	} else {
		window.location.reload()
	}
})
