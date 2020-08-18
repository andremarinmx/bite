import os
from flask import (
	Flask,
	render_template,
	send_from_directory,
	session
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

@app.route('/home')
def home():
	return render_template('home.html')



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
