from flask import Blueprint, redirect, request, session

api = Blueprint('api', __name__)

@api.route('/login', methods = ['POST'])
def login_endpoint():
	username = request.form.get('username')
	password = request.form.get('password')
	if username and password:
		# TODO: Agregar verificación con UserModel y establecer el id
		# en la sesión.
		return {"route": "/home"}
	return {"message": "El correo electrónico o la contraseña son incorrectos."}, 400

@api.route('/register', methods = ['POST'])
def register_endpoint():
	# TODO: Validar los datos de registro, luego guardar al usuario
	# con UserModel.
	return '/register'

@api.route('/logout')
def logout_user():
	if session.get('user_id'):
		session.pop('user_id')
	return redirect('/')

@api.route('/posts')
def get_posts():
	# TODO: Con ProductModel obtener una lista de productos públicos y
	# enviarlos como JSON.
	return []
