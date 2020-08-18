from flask import (
	Blueprint,
	request,
	session
)

api = Blueprint('api', __name__)

@api.route('/login', methods = ['POST'])
def login_endpoint():
	username = request.form.get('username')
	password = request.form.get('password')
	if username and password:
		# TODO: Agregar verificación con UserModel y establecer el id
		# en la sesión.
		return {
			"message": "All correct."
		}
	return {
		"message": "No valid data received (username, password)."
	}, 400

@api.route('/register', methods = ['POST'])
def register_endpoint():
	# TODO: Validar los datos de registro, luego guardar al usuario
	# con UserModel.
    return '/register'

@api.route('/logout')
def logout_user():
	# TODO: Con try/except quitar el id del usuario de la sesión,
	# luego volver al inicio.
	return '/logout'

@api.route('/posts')
def get_posts():
	# TODO: Con ProductModel obtener una lista de productos públicos y
	# enviarlos como JSON.
	return []
