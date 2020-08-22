import os
from flask import (
	Flask,
	render_template,
	request,
	send_from_directory,
	session
)
from api import api
from login import LoginHandler
from db import db

app = Flask(__name__)
app.register_blueprint(api)

app.secret_key = os.environ.get('SECRET_KEY', '05d08a3aa04b7283bba6ebf3')
app.config['LOGIN_REQUIRED_FALLBACK_PAGE'] = '/'
app.config['LOGOUT_REQUIRED_FALLBACK_PAGE'] = '/home'
app.config['LOGIN_SESSION_NAME'] = 'user_id'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///Data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login = LoginHandler(app)

@app.before_first_request
def create_tables():
	db.create_all()

@app.route('/')
@login.logout_required
def root():
	return render_template('index.html')
	
@app.route('/recover')
def recover():
	return '/recover'

@app.route('/home')
@login.login_required
def home():
	return render_template('home.html')

@app.route('/category/<int:category_id>')
def category(category_id: int):
	return '/category/:id'

@app.route('/search')
def search():
	return '/search'

@app.route('/orders')
def orders():
	return '/orders'

@app.route('/orders/<int:order_id>')
def order(order_id: int):
	return '/orders/:id'

@app.route('/opinion')
def opinion():
	return '/opinion'

@app.route('/profile')
def profile():
	return '/profile'

@app.route('/add_product')
def add_product():
	return '/add_product'

@app.route('/product/<int:product_id>')
def product(product_id: int):
	return '/product/:id'

@app.route('/edit_product/<int:product_id>')
def edit_product(product_id: int):
	return '/edit_product/:id'

@app.route('/settings')
def settings():
	return '/settings'

@app.route('/edit_profile')
def edit_profile():
	return '/edit_profile'

@app.route('/about')
def about():
	return '/about'

@app.route('/about/<string:page>')
def about_page(page: str):
	return '/about/:page'

# Archivos estáticos.

@app.route('/manifest.json')
def manifest():
	return send_from_directory('static', 'manifest.json')

@app.route('/favicon.ico')
def favicon():
	return send_from_directory('static/icons', 'icon-72x72.png')

@app.route('/icons/<string:filename>')
def icons(filename):
	return send_from_directory('static/icons', filename)

db.init_app(app)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)
