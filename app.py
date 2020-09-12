import os
from flask import Flask, render_template, request, send_from_directory, session
from api import api
from login import LoginHandler
from models.Category import CategoryModel
from models.Favourite import FavouriteModel
from models.Opinion import OpinionModel
from models.Order import OrderModel
from models.Product import ProductModel
from models.Report import ReportModel
from models.User import UserModel
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
	"""Crear tablas de la base de datos cuando se utiliza por primera vez."""
	db.create_all()

@app.before_request
def make_session_permanent():
	"""Hacer que la sesión sea permanente al iniciar sesión."""
	session.permanent = True

@app.errorhandler(404)
def not_found(e):
	"""Mostrar la página de 404 si una ruta no se encuentra."""
	user_id = session.get('user_id')
	return render_template('404.html', user_id = user_id), 404

@app.route('/')
@login.logout_required
def root():
	"""Página de acceso al sitio, iniciando sesión y registrándose."""
	return render_template('index.html')

@app.route('/recover')
def recover():
	"""Página para recuperar la contraseña."""
	return '/recover'

@app.route('/home')
@login.login_required
def home():
	"""Página de inicio, muestra las categorías de los productos."""
	return render_template('home.html')

@app.route('/category/<int:category_id>')
def category(category_id: int):
	"""Muestra los productos que pertenecen a cierta categoría."""
	return '/category/:id'

@app.route('/search')
@login.login_required
def search():
	"""Página para buscar productos."""
	return render_template('search.html')

@app.route('/orders')
@login.login_required
def orders():
	"""Muestra las órdenes realizadas o las órdenes pendientes en forma de lista."""
	return render_template('orders.html')

@app.route('/orders/<int:order_id>')
def order(order_id: int):
	"""Muestra los detalles de una orden en especial."""
	return '/orders/:id'

@app.route('/opinion')
def opinion():
	"""Crea una opinión del usuario sobre el producto."""
	return '/opinion'

@app.route('/profile')
@login.login_required
def profile():
	"""Visitar el perfil del usuario que está en la sesión."""
	user = UserModel.find_by_id(session.get('user_id'))
	return render_template('profile.html', user = user)

@app.route('/add_product')
def add_product():
	"""Agregar un nuevo producto al catálogo si el usuario es vendedor."""
	return '/add_product'

@app.route('/product/<int:product_id>')
def product(product_id: int):
	"""Muestra los detalles de un producto en particular."""
	return '/product/:id'

@app.route('/edit_product/<int:product_id>')
def edit_product(product_id: int):
	"""Se modifica algún aspecto del producto ya creado."""
	return '/edit_product/:id'

@app.route('/settings')
@login.login_required
def settings():
	"""Muestra el menú de configuración general para la cuenta."""
	user = UserModel.find_by_id(session.get('user_id'))
	return render_template('settings.html', user = user)

@app.route('/edit_profile')
def edit_profile():
	"""Se modifican los datos del perfil del usuario."""
	return '/edit_profile'

@app.route('/about')
def about():
	"""Muestra un menú con las secciones de información sobre la aplicación."""
	return '/about'

@app.route('/about/<string:page>')
def about_page(page: str):
	"""Muestra la información de la página que hay en ella."""
	return '/about/:page'

# Archivos estáticos.

@app.route('/icons/<string:filename>')
def icons(filename):
	"""Devuelve un ícono de la aplicación."""
	return send_from_directory('static/icons', filename)

db.init_app(app)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)
