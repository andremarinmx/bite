from flask import Blueprint, redirect, request, session
from models.UserModel import UserModel
import re
import bcrypt

api = Blueprint('api', __name__)

@api.route('/login', methods = ['POST'])
def login_endpoint():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')

	if email and password:
		user = UserModel.find_by_email(email)
		if user is None:
			return {"message": "El correo electrónico no está registrado."}, 401
		if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
			session['user_id'] = user.user_id
			return {"route": "/home"}
		return {"message": "La contraseña de acceso es incorrecta."}, 401
	return {"message": "El correo electrónico o la contraseña son incorrectos."}, 401

@api.route('/register', methods = ['POST'])
def register_endpoint():
	data = request.get_json()
	first_name = data.get('first_name')
	last_name = data.get('last_name')
	email = data.get('email')
	password = data.get('password')

	if first_name and last_name and email and password:
		identityRegex = re.compile(r'^[a-záéíóúñ]{1,20}$', re.IGNORECASE)
		emailRegex = re.compile(r'^[A-Za-z0-9_\-]+(\.[A-Za-z0-9_\-]+)*@([A-Za-z0-9_\-]+\.)+[a-z]{2,5}$')
		passwordRegex = re.compile(r'.{4,}')

		if identityRegex.match(first_name) is None or identityRegex.match(last_name) is None:
			return {"message": "El formato del nombre y apellido no es válido; no puede contener símbolos o números."}, 400
		if emailRegex.match(email) is None:
			return {"message": "El correo no cumple con el formato solicitado."}
		if passwordRegex.match(password) is None:
			return {"message": "La contraseña no cumple con el formato solicitado."}

		if UserModel.find_by_email(email):
			return {"message": "Ya existe una cuenta registrada con ese correo."}, 400
		
		hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
		new_user = UserModel(first_name, last_name, email, hashed_password)
		new_user.save_to_db()

		new_user = UserModel.find_by_email(email) # Get the same user, but with ID.
		session['user_id'] = new_user.user_id
		return {"route": "/home"}
	return {"message": "Los datos de registro ingresados no son válidos."}, 400

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
