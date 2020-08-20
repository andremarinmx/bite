from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/login')
def login_endpoint():
	return '/login'

@api.route('/register')
def register_endpoint():
	return '/register'
