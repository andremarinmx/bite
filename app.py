import os
from flask import (
	Flask,
	render_template,
	send_from_directory,
	session, 
	request
	
)
from api import api
from login import LoginHandler

app = Flask(__name__)
app.register_blueprint(api)

app.secret_key = os.environ.get('SECRET_KEY', '05d08a3aa04b7283bba6ebf3')
app.config['LOGIN_REQUIRED_FALLBACK_PAGE'] = '/'
app.config['LOGOUT_REQUIRED_FALLBACK_PAGE'] = '/home'
app.config['LOGIN_SESSION_NAME'] = 'user_id'

login = LoginHandler(app)

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/login')
def login():
	return '/login'
	
@app.route('/register')
def register():
    return '/register'
	
@app.route('/recover')
def recover():
    return '/recover'

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/category/:id')
def category(categoty_id:int):
    return '/category/:id'

@app.route('/search')
def search():
    return '/search'

@app.route('/orders/:id')
def orders(orders_id:int):
    return '/orders/:id'

@app.route('/opinion')
def opinion():
    return '/opinion'

@app.route('/profile')
def profile():
    return '/profile'

@app.route('/add_product')
def add_product():
    return '/add product'

@app.route('/product/:id')
def product(product_id:int):
    return '/product/:id'

@app.route('/edit_product/:id')
def edit_product(edit_product_id:int):
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

@app.route('/about/:page')
def about_page(about_page:int):
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

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)