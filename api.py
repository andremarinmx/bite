from flask import (
	Blueprint,
	jsonify,
	session
)

api = Blueprint('api', __name__)

@api.route('/login', methods = ['POST'])
def login_endpoint():
	return '/login'

@api.route('/register', methods = ['POST'])
def register_endpoint():
    return '/register'

@api.route('/logout')
def logout_user():
	return '/logout'

@api.route('/posts')
def get_posts():
	return jsonify([])
